from flask import Blueprint

from flask import render_template, url_for, flash, redirect, request, abort
from techfugees import app, db, bcrypt
from techfugees.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from techfugees.posts.forms import NewListingForm
from techfugees.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)