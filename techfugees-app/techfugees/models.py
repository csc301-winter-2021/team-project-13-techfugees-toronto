from techfugees import db, login_manager, app
from datetime import datetime
from flask_login import UserMixin #adds attributes lik authenticated, active, anon
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#need to split User into refugee and landlord classes dad
class User(db.Model, Base, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    type = db.Column(db.String(50))
    
    __mapper_args__ = {
        'polymorphic_on':type,
        'polymorphic_identity':'user'
    }

    def __repr__(self):
        return f"User('{self.username}, {self.email}, {self.image_file}')"

class Landlord(User):
    __tablename__ = 'landlord'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    credit_check = db.Column(db.Boolean, default=False)
    first_last = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post', backref='author', lazy="joined")
    checker = db.Column(db.String(20), default="landlord")

    __mapper_args__ = {
        'polymorphic_identity':'landlord'
    }
    
    def __repr__(self):
        return f"User('{self.username}')"

class Refugee(User):
    __tablename__ = 'refugee'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    sponsor_name = db.Column(db.String(20), default="none")
    checker = db.Column(db.String(20), default="refugee")

    __mapper_args__ = {
        'polymorphic_identity':'refugee'
    }

#template class, eventually change to fit rental postings
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('landlord.id'), nullable=False, unique=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.title}, {self.id}, {self.date_posted}')"