from flask import Flask
from markupsafe import escape
from flask import request
from flask import url_for

app = Flask(__name__)

# intermédiaires
@app.route("/")
def index():
    return "index"

@app.route("/login")
def login():
    return "login"

@app.route("/user/<string:username>")
def profile(username):
    return f"{username}\'s profile"

with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next="/"))
    print(url_for("profile", username="John Doe"))

# bases
# @app.route("/")
# def index():
#     return 'Index Page'
#
# @app.route("/hello")
# def hello():
#     name = request.args.get("name", "World")
#     return f"Hello {escape(name)} !"
#
# @app.route("/user/<username>")
# def show_user_profile(username):
#     # show the user profile
#     return f"User {escape(username)}"
#
# @app.route("/post/<int:post_id>")
# def show_post(post_id):
#     return f"Post {escape(post_id)}"
#
# @app.route("/path/<path:subpath>")
# def show_subpath(subpath):
#     return f"Subpath {escape(subpath)}"
#
# @app.route("/projects/")
# def projects():
#     return "The project page"
#
# @app.route("/about")
# def about():
#     return "The about page"