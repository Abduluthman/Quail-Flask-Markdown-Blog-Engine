import os
import yaml
import math
from flask import Flask, render_template, abort, request
from markdown import markdown
from pathlib import Path
from datetime import datetime

app = Flask(__name__)
POSTS_DIR = Path("posts")

def parse_post_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()

    if raw.startswith("---"):
        parts = raw.split('---', 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1])
            content = parts[2]
        else:
            meta = {}
            content = raw
    else:
        meta = {}
        content = raw

    # Convert markdown to HTML
    html_content = markdown(content, extensions=["fenced_code", "codehilite"])

    # Estimate reading time
    word_count = len(content.split())
    reading_time = math.ceil(word_count / 200)
    meta.setdefault("reading_time", f"{reading_time} min read")

    # Format date
    if "date" in meta:
        try:
            if isinstance(meta["date"], datetime):
                date_obj = meta["date"]
            elif hasattr(meta["date"], "strftime"):
                date_obj = datetime.combine(meta["date"], datetime.min.time())
            elif isinstance(meta["date"], str):
                date_obj = datetime.strptime(meta["date"], "%Y-%m-%d")
            else:
                raise ValueError("Unsupported date format.")
            meta["formatted_date"] = date_obj.strftime("%B %d, %Y")
        except Exception:
            meta["formatted_date"] = str(meta["date"])
    else:
        meta["formatted_date"] = "Unknown"

    return meta, html_content

def load_post(post_name):
    filepath = POSTS_DIR / f"{post_name}.md"
    if not filepath.exists():
        abort(404)
    return parse_post_file(filepath)

def load_posts():
    posts = []
    for post_file in POSTS_DIR.glob("*.md"):
        post_name = post_file.stem
        meta, content_html = parse_post_file(post_file)
        post = {
            "name": post_name,
            "title": meta.get("title", post_name.replace('-', ' ').title()),
            "tags": meta.get("tags", []),
            "category": meta.get("category", None),
            "formatted_date": meta.get("formatted_date", "Unknown"),
            "reading_time": meta.get("reading_time", "1 min read"),
            "content": content_html,
            "featured": str(meta.get("featured", False)).lower() == "true"
        }
        posts.append(post)

    # Sort by date descending if possible
    def sort_key(post):
        try:
            return datetime.strptime(post["formatted_date"], "%B %d, %Y")
        except:
            return datetime.min

    posts.sort(key=sort_key, reverse=True)
    return posts

@app.route("/")
def index():
    posts = load_posts()
    featured_posts = [p for p in posts if p["featured"]]
    return render_template("index.html", posts=posts, featured_posts=featured_posts)

@app.route("/post/<post_name>")
def post(post_name):
    meta, content = load_post(post_name)
    all_posts = load_posts()

    related_posts = []
    for p in all_posts:
        if p["name"] == post_name:
            continue

        shared_tags = set(p.get("tags", [])) & set(meta.get("tags", []))
        same_category = p.get("category") == meta.get("category")

        if shared_tags or same_category:
            related_posts.append({
                "name": p["name"],
                "title": p["title"],
                "formatted_date": p["formatted_date"],
                "reading_time": p["reading_time"],
                "tags": p["tags"],
                "category": p["category"],
                "score": len(shared_tags) + (1 if same_category else 0),
            })

    # Sort by most similar (shared tags + category match)
    related_posts = sorted(related_posts, key=lambda x: x["score"], reverse=True)[:4]

    return render_template(
        "post.html",
        content=content,
        meta=meta,
        title=meta.get("title", post_name),
        tags=meta.get("tags", []),
        related_posts=related_posts,
    )

@app.route("/search")
def search():
    query = request.args.get("q", "").lower().strip()
    if not query:
        return render_template("search.html", query=query, results=[])

    posts = load_posts()
    results = [
        post for post in posts
        if query in post["title"].lower() or query in post["content"].lower()
    ]
    return render_template("search.html", query=query, results=results)

@app.route("/tags")
def all_tags():
    posts = load_posts()
    tag_map = {}
    for post in posts:
        for tag in post["tags"]:
            tag_map.setdefault(tag, []).append(post)
    return render_template("tags.html", tag_map=tag_map)

@app.route("/tag/<tag>")
def tag(tag):
    posts = [p for p in load_posts() if tag in p["tags"]]
    return render_template("tag.html", tag=tag, posts=posts)

@app.route("/categories")
def all_categories():
    posts = load_posts()
    cat_map = {}
    for post in posts:
        cat = post["category"]
        if cat:
            cat_map.setdefault(cat, []).append(post)
    return render_template("categories.html", cat_map=cat_map)

@app.route("/category/<category>")
def category(category):
    posts = [p for p in load_posts() if p["category"] and p["category"].lower() == category.lower()]
    return render_template("category.html", category=category, posts=posts)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
