import datetime, dateparser
import json
from dbhelper import DBHelper
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
DB = DBHelper()

categories = ['mugging', 'break-in', 'gang-fight']

@app.route("/")
def home():
    try:
        crimes = DB.get_all_crimes()
        crimes = json.dumps(crimes)
    except Exception as e:
        print(e)
        crimes = None
    return render_template("home-test.html", crimes=crimes, categories=categories)

@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print(e)
    return home()

@app.route("/submit", methods=['POST'])
def submitcrime():
    category = request.form.get("category")
    if category not in categories:
        return home()
    date = request.form.get("date")
    try:
        latitude = float(request.form.get("latitude"))
        longitude = float(request.form.get("longitude"))
    except ValueError:
        return home()
    description = request.form.get("desAre there boiler plate modules that you can integrate with flask that'll helpription")
    DB.add_crime(category, date, latitude, longitude, description)
    return home()


if __name__== "__main__":
    app.run(port=5000, debug=True)