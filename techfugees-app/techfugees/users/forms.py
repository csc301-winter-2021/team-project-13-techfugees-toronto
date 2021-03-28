from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from techfugees.models import User, Landlord, Tenant

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    location = StringField('location')
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first() #none if no user
        if user is not None:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first() #none if not taken
        if user is not None:
            raise ValidationError('That email is taken. Please choose a different one.')

class LandlordRegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number')
    location = StringField('location')
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    credit_check = BooleanField('Are you willing to accept tenants without a credit score?')
    first_last = BooleanField('Are you willing to omit first and last month\'s rent deposit?')
    no_cosigner = BooleanField('Are you willing to accept tenants who don\'t have a co-signer for the rental agreement?')
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = Landlord.query.filter_by(username=username.data).first() #none if no user
        if user is not None:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = Landlord.query.filter_by(email=email.data).first() #none if not taken
        if user is not None:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateTenant(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    location = StringField('location')
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