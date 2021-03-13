from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from flask_login import login_user, current_user, logout_user, login_required
from techfugees import db, bcrypt
from techfugees.models import User, Post, Refugee, Landlord
from techfugees.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, LandlordRegistrationForm


users = Blueprint('users', __name__)

@users.route('/register/refugee', methods=['GET', 'POST'])
def refugee_register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        #password hashing to lessen impact of man in the middle attacks
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Refugee(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Account Created!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title="Create A Refugee Account", form=form)

@users.route('/register/landlord', methods=['GET', 'POST'])
def landlord_register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LandlordRegistrationForm()
    if form.validate_on_submit():
        #password hashing to lessen impact of man in the middle attacks
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Landlord(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Account Created!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title="Create A Landlord Account", form=form)

@users.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next') #redirect to page they were trying to access before authentication
            if next_page:
                return redirect(next_page)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid Credentials!', 'danger')
    return render_template('login.html', title='Login', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@users.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account Updated!', 'success') #second param is for bootstrap class
        return redirect(url_for('users.account'))
    elif request.method == 'GET': #populate fields
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)


# show wish list
@users.route('/wishList', methods=['GET','POST'])
@login_required
def wishList():
    post = Post.query.filter_by().all()
    user = Refugee.query.get_or_404(current_user.id)
    wishes = user.wish_list.split(",")
    if wishes == [""]:
        wishes = []
    wish_list = []
    for p in post:
        if str(p.id) in wishes:
            wish_list.append(p)
    return render_template('wishList.html', title='Wish List', wish_list=wish_list)

#should add custom @landlord decorator
@users.route('/my-listings', methods=['GET','POST'])
@login_required
def my_listings():
    post_arr = Post.query.all()
    listings = []
    for p in post_arr:
        if p.user_id == current_user.id:
            listings.append(p)
    return render_template('my_listings.html', title='My Listings', listings=listings)

#should add custom @landlord decorator
@users.route('/profile/<string:username>', methods=['GET','POST'])
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first()
    if user.checker == "landlord":

        #obtain listings information of landlord
        post_arr = Post.query.all()
        listings = []
        for p in post_arr:
            if p.user_id == user.id:
                listings.append(p)
        if current_user.username == user.username:
            return render_template('profile/landlord-profile.html', title='My Profile', listings=listings, user=current_user)
        else:
            return render_template('profile/landlord-profile.html', title='Other Landlord Profile', listings=listings, user=user)

    elif user.checker == "refugee":
        return render_template('profile/refugee-profile.html', title='Refugee Profile', user=user)








    #return render_template('my_listings.html', title='My Listings', listings=listings)