from flask import Flask, render_template
from post import Post
import requests


app = Flask(__name__)


def _generate_posts():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    posts = []
    for post in data:
        posts.append(Post(post["id"], post["title"],
                     post["subtitle"], post["body"]))
    return posts


posts = _generate_posts()


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
