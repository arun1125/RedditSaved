from reddit_saved import app, db
from reddit_saved.reddit_saved import reddit_saved
from reddit_saved.models import userinfo, savedposts
from uuid import uuid4
from flask_restful import reqparse
from flask import url_for, redirect, render_template, request, session, make_response




@app.route('/')
# @api.route('/api/')
def home():
    access_token = request.args.get('access_token', default = "None", type = int)

    if access_token == "None":
        return redirect(url_for('login'))
    else:
        rs = reddit_saved(session['access_token'])
        username = str(rs.reddit.user.me())
        # return redirect(url_for('homepage',access_token = session['access_token']))
        access_token = session['access_token']
        return redirect(f'http://localhost:80/Main/{access_token}')

@app.route('/login')
def login():

    rs = reddit_saved()
    auth_url = rs.make_authorization_url()
    text = f'<a href={auth_url}>Authenticate with reddit</a>'
    return {'login_url':auth_url}



# # Left as an exercise to the reader.
# # You may want to store valid states in a database or memcache.
# def save_created_state(state):
#     pass
# def is_valid_state(state):
#     return True

@app.route('/reddit_callback')
def reddit_callback():
    parser = reqparse.RequestParser()
    parser.add_argument('code')
    args = parser.parse_args()
    code = args.get('code')
    
    
    rs = reddit_saved()
    access_token = rs.reddit.auth.authorize(code)

    # session['access_token'] = access_token
    #once they login see if they're existing users or not! 
    #so route to the check user function and do the shit there
    #should I send back to the front end with the access token

    return redirect(url_for('check_user', access_token = access_token))
    # return redirect(f'/checkuser/{access_token}') 
    
    
@app.route('/checkuser/<access_token>', methods = ['GET', 'POST'])
def check_user(access_token):
    
    #check if user is in database
    rs = reddit_saved(access_token)
    username = str(rs.reddit.user.me())
    
    exists = db.engine.execute(f"""
                        SELECT username
                        FROM redditsaved.userinfo
                        WHERE username = '{username}'
                        """).fetchall()

    print(exists)

    if exists:
        # user = User.query.filter(User.username == username).first()
        # user.access_token = access_token
        # db.session.commit()

        db.engine.execute(f"""
                        UPDATE redditsaved.userinfo 
                        SET access_token = '{access_token}'
                        WHERE username = '{username}' 
                        """)


        # return redirect(url_for('homepage',access_token = access_token))
        return redirect(f'http://localhost:80/Main/{access_token}')

    else:
        user = userinfo(username = username, access_token = access_token)
        db.session.add(user)
        db.session.commit()

        # db.engine.execute(f"""
        #                 INSERT INTO redditsaved.userinfo 
        #                 {user}
        #                 """)
        return redirect(url_for('get_saved_posts', access_token = access_token))
        # return redirect(f'/getsavedposts/{access_token}')


@app.route('/getsavedposts/<access_token>')
def get_saved_posts(access_token):
    rs = reddit_saved(access_token)
    username = str(rs.reddit.user.me())
    saved_posts = rs.get_saved_posts(username)
    # num_posts = db.session.query(Saved).filter_by(username = username).count()
    # num_posts_to_update = len(saved_posts) - num_posts
    # if num_posts_to_update != 0:
    #     posts_to_update = saved_posts[-num_posts_to_update:]
    #     db.session.add_all(posts_to_update)
    #     db.session.commit()
    print(saved_posts)
    db.session.add_all(saved_posts)
    db.session.commit()


    # return redirect(url_for('add_email', username=username))
    # return redirect(url_for('homepage',access_token = access_token)) 
    return redirect(f'http://localhost:80/Main/{access_token}')


# @app.route('/add_email/<username>', methods = ['GET','POST'])
# def add_email(username):
#     if request.method == 'POST':
#         email = request.form['add_email']

#         db.engine.execute(f"""
#                             UPDATE Saved 
#                             SET email = '{email}'
#                             WHERE username = '{username}' 
#                             AND email = ''
#                             """)

#         return redirect(url_for('homepage',username=username)) 

#     else:
#         return render_template('add_email.html', value=username)

@app.route('/AddEmail/<access_token>', methods = ['POST'])
def AddEmail(access_token):
    rs = reddit_saved(access_token)
    username = str(rs.reddit.user.me())

    email = request.get_json()

    db.engine.execute(f"""
                        UPDATE redditsaved.savedposts 
                        SET email = '{email}'
                        WHERE username = '{username}' 
                        AND email = ''
                        """)

    # posts = db.engine.execute(f"""
    #                         SELECT permalink
    #                         FROM Saved
    #                         WHERE username = '{username}'
    #                         ORDER BY RANDOM()
    #                         LIMIT {5}
    #                         """).fetchall()
    # posts = [str(posts[k])[2:-4] for k in range(len(posts))]

    # rs.email_user(email, posts)

    return {'got_email': True}

    # if request.method == 'POST':
    #     # email = request.form['']
    #     print(request.get_json())
    #     return redirect(f'http://localhost:3000/Main/{access_token}')
    # else:
    #     return redirect(f'http://localhost:3000/Main/{access_token}')

    
@app.route('/homepage/<access_token>')
def homepage(access_token, n=5):

    rs = reddit_saved(access_token)
    username = str(rs.reddit.user.me())
    posts = db.engine.execute(f"""
                            SELECT permalink
                            FROM redditsaved.savedposts
                            WHERE username = '{username}'
                            ORDER BY RANDOM()
                            LIMIT {n}
                            """).fetchall()

    # postString = f'<h1>{posts}</h1>'
    posts_json = {str(k):str(posts[k])[2:-4] for k in range(len(posts))}
    posts_json['access_token'] = str(access_token)
    # make_response()
    return posts_json


    
#add a scheduled job to update saved posts and update emails 
