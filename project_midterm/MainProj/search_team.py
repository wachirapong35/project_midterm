from flask import Flask,render_template,request,redirect,Blueprint
from urllib.parse import quote
from urllib.request import urlopen
from flask.templating import render_template
import json
import requests
import urllib.parse
from flask_sqlalchemy import SQLAlchemy

search_team = Blueprint('search_team',__name__)

x_rapidapi_key = "49b84b96f9msh6d2625b2a3dde7ap153edbjsnec26e9bf9ce7"
x_rapidapi_host = "api-basketball.p.rapidapi.com"

@search_team.route("/team" , methods=["get", "post"])
def s_team():
    #ใช้TEAM_URL
    if request.method == "GET":
        return render_template('search_team.html')
    if request.method == "POST":
     #code search team
        url = "https://api-basketball.p.rapidapi.com/teams"
        querystring = {"search":"boston"}

        headers = {
        'x-rapidapi-key': x_rapidapi_key,
        'x-rapidapi-host': x_rapidapi_host,
         }
        word=request.form["team_search"]     
        x = str(word)
        querystring = {"search":f"{x}"}
        x = requests.request("GET", url, headers=headers, params=querystring).json()

        search_team = x['response']
        return render_template('search_team.html',search_team=search_team)
         
             