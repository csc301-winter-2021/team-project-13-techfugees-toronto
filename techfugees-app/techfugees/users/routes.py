from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from flask_login import login_user, current_user, logout_user, login_required
from techfugees import db, bcrypt
from techfugees.models import User, Post, Tenant, Landlord
from techfugees.users.forms import RegistrationForm, LoginForm, UpdateLandlord, UpdateTenant, LandlordRegistrationForm, TenantRegistrationForm


users = Blueprint('users', __name__)

@users.route('/register/tenant', methods=['GET', 'POST'])
def tenant_register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = TenantRegistrationForm()
    if form.validate_on_submit():
        #password hashing to lessen impact of man in the middle attacks
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Tenant(
            username=form.username.data, 
            email=form.email.data, 
            location=form.location.data,
            password=hashed_password,
            sponsor_name = form.sponsor_name.data,
            num_of_people = form.num_of_people.data,
            length_of_stay = form.length_of_stay.data,
            special_requirements = form.special_requirements.data
        )
        db.session.add(user)
        db.session.commit()

        flash('Account Created!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register/tenant-register.html', title="Create A Tenant Account", form=form)

@users.route('/register/landlord', methods=['GET', 'POST'])
def landlord_register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LandlordRegistrationForm()
    if form.validate_on_submit():
        #password hashing to lessen impact of man in the middle attacks
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Landlord(
            username=form.username.data, 
            email=form.email.data,
            phone_number=form.phone_number.data,
            location=form.location.data,
            password=hashed_password, 
            credit_check=form.credit_check.data, 
            first_last=form.first_last.data,
            no_cosigner=form.no_cosigner.data
        )
        db.session.add(user)
        db.session.commit()

        flash('Account Created!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register/landlord-register.html', title="Create A Landlord Account", form=form)


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
    if current_user.checker == "landlord":
        form = UpdateLandlord()
    elif current_user.checker == "tenant":
        form = UpdateTenant()

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.location = form.location.data
        if current_user.checker == "landlord":
            current_user.phone_number = form.phone_number.data
            current_user.no_cosigner = form.no_cosigner.data
            current_user.credit_check = form.credit_check.data
            current_user.first_last = form.first_last.data
        else:
            current_user.sponsor_name = form.sponsor_name.data
            current_user.num_of_people = form.num_of_people.data
            current_user.length_of_stay = form.length_of_stay.data
            current_user.special_requirements = form.special_requirements.data

        db.session.commit()
        flash('Account Updated!', 'success') #second param is for bootstrap class
        return redirect(url_for('users.account'))
    
    elif request.method == 'GET': #populate fields
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.location.data = current_user.location
        if current_user.checker == "landlord":
            form.phone_number.data = current_user.phone_number
            if current_user.no_cosigner:
                form.no_cosigner.data = 1
            if current_user.credit_check:
                form.credit_check.data = 1
            if current_user.first_last:
                form.first_last.data = 1
        else:
            form.sponsor_name.data = current_user.sponsor_name
            form.num_of_people.data = current_user.num_of_people
            form.length_of_stay.data = current_user.length_of_stay
            form.special_requirements.data = current_user.special_requirements

    if current_user.checker == "landlord":
        return render_template('account/landlord-account.html', title='Account', form=form)
    else:
        return render_template('account/tenant-account.html', title='Account', form=form)


# show wish list
@users.route('/wishList', methods=['GET','POST'])
@login_required
def wishList():
    post = Post.query.filter_by().all()
    user = Tenant.query.get_or_404(current_user.id)
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

    elif user.checker == "tenant":
        return render_template('profile/tenant-profile.html', title='Tenant Profile', user=user)








    #return render_template('my_listings.html', title='My Listings', listings=listings)