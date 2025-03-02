from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"  # Change to a more secure secret key in production

# Dummy database
users = {"lakshmi": "password123"}  # Replace with proper database storage

@app.route("/")
def home():
    if "user" in session:
        return render_template("home.html", user=session["user"])
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password:
            users[username] = password  # Storing in dummy dict (use a DB in real app)
            return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("home"))
        return render_template("login.html", error="Invalid credentials. Try again!")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("exit_page"))

@app.route("/exit")
def exit_page():
    return "<h1>Thanks for Visiting!</h1> <a href='/'>Back to Home</a>"

@app.route("/personal")
def personal():
    if "user" in session:
        return render_template("personal.html", user=session["user"])
    return redirect(url_for("login"))

@app.route("/projects")
def projects():
    if "user" in session:
        return render_template("projects.html")
    return redirect(url_for("login"))

@app.route("/resume")
def resume():
    if "user" in session:
        return render_template("resume.html")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
