from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    blog_url = "https://api.npoint.io/af73fa63821d3fd09fac"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("html.html", posts=all_posts)

@app.route("/post/<int:post_id>")
def get_post(post_id):
    blog_url = "https://api.npoint.io/af73fa63821d3fd09fac"
    response = requests.get(blog_url)
    all_posts = response.json()
    post = next(p for p in all_posts if p["id"] == post_id)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
