from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)

app.secret_key = "my_portfolio_secret_key"

users = {
    "shrashti": {
        "password": "@mishra",
        "page": "shrashti.html"
    },

    "yashika": {
        "password": "@sharma",
        "page": "yashika.html"
    }
}

@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("portfolio"))

    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username", "").strip().lower()
    password = request.form.get("password", "")

    if username in users and password == users[username]["password"]:

        session["username"] = username

        print("LOGIN SUCCESSFUL:", username)

        return redirect(url_for("portfolio"))

    print("LOGIN FAILED:", username)

    return render_template(
        "login.html",
        error="Invalid username or password!"
    )

@app.route("/portfolio")
def portfolio():

    if "username" not in session:
        return redirect(url_for("home"))

    username = session["username"]

    page = users[username]["page"]

    return render_template(page)

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

