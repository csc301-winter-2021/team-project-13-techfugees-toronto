from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, SelectField, \
    RadioField
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
    price = StringField('Price description', validators=[DataRequired()])
    submit = SubmitField('Post')


class NewReviewForm(FlaskForm):
    # stars = IntegerField('# of Stars', validators=[DataRequired()])
    stars = RadioField('# of stars', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1')
    comment = TextAreaField('comment', validators=[DataRequired()])
    submit = SubmitField('Post')


class NewSearchForm(FlaskForm):
    address = SelectField('Address')
    city = SelectField('City')
    type_of_building = SelectField('Type of Building')
    num_bedrooms = SelectField('# of Bedrooms')
    num_bathrooms = SelectField('# of bathrooms')
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
    submit = SubmitField('Search')


class MapSearchForm(FlaskForm):
    type_of_building = SelectField('Type of Building')
    submit = SubmitField('Search')
