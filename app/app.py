import sqlite3
import datetime

from flask import Flask, render_template
from flask_compress import Compress
from flask_apscheduler import APScheduler

class Config:
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)

Compress(app)

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

start = datetime.time(23, 50, 0)
end = datetime.time(23, 59, 0)


@app.route("/")
def index():
    if time_in_range(start, end, datetime.datetime.now().time() ):
        return render_template("update.html")
    else:
        c = sqlite3.connect("db/database.db")
        cur = c.cursor()
        cur.execute("SELECT * FROM topics")
        items = cur.fetchall()
        return render_template("index.html", items=items)