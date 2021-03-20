from flask import Flask,render_template,request,redirect,Blueprint
from urllib.parse import quote
from urllib.request import urlopen
from flask.templating import render_template
import json
import requests
import urllib.parse
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template


livescore = Blueprint('livescore',__name__)
API_KEY = '933b69c86c1b3ea85c48d115a67876bf17afca24aaf1b009fd9e79a2c6c31662'
LIVESCORE_URL = 'https://allsportsapi.com/api/basketball/?met=Livescore&timezone=Asia/Bangkok&APIkey={API_KEY}'

@livescore.route("/livescore")
def livescores():
    #ใช้LIVESCORE_URL
    result = get_livescore(API_KEY)
    return render_template('livescore.html',result=result)

def get_livescore(API_KEY):
    url = LIVESCORE_URL.format(API_KEY=API_KEY)
    data = urlopen(url).read()
    parsed = json.loads(data)
    result = []

    for i in range(len(parsed['result'])):

        event_date = parsed['result'][i]['event_date']
        event_time = parsed['result'][i]['event_time']
        event_home_team = parsed['result'][i]['event_home_team']
        event_away_team = parsed['result'][i]['event_away_team']
        event_final_result = parsed['result'][i]['event_final_result']
        league_name = parsed['result'][i]['league_name']
        league_round = parsed['result'][i]['league_round']
        home_team_key = parsed['result'][i]['home_team_key']
        away_team_key = parsed['result'][i]['away_team_key']
        url_home = 'https://allsportsapi.com/logo-basketball/{team_key}_{team_name}.png'.format(team_key=home_team_key,API_KEY=API_KEY,team_name=event_home_team.lower()).replace(" ","-")
        url_away = 'https://allsportsapi.com/logo-basketball/{team_key}_{team_name}.png'.format(team_key=away_team_key,API_KEY=API_KEY,team_name=event_away_team.lower()).replace(" ","-")
        
        try:
            f1stQuarter = parsed['result'][i]['scores']['1stQuarter'][0]
        except IndexError:
            f1stQuarter = 'null' 

        try:
            s2ndQuarter = parsed['result'][i]['scores']['2ndQuarter'][0]  
        except IndexError: 
            s2ndQuarter = 'null'  

        try:
            t3rdQuarter = parsed['result'][i]['scores']['3rdQuarter'][0]
        except IndexError:  
            t3rdQuarter = 'null'   
            
        try:         
            f4thQuarter = parsed['result'][i]['scores']['4thQuarter'][0]
        except IndexError:
            f4thQuarter = 'null'

        result.append({"event_date":event_date,
                        "event_time":event_time,
                        "event_home_team":event_home_team,
                        "event_away_team":event_away_team,
                        "event_final_result":event_final_result,
                        "league_name":league_name,
                        "league_round":league_round,
                        "url_home":url_home,
                        "url_away":url_away,
                        "f1stQuarter":f1stQuarter,
                        "s2ndQuarter":s2ndQuarter,
                        "t3rdQuarter":t3rdQuarter,
                        "f4thQuarter":f4thQuarter})  

    return result
    