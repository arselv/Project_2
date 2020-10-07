# import necessary libraries
from flask import Flask, render_template
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import sqlite3 as sql
import pandas as pd

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///uk_motorcycle_accidents_sqlite.sqlite")
#session = Session(engine)
# reflect an existing database into a new model
#Base = automap_base()
# reflect the tables
#Base.prepare(engine, reflect=True)

#################################################
# Flask Setup
#################################################

# create instance of Flask app
app = Flask(__name__)

# Set Variables (Needs correcting/connection)
lat = []
lon = []

# create route that renders index.html template
@app.route('/')
def home():
    return render_template("map.html")

@app.route('/heatmap')
def heat():
    return render_template("heatmap.html")

# create route that renders index.html template
@app.route('/documentation')
def documentation():
    return render_template("documentation.html")

# The following functions would be used for returning DB Query results, possible examples
@app.route("/agegrps")
def ageGroups(value):
    if value == "Under 19":
        session = Session(engine)
        lat = session.execute('Select Latitude From uk_motorcycle_accidents Where Age_Group = "Under 19"').fetchall()
        lon = session.execute('Select Longitude From uk_motorcycle_accidents Where Age_Group = "Under 19"').fetchall()
        session.close()
    elif value == "18 to 25":
        session = Session(engine)
        lat = session.execute('Select Latitude From uk_motorcycle_accidents Where Age_Group = "18 to 25"').fetchall()
        lon = session.execute('Select Longitude From uk_motorcycle_accidents Where Age_Group = "18 to 25"').fetchall()
        session.close()
    elif value == "26 to 35":
        session = Session(engine)
        lat = session.execute('Select Latitude From uk_motorcycle_accidents Where Age_Group = "26 to 35"').fetchall()
        lon = session.execute('Select Longitude From uk_motorcycle_accidents Where Age_Group = "26 to 35"').fetchall()
        session.close()
    elif value == "36 to 45":
        session = Session(engine)
        lat = session.execute('Select Latitude From uk_motorcycle_accidents Where Age_Group = "36 to 45"').fetchall()
        lon = session.execute('Select Longitude From uk_motorcycle_accidents Where Age_Group = "36 to 45"').fetchall()
        session.close()
    elif value == "46 to 55":
        session = Session(engine)
        lat = session.execute('Select Latitude From uk_motorcycle_accidents Where Age_Group = "46 to 55"').fetchall()
        lon = session.execute('Select Longitude From uk_motorcycle_accidents Where Age_Group = "46 to 55"').fetchall()
        session.close()
    elif value == "46 to 55":
        session = Session(engine)
        lat = session.execute('Select Latitude From uk_motorcycle_accidents Where Age_Group = "46 to 55"').fetchall()
        lon = session.execute('Select Longitude From uk_motorcycle_accidents Where Age_Group = "46 to 55"').fetchall()
        session.close()
    elif value == "Over 55":
        session = Session(engine)
        lat = session.execute('Select Latitude From uk_motorcycle_accidents Where Age_Group = "46 to 55"').fetchall()
        lon = session.execute('Select Longitude From uk_motorcycle_accidents Where Age_Group = "46 to 55"').fetchall()
        session.close()
    
    return render_template("map.html", lat=lat, lon=lon)

@app.route("/gengrps")
def genderGroups(value):
    session = Session(engine)

    session.close()
    return render_template("map.html", lat=lat, lon=lon)

@app.route("/yearcas")
def yearCasualties():
    session = Session(engine)

    session.close()
    return render_template("map.html", lat=lat, lon=lon)

# create route that renders ALL DATABASE LAT AND LONG 
@app.route('/ageGroups')
def latlng():
    df = pd.read_sql_query('Select * from uk_motorcycle_accidents', con=engine).head()
    return df.to_json(orient='index')



if __name__ == "__main__":
    app.run(debug=True)
