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
    return "<p>Cart</p>"

@views.route('/payment')
def payment():
    return "<p>Payment</p>"

@views.route('/about')
def about():
    return "<p>About</p>"

@views.route('/contact')
def contact():
    return "<p>Contact</p>"
