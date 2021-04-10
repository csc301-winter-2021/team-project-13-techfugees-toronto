from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from techfugees.models import User, Landlord, Tenant
import re

def check_email(email):
    if email.count('@') != 1:
        return False
    if email[-4:] not in [".com", '.org'] and email[-3:] not in [".ca"]:
        return False
    return True

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password (need at least one digit, uppercase letter, lowercase letter and special character)', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    location = StringField('location')
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        data = username.data
        user = User.query.filter_by(username=data).first() #none if no user
        if user is not None:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        data = email.data
        user = User.query.filter_by(email=data).first() #none if not taken
        if user is not None:
            raise ValidationError('That email is taken. Please choose a different one.')
        if not check_email(data):
            raise ValidationError('Wrong format, email needs to be in xxx@xxx.com or xxx@xxx.ca format.')
        
    def validate_password(self, password):
        data = password.data
        if len(data) < 8:
            raise ValidationError('Minimum length of password is 8.')
        if len(data.strip()) != len(data):
            raise ValidationError('No space at the start or end please.')
        if re.search(r"\d", data) is None:
            raise ValidationError('Need at least one digit.')
        if re.search(r"[A-Z]", data) is None:
            raise ValidationError('Need at least one uppercase letter.')
        if re.search(r"[a-z]", data) is None:
            raise ValidationError('Need at least one lowercase letter.')
        if re.search(r"\W", data) is None:
            raise ValidationError('Need at least one special character. (!@#$...)')

class LandlordRegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number')
    location = StringField('location')
    password = PasswordField('Password (need at least one digit, uppercase letter, lowercase letter and special character)', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    credit_check = BooleanField('Are you willing to accept tenants without a credit score?')
    first_last = BooleanField('Are you willing to omit first and last month\'s rent deposit?')
    no_cosigner = BooleanField('Are you willing to accept tenants who don\'t have a co-signer for the rental agreement?')
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        data = username.data
        user = User.query.filter_by(username=data).first() #none if no user
        if user is not None:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        data = email.data
        user = User.query.filter_by(email=data).first() #none if not taken
        if user is not None:
            raise ValidationError('That email is taken. Please choose a different one.')
        if not check_email(data):
            raise ValidationError('Wrong format, email needs to be in xxx@xxx.com or xxx@xxx.ca format.')
        
    def validate_password(self, password):
        data = password.data
        if len(data) < 8:
            raise ValidationError('Minimum length of password is 8.')
        if len(data.strip()) != len(data):
            raise ValidationError('No space at the start or end please.')
        if re.search(r"\d", data) is None:
            raise ValidationError('Need at least one digit.')
        if re.search(r"[A-Z]", data) is None:
            raise ValidationError('Need at least one uppercase letter.')
        if re.search(r"[a-z]", data) is None:
            raise ValidationError('Need at least one lowercase letter.')
        if re.search(r"\W", data) is None:
            raise ValidationError('Need at least one special character. (!@#$...)')
        
    def validate_phone_number(self, phone_number):
        data = phone_number.data
        if len(data) < 8:
            raise ValidationError('Phone number needs at least 8 digit.')
        if not data.isdigit():
            raise ValidationError('Only digits allowed.') 

class TenantRegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    location = StringField('location')
    password = PasswordField('Password (need at least one digit, uppercase letter, lowercase letter and special character)', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    sponsor_name = StringField('Refugee status', validators=[DataRequired()])
    num_of_people = IntegerField('# of people', validators=[DataRequired()])
    length_of_stay = IntegerField('preferred length of stay(in month)', validators=[DataRequired()])
    special_requirements = TextAreaField('special requirements')
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        data = username.data
        user = User.query.filter_by(username=data).first() #none if no user
        if user is not None:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        data = email.data
        user = User.query.filter_by(email=data).first() #none if not taken
        if user is not None:
            raise ValidationError('That email is taken. Please choose a different one.')
        if not check_email(data):
            raise ValidationError('Wrong format, email needs to be in xxx@xxx.com or xxx@xxx.ca format.')
        
    def validate_password(self, password):
        data = password.data
        if len(data) < 8:
            raise ValidationError('Minimum length of password is 8.')
        if len(data.strip()) != len(data):
            raise ValidationError('No space at the start or end please.')
        if re.search(r"\d", data) is None:
            raise ValidationError('Need at least one digit.')
        if re.search(r"[A-Z]", data) is None:
            raise ValidationError('Need at least one uppercase letter.')
        if re.search(r"[a-z]", data) is None:
            raise ValidationError('Need at least one lowercase letter.')
        if re.search(r"\W", data) is None:
            raise ValidationError('Need at least one special character. (!@#$...)')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateTenant(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    location = StringField('location')
    sponsor_name = StringField('Refugee status', validators=[DataRequired()])
    num_of_people = IntegerField('# of people', validators=[DataRequired()])
    length_of_stay = IntegerField('preferred length of stay(in month)', validators=[DataRequired()])
    special_requirements = TextAreaField('special requirements')
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username: #only want to check availability if changed
            user = User.query.filter_by(username=username.data).first() #none if no user
            if user is not None:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first() #none if not taken
            if user is not None:
                raise ValidationError('That email is taken. Please choose a different one.')

class UpdateLandlord(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number')
    location = StringField('location')
    credit_check = BooleanField('Are you willing to accept tenants without a credit score?')
    first_last = BooleanField('Are you willing to omit first and last month\'s rent deposit?')
    no_cosigner = BooleanField('Are you willing to accept tenants who don\'t have a co-signer for the rental agreement?')
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username: #only want to check availability if changed
            user = User.query.filter_by(username=username.data).first() #none if no user
            if user is not None:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first() #none if not taken
            if user is not None:
                raise ValidationError('That email is taken. Please choose a different one.')