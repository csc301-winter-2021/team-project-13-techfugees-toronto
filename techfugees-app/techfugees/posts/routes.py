from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from techfugees import db
from techfugees.models import Post, User
from techfugees.posts.forms import NewListingForm


posts = Blueprint('posts', __name__)

@posts.route('/post/new', methods=['GET','POST'])
@login_required
def new_rental_posting():
    form = NewListingForm()
    if form.validate_on_submit():
        listing = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(listing)
        db.session.commit()
        flash('Listing Added!', 'success')
        return redirect(url_for('main.index'))
    return render_template('create_post.html', title='Add New Listing', form=form)

@posts.route('/post/<int:post_id>', methods=['GET','POST'])
def listing(post_id):
    listing = Post.query.get_or_404(post_id)
    return render_template('listing.html', title=listing.title, post=listing)

@posts.route('/post/<int:post_id>/update', methods=['GET','POST'])
@login_required
def update_listing(post_id):
    listing = Post.query.get_or_404(post_id)
    if listing.author != current_user:
        abort(403)
    form = NewListingForm()
    if form.validate_on_submit():
        listing.title = form.title.data #SQLalchemy convention, post refers to Post class, and is lowercase here
        listing.content =form.content.data
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