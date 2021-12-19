from flask import Blueprint, render_template, request
from flask_login import login_required

from blog.models import Post, User

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def home():
    return render_template('main/index.html', title='Главная')


@main.route('/blog', methods=['POST', 'GET'])
@login_required
def blog():
    all_posts = Post.query.order_by(Post.title.desc()).all()
    all_users = User.query.all()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)

    return render_template('main/blog.html', title='Блог', posts=posts,
                           all_posts=all_posts, all_users=all_users)


@main.route('/html_page')
def html_page():
    return render_template('main/html_page.html')


@main.route('/css_page')
def css_page():
    return render_template('main/css_page.html')


@main.route('/js_page')
def js_page():
    return render_template('main/js_page.html')


@main.route('/python_page')
def python_page():
    return render_template('main/python_page.html')


@main.route('/flask_page')
def flask_page():
    return render_template('main/flask_page.html')


@main.route('/django_page')
def django_page():
    return render_template('main/django_page.html')
