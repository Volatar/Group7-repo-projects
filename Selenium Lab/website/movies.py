from flask import Blueprint, render_template, request, session, redirect, url_for

movie = Blueprint('movie', __name__)

movies = {
    'A': 'Alien vs Ogre',
    'B': 'Back to the Present',
    'C': 'Casino Royale with Cheese',
    'D': 'The Dark Night',
    'E': 'Elven',
    'F': 'Fobemat',
    'G': 'Gladiator: Mall Cop',
    'H': 'Home Alone with The Grinch',
    'I': 'Iron Boy',
    'J': 'Jurassic Shark',
    'K': 'The Karate Baby',
    'L': 'The Lord of the Rings: Ring Nation',
    'M': 'The Matrix: Reducked',
    'N': 'Night at the Supermarket',
    'O': 'Owltopia',
    'P': 'Planet of the Lizards',
    'Q': 'Queen of the Legos',
    'R': 'Raiders of the Lost Park',
    'S': 'Star Trek: Wrath of Picard',
    'T': 'T for Timeloop',
    'U': 'Up Again',
    'V': 'V for Venom',
    'W': 'Website Story',
    'X': 'Xtreme Wormhole Adventure',
    'Y': "You've Got Junk Mail",
    'Z': 'Zoolando'
}


@movie.route("/search", methods=["GET", "POST"])
def movie_search():
    result = ""
    if request.method == "POST":
        user_input = request.form.get("user_input")
        user_input = user_input.upper()

        if user_input == "QUIT":
            result = "You have quit the search."
        elif user_input in movies:
            result = movies[user_input]
        else:
            result = 'No movies found for the letter "{}".'.format(user_input)

    return render_template("search.html", result=result)

@movie.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    movie_found = request.form.get("movie")
    movie_key = movie_found[0]
    if 'cart' not in session:
        session['cart'] = []

    if movie_key in movies:
        edit_cart = session['cart']
        edit_cart.append(movie_found)
        session['cart'] = edit_cart

    return redirect(url_for('movie.movie_search'))

@movie.route("/get_cart", methods=['GET', 'POST'])
def view_cart():
    return render_template("cart.html", cart=session['cart'])


@movie.route("/delete_item", methods=['POST'])
def remove_item():
    edit_cart = session['cart']
    edit_cart.remove(request.form.get("movie"))
    session['cart'] = edit_cart
    return render_template("cart.html", cart=session['cart'])


@movie.route("/empty_cart", methods=['POST'])
def empty_cart():
    session['cart'] = []
    return render_template("cart.html", cart=session['cart'])
