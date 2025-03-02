from flask import render_template, request, Blueprint
from capstone_depot.models import Post
from capstone_depot.posts.forms import CATEGORIES

main = Blueprint('main', __name__)

@main.route("/") # handles all the server actions and provides endpoint
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.year.desc(), Post.id.desc()).paginate(page=page, per_page=10)
    return render_template('home.html', posts=posts, categories=CATEGORIES[1:])


@main.route("/about")
def about():
    return render_template('about.html', title='About')
