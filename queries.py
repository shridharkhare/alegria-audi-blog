from initdb import db
from flask import redirect, url_for


def get_blogs():
    try:
        if db.get():
            blogs = db.get()

            blogs = [
                {
                    "title": blog.get("title", "Untitled"),
                    "description": blog.get("description", "No description available"),
                    "blog": blog.get("blog", "No content available"),
                    "author": blog.get("author", "Anonymous"),
                }
                for blog in blogs.values()
            ]

        else:
            blogs = []
        return blogs
    except Exception as e:
        return str(e)


def generate_id():
    try:
        if db.get():
            posts = db.get()
            return len(posts) + 1
        else:
            return 1
    except Exception as e:
        return str(e)


def post_blog(post):
    try:
        title = post.get("title")
        description = post.get("description")
        blog = post.get("blog")
        author = post.get("author")
        id = generate_id()

        new_post = {
            "id": id,
            "title": title,
            "description": description,
            "blog": blog,
            "author": author,
        }

        db.push(new_post)

        return "Post created successfully"
    except Exception as e:
        return str(e)


def get_blog_by_id_(blog_id):
    try:
        blogs_data = db.get()
        if blogs_data:
            for key, value in blogs_data.items():
                if value["id"] == blog_id:
                    value["key"] = key
                    # print(value)
                    return value
        return None

    except Exception as e:
        return str(e)


def delete_blog(blog_id):
    try:
        print("received blog id", blog_id)
        blog = get_blog_by_id_(blog_id)

        if not blog:
            return "Blog not found", 404

        db.child(blog["key"]).delete()
        return redirect(url_for("blogs"))

    except Exception as e:
        return str(e)
