from flask import render_template, url_for, flash, redirect, request
from techfugees import app, db, bcrypt
from techfugees.forms import RegistrationForm, LoginForm, UpdateAccountForm, NewListingForm
from techfugees.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        #password hashing to lessen impact of man in the middle attacks
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Account Created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Create an Account", form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next') #redirect to page they were trying to access before authentication
            if next_page:
                return redirect(next_page)
            return redirect(url_for('index'))
        else:
            flash('Invalid Credentials!', 'danger')
    return render_template('login.html', title='login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account Updated!', 'success') #second param is for bootstrap class
        return redirect(url_for('account'))
    elif request.method == 'GET': #populate fields
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)

@app.route('/post/new', methods=['GET','POST'])
@login_required
def new_rental_posting():
    form = NewListingForm()
    if form.validate_on_submit():
        listing = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(listing)
        db.session.commit()
        flash('Listing Added!', 'success')
        return redirect(url_for('index'))
    return render_template('create_post.html', title='Add New Listing', form=form)