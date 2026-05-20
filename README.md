# Flask-Blog
# 📝 Flask Blog

A clean, minimal personal blog built with **Flask** and **Jinja2 templates**, styled with a dark editorial aesthetic. Posts are fetched from a remote JSON API and rendered server-side.
---
## ✨ Features

- Dynamic post listing fetched from a live API endpoint
- Individual post pages with full title, subtitle, and body
- Responsive dark-themed UI with custom CSS (no frameworks)
- Jinja2 templating with shared layout structure
- Clean URL routing (`/` for index, `/post/<id>` for individual posts)

---

## 🗂️ Project Structure

```
flask-blog/
├── main.py                  # Flask app & routes
├── static/
│   └── style.css            # All styling (dark theme, typography, layout)
└── templates/
    ├── html.html            # Blog index (post card list)
    └── post.html            # Single post view
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/flask-blog.git
cd flask-blog

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install flask requests
```

### Running the App

```bash
python main.py
```

Then open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🛣️ Routes

| Route | Description |
|-------|-------------|
| `/` | Home page — lists all blog posts |
| `/post/<int:post_id>` | Full view of a single post |

---

## 🎨 Design

- **Color scheme:** Dark background (`#0d1117`) with amber accent (`#f0a500`)
- **Typography:** Playfair Display (headings) + DM Sans (body)
- **Layout:** Centered single-column, max 720px wide

---

## 📡 Data Source

Posts are fetched from a public JSON endpoint via the `requests` library:

```
https://api.npoint.io/af73fa63821d3fd09fac
```

Each post object is expected to contain: `id`, `title`, `subtitle`, `body`.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Made with ❤️ in London.
