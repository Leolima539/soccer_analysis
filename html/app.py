import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
from flask import Flask, render_template


#################################################
# Database Setup
#################################################
connection_string = "postgres:taunus48@localhost:5432/football_db"
engine = create_engine(f'postgresql://postgres:taunus48@localhost:5432/football_db')

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)

# # Save reference to the table
# dataFrame = Base.classes.football_df

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/transfer.html")
def transfers():
    
    def from_coordinates():
        locations_from = """SELECT locations.latitude, locations.longitude\
        FROM locations\
        JOIN league_countries c ON c.country = locations.country\
        JOIN transfers t ON t.league_from = league_name\
        WHERE name={season_selection}"""
        transfers_from = pd.read_sql_query(locations_from, con=engine)
        return transfers_from

    def to_coordinates():
        locations_to = """SELECT locations.latitude, locations.longitude\
        FROM locations\
        JOIN league_countries c ON c.country = locations.country\
        JOIN transfers t ON t.league_from = league_name\
        WHERE name={season_selection}"""
        transfers_to = pd.read_sql_query(locations_to, con=engine)
        return transfers_to


@app.route("/api/v1.0/names")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(dataFrame.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


# @app.route("/api/v1.0/passengers")
# def passengers():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # Query all passengers
#     results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

#     session.close()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_passengers = []
#     for name, age, sex in results:
#         passenger_dict = {}
#         passenger_dict["name"] = name
#         passenger_dict["age"] = age
#         passenger_dict["sex"] = sex
#         all_passengers.append(passenger_dict)

#     return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)


