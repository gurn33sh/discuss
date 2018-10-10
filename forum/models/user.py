from forum import db
from flask_login import UserMixin

class User(db.Model, UserMixin):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    registered_on = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )

    texts = db.relationship('Text', backref='user', lazy='dynamic')
    links = db.relationship('Link', backref='user', lazy='dynamic')

    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    post_karma = db.Column(db.Integer, nullable=False, default=0)
    comment_karma = db.Column(db.Integer, nullable=False, default=0)

    has_upvoted = db.relationship('ThreadUpvote', backref='user', lazy='dynamic')
    has_downvoted = db.relationship('ThreadDownvote', backref='user', lazy='dynamic')

    has_upvoted_comment = db.relationship(
        'CommentUpvote', backref='user', lazy='dynamic'
    )
    has_downvoted_comment = db.relationship(
        'CommentDownvote', backref='user', lazy='dynamic'
    )