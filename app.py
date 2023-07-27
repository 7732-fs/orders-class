from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
from db import get_dicts
import db
import datetime

@app.route('/')
def home():
    today=datetime.date.today()
    return render_template("orders.html", orders=sorted(get_dicts(), key=lambda i:i["date"]), companies=db.get_companies(), date="/".join([str(today.day), str(today.month), str(today.year)]))

@app.route('/add')
def add():
    pass

@app.route('/delete')
def method_name():
    db.query_db(f"DELETE FROM orders WHERE id={request.args['id']}")
    return redirect(url_for("home"))


