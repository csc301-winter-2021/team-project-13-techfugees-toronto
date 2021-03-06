from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from techfugees import db
from techfugees.models import Post, User, Refugee
from techfugees.posts.forms import NewListingForm
from techfugees import app
import os

app.config['UPLOAD_FOLDER'] = 'techfugees-app/techfugees/static/HousePhoto'
posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_rental_posting():
    form = NewListingForm()
    if current_user.checker == 'landlord':
        if form.validate_on_submit():
            listing = Post(title=form.title.data,
                        address=form.address.data,
                        city=form.city.data,
                        pet=form.pet.data,
                        smoking=form.smoking.data,
                        balcony=form.balcony.data,
                        air_conditioning=form.air_conditioning.data,
                        stove_oven=form.stove_oven.data,
                        washer=form.washer.data,
                        dryer=form.dryer.data,
                        dishwasher=form.dishwasher.data,
                        microwave=form.microwave.data,
                        cable=form.cable.data,
                        water=form.water.data,
                        electricity=form.electricity.data,
                        num_bathrooms=form.num_bathrooms.data,
                        num_bedrooms=form.num_bedrooms.data,
                        type_of_building=form.type_of_building.data,
                        content=form.content.data,
                        author=current_user)
            """
            uploaded_file = request.files['file']
            if uploaded_file.filename != '':
                print('ok')
                folder = os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], form.title.data))
                if not folder:
                    os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], form.title.data))
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], form.title.data + '/' + uploaded_file.filename)
                uploaded_file.save(file_path)
            """
            db.session.add(listing)
            db.session.commit()
            flash('Listing Added!', 'success')
            return redirect(url_for('main.index'))
        return render_template('create_post.html', title='Add New Listing', form=form)
    else:
        return redirect(url_for('main.index'))


@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
def listing(post_id):
    wish = False
    listing = Post.query.get_or_404(post_id)
    if current_user.is_authenticated:
        if not current_user.checker == 'landlord':
            user = Refugee.query.filter_by(username=current_user.username).first()
            wishes = user.wish_list.split(",")
            if str(post_id) in wishes:
                wish = True
    if current_user.is_authenticated and current_user.checker == 'refugee':
        return render_template('listing.html', title=listing.title, post=listing, wish=wish, user_type=0)
    elif current_user.is_authenticated:
        return render_template('listing.html', title=listing.title, post=listing, user_type=1)
    else:
        return render_template('listing.html', title=listing.title, post=listing, user_type=-1)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_listing(post_id):
    listing = Post.query.get_or_404(post_id)
    if listing.author != current_user:
        abort(403)
    form = NewListingForm()
    if form.validate_on_submit():
        # SQLalchemy convention, post refers to Post class, and is lowercase here
        listing.title = form.title.data
        listing.content = form.content.data
        db.session.commit()
        flash('Post updated', 'success')
        return redirect(url_for('posts.listing', post_id=listing.id))
    elif request.method == 'GET':
        form.title.data = listing.title
        form.content.data = listing.content

    return render_template('create_post.html', title='Update Post', form=form)


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.index'))


# add to wish list
@posts.route("/post/<int:post_id>/wish", methods=['POST'])
@login_required
def wish_list(post_id):
    user = Refugee.query.get_or_404(current_user.id)
    wishes = user.wish_list.split(",")
    if wishes == [""]:
        wishes = []
    wishes += [post_id]
    user.wish_list = ",".join([str(x) for x in wishes])

    post = Post.query.get_or_404(post_id)
    wish_users = post.wish_user.split(",")
    if wish_users == [""]:
        wish_users = []
    if user.username not in wish_users:
        wish_users += [user.username]
    post.wish_user = ",".join(wish_users)

    db.session.commit()
    return redirect(url_for('main.index'))


@posts.route("/post/<int:post_id>/unwish", methods=['POST'])
@login_required
def unWish(post_id):
    user = Refugee.query.get_or_404(current_user.id)
    wishes = user.wish_list.split(",")
    if wishes == [""]:
        return redirect(url_for('main.index'))
    if str(post_id) in wishes:
        wishes.remove(str(post_id))
    if not wishes:
        user.wish_list = ""
    elif len(wishes) == 1:
        user.wish_list = str(wishes[0])
    else:
        user.wish_list = ",".join([str(x) for x in wishes])

    post = Post.query.get_or_404(post_id)
    wish_users = post.wish_user.split(",")
    if wish_users == [""]:
        return redirect(url_for('main.index'))
    if user.username in wish_users:
        wish_users.remove(user.username)
    if not wish_users:
        post.wish_user = ""
    elif len(wish_users) == 1:
        post.wish_user = str(wish_users[0])
    else:
        post.wish_user = ",".join(wish_users)

    db.session.commit()
    return redirect(url_for('main.index'))

