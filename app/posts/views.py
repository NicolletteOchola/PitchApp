from flask import (render_template, url_for, flash,redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from app import db
from app.models import Post, User, Comment
from app.posts.forms import PostForm, CommentForm

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user, category=form.category.data)
        db.session.add(post)
        db.session.commit()
        flash('You pitch has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('new-post.html', title='New Pitch', form=form, legend='New Pitch')
