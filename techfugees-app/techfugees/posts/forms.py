from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from techfugees.models import User


class NewListingForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    pet = BooleanField('Pet Friendly')
    smoking = BooleanField('Smoking Allow')
    balcony = BooleanField('Balcony')
    air_conditioning = BooleanField('Air conditioning')
    stove_oven = BooleanField('Stove and Oven')
    washer = BooleanField('Washer')
    dryer = BooleanField('Dryer')
    dishwasher = BooleanField('Dishwasher')
    microwave = BooleanField('Microwave')
    cable = BooleanField('Cable')
    water = BooleanField('Water')
    electricity = BooleanField('Electricity')
    content = TextAreaField('Content')
    num_bedrooms = IntegerField('# of Bedrooms', validators=[DataRequired()])
    num_bathrooms = IntegerField('# of bathrooms', validators=[DataRequired()])
    type_of_building = StringField('Type of Building', validators=[DataRequired()])
    submit = SubmitField('Post')


class NewReviewForm(FlaskForm):
    stars = IntegerField('# of Stars', validators=[DataRequired()])
    comment = TextAreaField('comment', validators=[DataRequired()])
    submit = SubmitField('Post')


class NewSearchForm(FlaskForm):
    address = SelectField('Address')
    city = SelectField('City')
    pet = BooleanField('Pet Friendly')
    smoking = BooleanField('Smoking Allow')
    balcony = BooleanField('Balcony')
    air_conditioning = BooleanField('Air conditioning')
    stove_oven = BooleanField('Stove and Oven')
    washer = BooleanField('Washer')
    dryer = BooleanField('Dryer')
    dishwasher = BooleanField('Dishwasher')
    microwave = BooleanField('Microwave')
    cable = BooleanField('Cable')
    water = BooleanField('Water')
    electricity = BooleanField('Electricity')
    content = TextAreaField('Content')
    num_bedrooms = StringField('# of Bedrooms')
    num_bathrooms = StringField('# of bathrooms')
    type_of_building = StringField('Type of Building')
    submit = SubmitField('Search')