from techfugees import db, login_manager, app
from datetime import datetime
from flask_login import UserMixin #adds attributes lik authenticated, active, anon
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#need to split User into tenant and landlord classes
class User(db.Model, Base, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    location = db.Column(db.String(20), unique=False, nullable=True)
    reviews = db.relationship('Review', backref='user')
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
    no_cosigner = db.Column(db.Boolean, default=False)
    phone_number = db.Column(db.String(20), unique=False, nullable=True)
    posts = db.relationship('Post', backref='author', lazy="joined")
    checker = db.Column(db.String(20), default="landlord")

    __mapper_args__ = {
        'polymorphic_identity':'landlord'
    }

    def __repr__(self):
        return f"User('{self.username}')"

class Tenant(User):
    __tablename__ = 'tenant'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    sponsor_name = db.Column(db.String(20), default="none")
    preferred_location = db.Column(db.String(50), default="none")
    num_of_people = db.Column(db.Integer, default="none")
    length_of_stay = db.Column(db.Integer, default="none")
    special_requirements = db.Column(db.String(120), default="none")
    checker = db.Column(db.String(20), default="tenant")
    wish_list = db.Column(db.String(200), default='')
    __mapper_args__ = {
        'polymorphic_identity':'tenant'
    }

#template class, eventually change to fit rental postings
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    pet = db.Column(db.Boolean, default=False)
    smoking = db.Column(db.Boolean, default=False)
    balcony = db.Column(db.Boolean, default=False)
    air_conditioning = db.Column(db.Boolean, default=False)
    stove_oven = db.Column(db.Boolean, default=False)
    washer = db.Column(db.Boolean, default=False)
    dryer = db.Column(db.Boolean, default=False)
    dishwasher = db.Column(db.Boolean, default=False)
    microwave = db.Column(db.Boolean, default=False)
    cable = db.Column(db.Boolean, default=False)
    water = db.Column(db.Boolean, default=False)
    electricity = db.Column(db.Boolean, default=False)
    num_bedrooms = db.Column(db.Integer, nullable=False)
    num_bathrooms = db.Column(db.Integer, nullable=False)
    type_of_building = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    wish_user = db.Column(db.String, default='')
    reviews = db.relationship('Review', backref='post')
    latitude = db.Column(db.String, default='')
    longitude = db.Column(db.String, default='')

    def __repr__(self):
        return f"Post('{self.title}, {self.id}, {self.date_posted}, {self.address}, {self.city}, {self.pet}, {self.smoking}, {self.balcony}, {self.air_conditioning}, {self.stove_oven}, {self.washer}, {self.dryer}, {self.dishwasher}, {self.microwave}, {self.cable}, {self.water}, {self.electricity}, {self.num_bathrooms}, {self.num_bedrooms}, {self.type_of_building},')"


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), default='')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

