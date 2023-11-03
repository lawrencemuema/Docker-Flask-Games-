from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# List of words for the game
#fruits
words = ["apple", "banana", "orange", "pear", "grape", "pineapple", "strawberry", "blueberry", "mango", "watermelon"]

#animals
# words = ["dog", "cat", "bird", "fish", "rabbit", "hamster", "turtle", "snake", "lizard", "frog"]

#countries
# words = ["germany", "france", "spain", "italy", "poland", "austria", "switzerland", "belgium", "netherlands", "denmark"]

#colors
# words = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "white"]

#sports
# words = ["soccer", "basketball", "football", "baseball", "tennis", "volleyball", "hockey", "golf", "rugby", "cricket"]

#cars
# words = ["toyota", "honda", "ford", "chevrolet", "nissan", "hyundai", "kia", "bmw", "mercedes", "audi"]

#movies
# words = ["titanic", "avatar", "star wars", "jurassic park", "the avengers", "the dark knight", "inception", "the matrix", "forrest gump", "the lion king"]



# Initialize game variables
word = ""
attempts = 6
guessed_letters = set()

def choose_word():
    return random.choice(words)

def initialize_game():
    global word, guessed_letters, attempts
    word = choose_word()
    guessed_letters = set()
    attempts = 6

@app.route("/")
def index():
    initialize_game()
    return render_template("index.html", display_word=" ".join("_" for _ in word), attempts=attempts)

@app.route("/make_guess", methods=["POST"])
def make_guess():
    global guessed_letters, attempts
    guess = request.form.get("guess", "").lower()

    if not guess.isalpha() or len(guess) != 1:
        return jsonify({"message": "Invalid guess. Please enter a single letter."})

    if guess in guessed_letters:
        return jsonify({"message": "You already guessed that letter."})

    guessed_letters.add(guess)

    if guess not in word:
        attempts -= 1

    display_word = [letter if letter in guessed_letters else "_" for letter in word]

    if "_" not in display_word:
        return jsonify({"message": "You win!"})

    if attempts == 0:
        return jsonify({"message": f"You lose! The word was '{word}'."})

    return jsonify({"display_word": " ".join(display_word), "attempts": attempts})


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=8080)
