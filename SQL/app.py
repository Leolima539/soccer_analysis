import datetime as dt
import imp
import numpy as np
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import Column, Integer, String, Float
from flask import Flask, jsonify, render_template
from sqlalchemy.ext.declarative import declarative_base
# app = Flask(__name__)

Base = declarative_base()
connection_string = "postgres:taunus48@localhost:5432/football_db"
engine = create_engine(f'postgresql://{connection_string}')

Base.metadata.create_all(engine)

session = Session(bind=engine)
# Base.classes.keys()
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

# transfers_b = Base.classes.transfers
# locations_b = Base.classes.locations
# leagues_b = Base.classes.league_countries



@app.route("/")
def from_coordinates():


    results = session.query(Transfers.name)
    for result in results:
         print(result.name)
    session.close()
    players = list(np.ravel(results))
    return jsonify(players)

    # books=engine.execute("SELECT * FROM transfers")
    # return render_template(".../html/transfers.html", books=books)


    # locations_from = session.query(transfers_b.name, transfers_b.league_from).\
    #     filter(transfers_b.season == '2011-2012').all()

    # session.close()
    # # Dict with date as the key and prcp as the value
    # # precip = {date: prcp for date, prcp in precipitation}
    # return locations_from
    
    # locations_from = engine.execute("""SELECT locations.latitude, locations.longitude\
    # FROM locations\
    # JOIN league_countries c ON c.country = locations.country\
    # JOIN transfers t ON t.league_from = league_name\
    # WHERE name= 'Neymar'""")
    # transfers_from = pd.read_sql_query(locations_from, con=engine)
    # return transfers_from 

if __name__ == '__main__':
    app.run(debug=True)