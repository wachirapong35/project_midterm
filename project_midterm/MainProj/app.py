from flask import Flask, render_template, request, redirect, Blueprint
from urllib.parse import quote
from urllib.request import urlopen
from models import db, info
from about import about
from livescore import livescore
from fixtures import fixtures
from search_team import search_team
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
import requests
import json


app = Flask(__name__)
app.register_blueprint(about)
app.register_blueprint(livescore)
app.register_blueprint(fixtures)
app.register_blueprint(search_team)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ab_info.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


# 100 request per days
x_rapidapi_key = "49b84b96f9msh6d2625b2a3dde7ap153edbjsnec26e9bf9ce7"
x_rapidapi_host = "api-basketball.p.rapidapi.com"


@app.route("/")
def home():
    # ใช้STANDING
    url = "https://api-basketball.p.rapidapi.com/standings"

    querystring = {"league": "12", "season": "2020-2021"}

    headers = {
        'x-rapidapi-key': x_rapidapi_key,
        'x-rapidapi-host': x_rapidapi_host
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    western = list()
    eastern = list()
    for i in range(int(len(response['response'][0])/2)):
        check = response['response'][0][i]['group']['name']
        if check == "Western Conference":
            add = response['response'][0][i]
            western.append(add)
        else:
            add = response['response'][0][i]
            eastern.append(add)
    return render_template('home.html', standing_w=western,standing_e=eastern)

app.run(debug=True, use_reloader=True)
