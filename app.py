# import necessary libraries
from flask import Flask, render_template, jsonify
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
@app.route("/gengrps/<GenderRange>")
def genderGroups(GenderRange):
    df = pd.read_sql_query(f"Select * From uk_motorcycle_accidents Where Sex_of_Casualty = '{GenderRange}'", con=engine)
    df_dict = df.to_dict(orient = 'record')
    return jsonify(df_dict)

@app.route("/yearcas/<YearRange>")
def yearCasualties(YearRange):
    df = pd.read_sql_query(f"Select * From uk_motorcycle_accidents Where Year = '{YearRange}'", con=engine)
    df_dict = df.to_dict(orient = 'record')
    return jsonify(df_dict)

# create route that renders ALL DATABASE LAT AND LONG 
@app.route('/agegrps/<AgeRange>')
def ageGroups(AgeRange):
    df = pd.read_sql_query(f"Select * From uk_motorcycle_accidents Where Age_Group = '{AgeRange}'", con=engine)
    df_dict = df.to_dict(orient = 'record')
    return jsonify(df_dict)

@app.route('/fltrdgrps/<YearRange>/<GenderRange>/<AgeRange>')
def filteredGroup(YearRange, GenderRange, AgeRange):
    df = pd.read_sql_query(f"Select * From uk_motorcycle_accidents Where Year = '{YearRange}' and Sex_of_Casualty = '{GenderRange}' and Age_Group = '{AgeRange}'", con=engine)
    df_dict = df.to_dict(orient = 'record')
    return jsonify(df_dict)

@app.route('/all500')
def all500():
    df = pd.read_sql_query(f"Select * From uk_motorcycle_accidents LIMIT 500" , con=engine)
    df_dict = df.to_dict(orient = 'record')
    return jsonify(df_dict)

@app.route('/all')
def all():
    df = pd.read_sql_query(f"Select * From uk_motorcycle_accidents" , con=engine)
    df_dict = df.to_dict(orient = 'record')
    return jsonify(df_dict)

if __name__ == "__main__":
    app.run(debug=True)
