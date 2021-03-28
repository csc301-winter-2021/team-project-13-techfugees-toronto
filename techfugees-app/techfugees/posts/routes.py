from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from techfugees import db
from techfugees.models import Post, User, Refugee, Review
from techfugees.posts.forms import NewListingForm, NewReviewForm, NewSearchForm
from techfugees import app
import os
import time
import shutil

app.config['UPLOAD_FOLDER'] = app.root_path + "/static/HousePhoto"
posts = Blueprint('posts', __name__)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG'])

def allowed_file(filename):
    return '.' in filename and filename.split('.')[-1] in ALLOWED_EXTENSIONS

@app.route('/post/new')
@login_required
def new_rental_posting_template():
    form = NewListingForm()
    return render_template('create_post.html', title='Add New Listing', form=form)


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
            uploaded_file = request.files.getlist("file[]")
            if uploaded_file != []:
                folder = os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], form.title.data))
                if not folder:
                    os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], form.title.data))
                i = 1
                for im in uploaded_file:
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], form.title.data + '/' + "{}.{}".format(time.time(), im.filename[-3:]))
                    if allowed_file(im.filename):
                        im.save(file_path)
                    i = i + 1
            db.session.add(listing)
            db.session.commit()
            flash('Listing Added!', 'success')
            return redirect(url_for('main.index'))
        else: 
            #form not submitted
            return render_template('create_post.html', title='Add New Listing', form=form)
    else:
        return redirect(url_for('main.index'))


@posts.route('/post/<int:post_id>/new_review', methods=['GET', 'POST'])
@login_required
def new_review(post_id):
    form = NewReviewForm()
    if form.validate_on_submit():
        review = Review(stars=form.stars.data,  comment=form.comment.data)
        review.user_id = current_user.id
        review.post_id = post_id
        db.session.add(review)
        db.session.commit()
        flash('Review Added!', 'success')
        return redirect(url_for('posts.listing', post_id=post_id))
    return render_template('create_review.html', title='Add review', form=form)


@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
def listing(post_id):
    wish = False
    listing = Post.query.get_or_404(post_id)

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], listing.title)
    files_list = os.listdir(file_path)
    reviews = listing.reviews

    if current_user.is_authenticated:
        if current_user.checker == 'refugee':
            user = Refugee.query.filter_by(username=current_user.username).first()
            wishes = user.wish_list.split(",")
            if str(post_id) in wishes:
                wish = True
            return render_template('listing.html', title=listing.title, post=listing, wish=wish, user_type=0, files_list=files_list, reviews=reviews)
        elif current_user.checker == 'landlord':
            return render_template('listing.html', title=listing.title, post=listing, user_type=1, files_list=files_list, reviews=reviews)
    else:
        return render_template('listing.html', title=listing.title, post=listing, user_type=-1, files_list=files_list, reviews=reviews)



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
        listing.address = form.address.data
        listing.city=form.city.data
        listing.pet=form.pet.data
        listing.smoking=form.smoking.data
        listing.balcony=form.balcony.data
        listing.air_conditioning=form.air_conditioning.data
        listing.stove_oven=form.stove_oven.data
        listing.washer=form.washer.data
        listing.dryer=form.dryer.data
        listing.dishwasher=form.dishwasher.data
        listing.microwave=form.microwave.data
        listing.cable=form.cable.data
        listing.water=form.water.data
        listing.electricity=form.electricity.data
        listing.num_bathrooms=form.num_bathrooms.data
        listing.num_bedrooms=form.num_bedrooms.data
        listing.type_of_building=form.type_of_building.data
        listing.author=current_user
        uploaded_file = request.files.getlist("file[]")
        for im in uploaded_file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], form.title.data + '/' + "{}.{}".format(time.time(), im.filename[-3:]))
            if allowed_file(im.filename):
                im.save(file_path)
        db.session.commit()
        flash('Post updated', 'success')
        return redirect(url_for('posts.listing', post_id=listing.id))
    elif request.method == 'GET':
        form.title.data = listing.title
        form.content.data = listing.content
        form.address.data = listing.address
        form.city.data = listing.city
        form.pet.data = listing.pet
        form.smoking.data = listing.smoking
        form.balcony.data = listing.balcony
        form.air_conditioning.data = listing.air_conditioning
        form.stove_oven.data = listing.stove_oven
        form.washer.data = listing.washer
        form.dryer.data = listing.dryer
        form.dishwasher.data = listing.dishwasher
        form.microwave.data = listing.microwave
        form.cable.data = listing.cable
        form.water.data = listing.water
        form.electricity.data = listing.electricity
        form.num_bathrooms.data = listing.num_bathrooms
        form.num_bedrooms.data = listing.num_bedrooms
        form.type_of_building.data = listing.type_of_building


    return render_template('create_post.html', title='Update Post', form=form)


@posts.route('/post/<int:post_id>/<int:review_id>/delete_review', methods=['GET', 'POST'])
@login_required
def delete_review(post_id, review_id):
    review = Review.query.get_or_404(review_id)
    if review.user != current_user:
        abort(403)
    db.session.delete(review)
    db.session.commit()
    flash('Your review has been deleted!', 'success')
    return redirect(url_for('posts.listing', post_id=post_id))


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    shutil.rmtree(os.path.join(app.config['UPLOAD_FOLDER'], post.title))
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
    return redirect(url_for('posts.listing', post_id=post_id))


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
    return redirect(url_for('posts.listing', post_id=post_id))


@posts.route("/post/search", methods=['GET', 'POST'])
def search():
    form = NewSearchForm()
    form.address.choices = [("-1", "N/A")] + sorted(list(set([(p.address, p.address) for p in Post.query.order_by(Post.address)])))
    form.city.choices = [("-1", "N/A")] + sorted(list(set([(p.city, p.city) for p in Post.query.order_by(Post.city)])))
    form.type_of_building.choices = [("-1", "N/A")] + sorted(list(set([(p.type_of_building, p.type_of_building) for p in Post.query.order_by(Post.type_of_building)])))
    form.num_bedrooms.choices = [("-1", "N/A")] + sorted(list(set([(str(p.num_bedrooms), str(p.num_bedrooms)) for p in Post.query.order_by(Post.num_bedrooms)])))
    form.num_bathrooms.choices = [("-1", "N/A")] + sorted(list(set([(str(p.num_bathrooms), str(p.num_bathrooms)) for p in Post.query.order_by(Post.num_bathrooms)])))
    if form.validate_on_submit():

        if form.address.data != "-1" and form.city.data != "-1":
            posts = Post.query.filter_by(address=form.address.data, city=form.city.data).all()
        elif form.address.data != "-1":
            posts = Post.query.filter_by(address=form.address.data).all()
        elif form.city.data != "-1":
            posts = Post.query.filter_by(city=form.city.data).all()
        else:
            posts = Post.query.filter_by().all()

        if form.num_bedrooms.data != "-1":
            posts = [post for post in posts if str(post.num_bedrooms) == form.num_bedrooms.data]

        if form.num_bathrooms.data != "-1":
            posts = [post for post in posts if str(post.num_bathrooms) == form.num_bathrooms.data]

        if form.type_of_building.data != "-1":
            posts = [post for post in posts if post.type_of_building == form.type_of_building.data]

        if form.pet.data:
            posts = [post for post in posts if post.pet]

        if form.smoking.data:
            posts = [post for post in posts if post.smoking]

        if form.balcony.data:
            posts = [post for post in posts if post.balcony]

        if form.air_conditioning.data:
            posts = [post for post in posts if post.air_conditioning]

        if form.stove_oven.data:
            posts = [post for post in posts if post.stove_oven]

        if form.washer.data:
            posts = [post for post in posts if post.washer]

        if form.dryer.data:
            posts = [post for post in posts if post.dryer]

        if form.dishwasher.data:
            posts = [post for post in posts if post.dishwasher]

        if form.microwave.data:
            posts = [post for post in posts if post.microwave]

        if form.cable.data:
            posts = [post for post in posts if post.cable]

        if form.water.data:
            posts = [post for post in posts if post.water]

        if form.electricity.data:
            posts = [post for post in posts if post.electricity]

        return render_template('search.html', form=form, posts=posts)
    return render_template('search.html', form=form)


