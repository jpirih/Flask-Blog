# -*- coding: utf-8 -*-
from flask import request, render_template, redirect, url_for, flash, Blueprint
from project import db
from flask.ext.login import login_required, current_user
from project.models import BlogPost, Comment
from forms import CreatePostForm, CommentForm
from project.helpers import date_time_standard

blog_blueprint = Blueprint(
    'blog', __name__,
    template_folder='templates'
)


@blog_blueprint.route('/blog')
@login_required
def blog_home():
    posts = db.session.query(BlogPost).order_by('id desc').all()
    return render_template('blog_home.html', posts=posts)



@blog_blueprint.route('/blog-post/<post_id>')
@login_required
def blog_details(post_id):
    form = CommentForm()
    post = BlogPost.query.filter_by(id=post_id).first()
    objavljeno  = date_time_standard(post.created_at)
    comments = db.session.query(Comment).filter_by(post_id=post_id).all()
    return render_template('post_details.html', post=post, form=form, comments=comments, objavljeno=objavljeno)


@blog_blueprint.route('/blog-post/<post_id>/create-comment', methods=['POST'])
@login_required
def create_commment(post_id):
    post = BlogPost.query.filter_by(id=post_id).first()
    form = CommentForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        comment = Comment(
            post_id=post_id,
            user_id=current_user.id,
            title=title,
            content=content
        )
        db.session.add(comment)
        db.session.commit()
        flash('Komentar shranjen OK')
        return redirect(url_for('blog.blog_details',post_id=post_id))



@blog_blueprint.route('/blog/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = CreatePostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            post = BlogPost(
                title=title,
                description=description,
                author=current_user.id
            )

            db.session.add(post)
            db.session.commit()
            flash('Objava je bila shranjena')
            return redirect(url_for('blog.blog_home'))

    return render_template('create_post.html', form=form)
