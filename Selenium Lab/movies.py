from flask import Flask, render_template, request

app = Flask(__name__)

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
    'W': 'The Wizard of Oz 2: Tornado Alley',
    'X': 'Xtreme Wormhole Adventure',
    'Y': "You've Got Junk Mail",
    'Z': 'Zootedtopia'
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
