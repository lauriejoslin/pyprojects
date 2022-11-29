import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///votes.db")


"""@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response """

@app.route("/vote", methods=["GET", "POST"])
def vote():
    if request.method == "POST":
        print("alpha")
        name = request.form.get("name")
        opinion = request.form.get("opinion")
        db.execute("INSERT INTO GENERAL (firstname, opinion) VALUES(?,?)", name, opinion)
        return redirect("/vote")
    votes = db.execute("SELECT * FROM GENERAL")
    return render_template("vote.html", votes=votes)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print('why does this work')
        name = request.form.get("name")
        opinion = request.form.get("opinion")
        db.execute("INSERT INTO GENERAL (firstname, opinion) VALUES(?,?)", name, opinion)
        return redirect(url_for('vote'))
    return render_template("index.html")



