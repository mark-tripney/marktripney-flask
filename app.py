from markdown import markdown
from flask import Flask, render_template, render_template_string, url_for
from flask_flatpages import FlatPages


def my_markdown(text):
    markdown_text = render_template_string(text)
    formatted_text = markdown(
        markdown_text, extensions=["fenced_code"]
    )
    return formatted_text


FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = ".md"

app = Flask(__name__)
app.config.from_object(__name__)
app.config["FLATPAGES_HTML_RENDERER"] = my_markdown
pages = FlatPages(app)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html", title="Home")


@app.route("/writing/<path:path>.html")
def page(path):
    print("Page function running")
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)


@app.route("/work")
def work():
    return render_template("work.html", title="Work")


@app.route("/writing")
def writing():
    return render_template("writing.html", title="Writing")


@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")
