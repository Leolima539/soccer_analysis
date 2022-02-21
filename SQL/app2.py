from importlib_metadata import metadata
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from flask import Flask, jsonify, render_template, request


#################################################
# Database Setup
#################################################
connection_string = "postgres:taunus48@localhost:5432/football_db"
engine = create_engine(f'postgresql://{connection_string}')
session = sessionmaker(engine)
# reflect an existing database into a new model
metadata = MetaData()
metadata.reflect(engine)
Base = automap_base(metadata=metadata)
# reflect the tables
Base.prepare(engine, reflect=True)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def from_coordinates():
    locations_from = """SELECT locations.latitude, locations.longitude\
    FROM locations\
    JOIN league_countries c ON c.country = locations.country\
    JOIN transfers t ON t.league_from = league_name\
    WHERE name= 'Neymar'"""
    # transfers_from = pd.read_sql_query(locations_from, con=engine)
    return locations_from

if __name__ == '__main__':
    app.run(debug=True)
