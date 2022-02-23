import json
import numpy as np
from sqlalchemy import create_engine, func
from sqlalchemy import Column, Integer, String, Float
from flask import Flask, jsonify, render_template, flash, redirect, request, abort,send_from_directory, send_file
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()
connection_string = "postgres:taunus48@localhost:5432/football_db"
engine = create_engine(f'postgresql://{connection_string}')
# Base = automap_base()
Base.metadata.create_all(engine)



app = Flask(__name__)

class Transfers(Base):
    __tablename__ = 'transfers'
    index = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)
    age = Column(Integer)
    team_from = Column(String)
    league_from = Column(String)
    team_to = Column(String)
    league_to = Column(String)
    season = Column(String)
    market_value = Column(Integer)
    transfer_fee = Column(Integer)

class Leagues(Base):
    __tablename__ = 'league_countries'
    league_name = Column(Integer, primary_key=True)
    country = Column(String)

class Locations(Base):
    __tablename__ = 'locations'
    country = Column(Integer, primary_key=True)
    country_code = Column(Integer)
    latitude = Column(Integer)
    longitude = Column(Integer)

user_input = input("What season do you want to check? ")

# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route("/")
def from_coordinates():
    session = Session(engine)

    
    results = session.query(Locations.latitude,Locations.longitude,Locations.country).\
        join(Leagues, Leagues.country == Locations.country).\
            join(Transfers, Transfers.league_from == Leagues.league_name).\
                filter(Transfers.season == user_input)
    session.close()
    res = []
    for latitude, longitude, country in results:
        dict1 = {}
        dict1["coordinates"] = longitude, latitude
        dict1["type"] = 'Point'
        dict1["country"] = country

        res.append(dict1)
    trans_json = open("myfile.geojson", "w")
    json.dump(res, trans_json, indent=6)
    
    json_json = open("samples.json", "w")
    json.dump(res, json_json, indent=6)
    trans_json.close()
    return jsonify(res)
    


@app.route("/transfer-map")
def transfer_map():
    return render_template("transfer.html")


    # results = session.query(Transfers).filter_by(eason="Neymar")
    # for name in results:
    #     print(name.league_to)

if __name__ == '__main__':
    app.run(debug=True)