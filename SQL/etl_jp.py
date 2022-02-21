
from tkinter import Y
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
# from sqlalchemy_utils import database_exists, create_database
from local_settings import postgresql as settings
import pandas as pd
from sqlalchemy import text
import psycopg2

connection_string = "postgres:taunus48@localhost:5432/football_db"
engine = create_engine(f'postgresql://{connection_string}')

def from_coordinates():
    locations_from = text("SELECT locations.latitude, locations.longitude\
    FROM locations\
    JOIN league_countries c ON c.country = locations.country\
    JOIN transfers t ON t.league_from = league_name\
    WHERE name=:year_input")
    transfers_from = pd.read_sql_query(locations_from, con=engine)
    return transfers_from

def to_coordinates():
    x =  ('2010-2011')
    locations_to = ("SELECT locations.latitude, locations.longitude\
    FROM locations\
    JOIN league_countries c ON c.country = locations.country\
    JOIN transfers t ON t.league_from = league_name\
    WHERE season =:image_id_input;", 
        {"image_id_input": x})
    
    transfers_to = pd.read_sql_query(locations_to, con=engine)
    print(transfers_to)
    return transfers_to
    

# year_input = input("Choose a year between 2008 and 2017 ")
# year_end = year_input+1
# season_selection = (f'{year_input}-{year_end}')

# print(season_selection)

to_coordinates()