from flask import Flask, render_template, request

app = Flask(__name__)

movies = {
    "A": "Avatar",
    "B": "Blade Runner",
    "C": "Casablanca",
    "D": "Die Hard",
    "E": "E.T. the Extra-Terrestrial",
    "F": "Forrest Gump",
    "G": "Gladiator",
    "H": "Home Alone",
    "I": "Inception",
    "J": "Jurassic Park",
    "K": "The Karate Kid",
    "L": "The Lord of the Rings",
    "M": "The Matrix",
    "N": "National Treasure",
    "O": "Office Space",
    "P": "Pulp Fiction",
    "Q": "The Queen",
    "R": "Raiders of the Lost Ark",
    "S": "Star Wars",
    "T": "Titanic",
    "U": "Up",
    "V": "V for Vendetta",
    "W": "The Wizard of Oz",
    "X": "X-Men",
    "Y": "You Again",
    "Z": "Zootopia",
}


@app.route("/", methods=["GET", "POST"])
def movie_search():
    result = ""

    if request.method == "POST":
        user_input = request.form["user_input"]
        user_input = user_input.upper()

        if user_input == "QUIT":
            result = "You have quit the search."
        elif user_input in movies:
            result = ", ".join(movies[user_input])
        else:
            result = 'No movies found for the letter "{}".'.format(user_input)

    return render_template("search.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
