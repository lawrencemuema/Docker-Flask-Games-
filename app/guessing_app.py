from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.form['guess'])
    if user_guess < random_number:
        message = "Too low! Try again."
    elif user_guess > random_number:
        message = "Too high! Try again."
    else:
        message = f"Congratulations! You guessed the number {random_number}!"
    
    return render_template('index.html', message=message)

@app.route('/reset', methods=['POST'])
def reset():
    global random_number
    random_number = random.randint(1, 100)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True
    ,host = '0.0.0.0',
    port=5000
    )
