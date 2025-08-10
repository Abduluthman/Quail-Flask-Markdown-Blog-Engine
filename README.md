# 📝 Flask Markdown Blog Engine

A lightweight and flexible **Markdown-based blog engine** built with Flask.  
Write posts in `.md` files, store them in a `posts/` folder, and serve them as fully styled HTML pages with tags, categories, search, related posts, featured articles, and more.

---

## 🚀 Features

- **Markdown Posts** → Write your blog posts in `.md` files with optional YAML front matter
- **Automatic Metadata Parsing**:
  - Title
  - Tags
  - Category
  - Cover image
  - Featured status
  - Published date
  - Estimated reading time
- **Search** → Full-text search on titles and content
- **Tags & Categories** → Browse by tag or category
- **Related Posts** → Suggestions based on shared tags & category
- **Featured Articles** → Highlighted posts on the homepage
- **Dark Mode Toggle** → Persistent theme preference
- **Responsive Design** → Mobile-friendly layout
- **Image & Code Block Styling** → With optional lightbox for images
- **RSS Feed** → Let people subscribe to your blog updates
- **Ready for Newsletter Automation** → Integrate with Mailchimp, ConvertKit, or Zapier
- **Syntax Highlighting** → For code blocks in posts

---

## 📂 Project Structure
```bash
project/
├── app.py # Flask app entry point
├── posts/ # Markdown blog posts
│ ├── my-first-blog.md
│ ├── why-use-a-static-blog.md
│ └── ...
├── templates/ # Jinja2 HTML templates
│ ├── base.html
│ ├── index.html
│ ├── post.html
│ ├── search.html
│ ├── tag.html
│ ├── category.html
│ ├── tags.html
│ └── categories.html
├── static/
│ │── style.css
│ ├── script.js
├── requirements.txt
└── README.md
```

---

## 🛠 Installation

### 1️. Clone the Repository

```bash
git clone https://github.com/yourusername/flask-markdown-blog.git
cd flask-markdown-blog
```
### 2️. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the App
```bash
python app.py
```

---

## ✍️ Writing Posts
Create a new .md file in the posts/ folder:
```bash
---
title: My First Blog Post
tags: [python, flask]
category: Web Development
date: 2025-08-10
cover_image: my-cover.jpg
featured: true
---

## Welcome!

This is my **first post** in Markdown.
```
YAML Front Matter (the --- block at the top) is optional but recommended.

The body supports all standard Markdown features, including headings, lists, images, and fenced code blocks.

--- 

## 🔍 Searching
Search bar on the homepage searches both titles and post content.

Matches are highlighted automatically.

---

## 📅 Metadata
- Estimated Reading Time → Automatically calculated (200 words per minute)
- Published Date → From date in YAML front matter or defaults to "Unknown"
- Category & Tags → Clickable badges for navigation

---

## 🌙 Dark Mode
- Click the moon/sun icon in the navbar to toggle between light and dark themes.
- Your choice is saved in localStorage.

---

## 🔗 Related Posts
At the bottom of each post, up to 4 related posts are shown:
- Shared tags
- Same category
- Sorted by relevance

---

## 📜 License
MIT License — Feel free to use, modify, and share.

---

## 💡 Future Improvements
- Comment system (Disqus, Giscus, or custom)
- Pagination for large blogs
- Author profiles
- Post series support
- Advanced image gallery

