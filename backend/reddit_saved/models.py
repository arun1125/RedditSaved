from reddit_saved import db


class userinfo(db.Model):
    # __bind_key__ = 'other_schema'
    # id = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key = True, autoincrement=True)
    username = db.Column(db.String(40), primary_key = True, nullable=False)
    email =db.Column(db.String(140), nullable=True)
    access_token = db.Column(db.String(100), nullable=False)
    # saved = db.relationship('Saved', backref = 'user', lazy=True)

    def __repr__(self):
        return f"user={self.username}, id={self.id}, access_token={self.access_token}"




class savedposts(db.Model):
    # __bind_key__ = 'other_schema'

    id = db.Column(db.String(50), primary_key = True)
    username = db.Column(db.String(40), nullable=False)
    email =db.Column(db.String(140), nullable=True)
    post_id = db.Column(db.String(50), nullable = False)
    score = db.Column(db.Integer, nullable = True)
    permalink = db.Column(db.String(250), nullable = False)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"""
        user={self.username}, post_id={self.post_id},
        email= {self.email}
        """


#     CREATE TABLE savedposts (
# 	id BIGINT PRIMARY KEY ,
# 	username VARCHAR ( 50 )  ,
#  	email VARCHAR ( 255 )  ,
#  	post_id VARCHAR ( 255 )  ,
#  	score INT,
#  	permalink VARCHAR ( 255 )  
#  );


# CREATE TABLE userinfo (
# 	id BIGINT PRIMARY KEY ,
# 	username VARCHAR ( 50 ) UNIQUE ,
# 	email VARCHAR ( 255 ) UNIQUE ,
# 	access_token VARCHAR ( 255 ) UNIQUE ,
# );