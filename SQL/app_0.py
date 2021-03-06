import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='football_db',
                            user=['postgres'],
                            password=['taunus48'])
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM transfers;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)