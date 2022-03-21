import sqlite3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    c = sqlite3.connect("db/database.db")
    cur = c.cursor()
    cur.execute("SELECT * FROM topics")
    items = cur.fetchall()
    return render_template("index.html", items=items)
