movies_dict = {
    'A': 'Avatar',
    'B': 'Blade Runner',
    'C': 'Casablanca',
    'D': 'Die Hard',
    'E': 'E.T. the Extra-Terrestrial',
    'F': 'Forrest Gump',
    'G': 'Gladiator',
    'H': 'Home Alone',
    'I': 'Inception',
    'J': 'Jurassic Park',
    'K': 'The Karate Kid',
    'L': 'The Lord of the Rings',
    'M': 'The Matrix',
    'N': 'National Treasure',
    'O': 'Office Space',
    'P': 'Pulp Fiction',
    'Q': 'The Queen',
    'R': 'Raiders of the Lost Ark',
    'S': 'Star Wars',
    'T': 'Titanic',
    'U': 'Up',
    'V': 'V for Vendetta',
    'W': 'The Wizard of Oz',
    'X': 'X-Men',
    'Y': 'You Again',
    'Z': 'Zootopia'
}

def search_movie():
    while True:
        user_input = input("Enter the first letter of the movie title (A-Z) to see what's available for rental, or 'quit' to exit: ").upper()
        
        if user_input == 'QUIT':
            print("Exiting the program.")
            break
        
        movie_title = movies_dict.get(user_input, 'Movie not found')
        print(f"Movie title starting with '{user_input}': {movie_title}")

# Main program
if __name__ == "__main__":
    search_movie()