from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request, abort
from techfugees import app, db, bcrypt
from techfugees.users.forms import RegistrationForm, LoginForm, UpdateLandlord, UpdateTenant
from techfugees.posts.forms import NewListingForm
from techfugees.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from techfugees import app

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.index', page=posts.next_num) if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) if posts.has_prev else None

    return render_template('index.html', posts=posts.items, next_url=next_url, prev_url=prev_url)