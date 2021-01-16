from reddit_saved import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(40), nullable=False)
    email =db.Column(db.String(140), nullable=True)
    access_token = db.Column(db.String(100), nullable=False)
    # saved = db.relationship('Saved', backref = 'user', lazy=True)

    def __repr__(self):
        return f"user={self.username}, id={self.id}, access_token={self.access_token}"




class Saved(db.Model):

    id = db.Column(db.Integer, primary_key = True)
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