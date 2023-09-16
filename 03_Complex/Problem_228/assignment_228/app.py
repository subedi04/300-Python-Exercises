'''
Write A Python Program to Generate a Strong Password, 
Length should be provided from user on Web.
'''
from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_strong_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            password_length = int(request.form["length"])
            if password_length < 8:
                return "Password length must be at least 8 characters."
            strong_password = generate_strong_password(password_length)
            return f"Generated Strong Password: {strong_password}"
        except ValueError:
            return "Invalid input. Please enter a valid number for password length."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
