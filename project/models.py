from project import db
from project import bcrypt
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
import datetime


class BlogPost(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.datetime.utcnow())
    author_id = db.Column(db.Integer, ForeignKey("users.id"))
    comments = relationship("Comment", backref="comments")

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author_id = author

    def __repr__(self):
        return 'title {}| {}'.format(self.title, self.description)


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, ForeignKey('users.id'), default=1)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, post_id, user_id, title, content):
        self.post_id = post_id
        self.user_id = user_id
        self.title = title
        self.content = content

    def __repr__(self):
        return 'zadeva: {} | {}'.format(self.title, self.content)


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(155), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = relationship("BlogPost", backref="author")
    comments = relationship("Comment", backref="commentator")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name {}'.format(self.name)