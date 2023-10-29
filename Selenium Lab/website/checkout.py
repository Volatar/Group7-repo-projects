from flask import Blueprint, render_template, request, session, redirect, url_for, flash
# from movies import movies

checkout = Blueprint('checkout', __name__)

# TODO: popup asking user if ok
# TODO: clear cart and go to home if ok, do not leave page otherwise


@checkout.route("/payment", methods=['GET', 'POST'])
def get_checkout():
    if 'cart' not in session:
        session['cart'] = []
    payment_cart = session['cart']
    videos = len(payment_cart)
    total = videos * 3.0

    return render_template("payment.html", cart=session['cart'], num_videos=videos, total_cost=total)


@checkout.route("/finish_pay", methods=['GET', 'POST'])
def ask_purchase():
    # TODO: Implement confirmation dialog
    session['cart'] = []
    return render_template("home.html")
