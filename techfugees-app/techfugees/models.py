from techfugees import db, login_manager, app
from datetime import datetime
from flask_login import UserMixin #adds attributes lik authenticated, active, anon

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#need to split User into refugee and landlord classes
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    landlord = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.username}, {self.email}, {self.image_file}')"

class Refugee(User):
    wish_list = db.Column(db.String(200), default='')

    def __repr__(self):
        return f"User('{self.username}, {self.email}, {self.image_file}')"

#template class, eventually change to fit rental postings
class Post(db.Model):
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
    wish_user = db.Column(db.String(2000), default='')

    def __repr__(self):
        return f"Post('{self.title}, {self.id}, {self.date_posted}, {self.address}, {self.city}, {self.pet}, {self.smoking}, {self.balcony}, {self.air_conditioning}, {self.stove_oven}, {self.washer}, {self.dryer}, {self.dishwasher}, {self.microwave}, {self.cable}, {self.water}, {self.electricity}, {self.num_bathrooms}, {self.num_bedrooms}, {self.type_of_building},')"