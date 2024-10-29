from flask import Flask, render_template, request, redirect, url_for
from queries import get_blogs, post_blog, get_blog_by_id_, delete_blog

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/blogs", methods=["POST", "GET"])
def blogs():
    if request.method == "GET":
        blogs = get_blogs()
        return render_template("blogs.html", blogs=blogs)
    else:
        form = request.form
        blog = post_blog(form)
        return redirect(url_for("blogs"))


@app.route("/blogs/create", methods=["GET"])
def create_blog():
    return render_template("create_blog.html")


@app.route("/blogs/get", methods=["POST"])
def get_blog_by_id():
    blog_id = request.form.get("blog_id")

    if blog_id and blog_id.isdigit():
        return redirect(url_for("view_blog", blog_id=int(blog_id)))
    else:
        return "Invalid Blog ID", 400


@app.route("/blogs/<int:blog_id>", methods=["GET", "POST"])
def view_blog(blog_id):

    if request.method == "GET":
        blog = get_blog_by_id_(blog_id)
        return render_template("view_blog.html", blog=blog)
    else:
        response = delete_blog(blog_id)
        print(response)
        if "success" in response:
            print("Blog deleted successfully")


if __name__ == "__main__":
    app.run()
