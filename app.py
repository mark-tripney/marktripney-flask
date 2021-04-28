from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html", title="Home")


@app.route("/work")
def work():
    return render_template("work.html", title="Work")


@app.route("/writing")
def writing():
    return render_template("writing.html", title="Writing")


@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")
