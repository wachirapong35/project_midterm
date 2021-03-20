from flask import Flask,render_template,request,redirect,Blueprint
from urllib.parse import quote
from urllib.request import urlopen
from flask.templating import render_template
import json
import requests
import urllib.parse
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

today = datetime.today()
dtd = today.strftime("%Y-%m-%d")

fixtures = Blueprint('fixtures',__name__)

x_rapidapi_key = "49b84b96f9msh6d2625b2a3dde7ap153edbjsnec26e9bf9ce7"
x_rapidapi_host = "api-basketball.p.rapidapi.com"

@fixtures.route("/fixtures")
def fixtures_game():

    url = "https://api-basketball.p.rapidapi.com/games"
    querystring = {"season":"2020-2021","timezone":"Asia/Bangkok","league":"12","date":f"{dtd}"}
    headers = {
            'x-rapidapi-key': x_rapidapi_key,
            'x-rapidapi-host': x_rapidapi_host
            }
    x = requests.request("GET", url, headers=headers, params=querystring).json()
    fixtures = x['response']
    return render_template('fixtures.html',fixtures=fixtures)