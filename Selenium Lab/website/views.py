from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/search')
def search():
    return render_template("search.html")


@views.route('/cart')
def cart():
    return render_template("cart.html")


@views.route('/about')
def about():
    return render_template("about.html")


@views.route('/contact')
def contact():
    return "<p>Contact</p>"
