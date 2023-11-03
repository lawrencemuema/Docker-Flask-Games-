from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Initialize game variables
choices = ["rock", "paper", "scissors"]
player_choice = ""
computer_choice = ""
result = ""

def initialize_game():
    global player_choice, computer_choice, result
    player_choice = ""
    computer_choice = ""
    result = ""
@app.route("/")
def index():
    initialize_game()
    return render_template("index.html", result=result, player_choice=player_choice, computer_choice=computer_choice)

@app.route("/play", methods=["POST"])
def play():
    global player_choice, computer_choice, result
    player_choice = request.form["choice"]
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    return render_template("index.html", result=result, player_choice=player_choice, computer_choice=computer_choice)


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=8080)
