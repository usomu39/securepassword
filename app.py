from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    password = None
    error = None

    if request.method == "POST":
        try:
            length = int(request.form.get("length", 0))
        except ValueError:
            error = "Please enter a valid length."
            return render_template("index.html", password=password, error=error)

        include_digits = request.form.get("digits") == "on"
        include_special = request.form.get("special") == "on"
        include_uppercase = request.form.get("uppercase") == "on"

        # Default always lowercase letters
        characters = string.ascii_lowercase

        if include_digits:
            characters += string.digits
        if include_special:
            characters += string.punctuation
        if include_uppercase:
            characters += string.ascii_uppercase

        if not characters:
            error = "You must select at least one character set."
        elif length <= 0:
            error = "Length must be greater than 0."
        else:
            password = ''.join(secrets.choice(characters) for _ in range(length))

    return render_template("index.html", password=password, error=error)

if __name__ == '__main__':
    app.run(debug=True)
