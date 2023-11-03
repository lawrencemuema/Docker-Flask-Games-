from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Initialize the game board
board = [""] * 9
player_symbol = "X"
computer_symbol = "O"

def check_winner(board, symbol):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if all(board[i] == symbol for i in combo):
            return True
    return False

def check_tie(board):
    return "" not in board


@app.route("/")
def index():
    return render_template("index.html", board=board, message="")


@app.route("/make_move", methods=["POST"])
def make_move():
    position = int(request.form["position"])
    if board[position] == "":
        board[position] = player_symbol
        if check_winner(board, player_symbol):
            return jsonify({"board": board, "message": "You win!"})
        elif check_tie(board):
            return jsonify({"board": board, "message": "It's a tie!"})
        else:
            computer_move = random.choice([i for i, val in enumerate(board) if val == ""])
            # computer_move = random.randint(0, 8)
            
            board[computer_move] = computer_symbol
            if check_winner(board, computer_symbol):
                return jsonify({"board": board, "message": "Computer wins!"})
            elif check_tie(board):
                return jsonify({"board": board, "message": "It's a tie!"})
    return jsonify({"board": board, "message": ""})

@app.route("/reset", methods=["POST"])
def reset():
    global board
    board = [""] * 9
    return jsonify({"board": board, "message": ""})

if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=1000)
