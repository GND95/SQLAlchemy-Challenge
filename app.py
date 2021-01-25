from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    #text returned to be in HTML since that's what the web page can render
    return "<strong>Available routes:</strong>\
            <ul>\
            <li><i>/api/v1.0/precipitation</i></li>\
            <li><i>/api/v1.0/stations</i></li>\
            <li><i>/api/v1.0/tobs</i></li>\
            <li><i>/api/v1.0/<strong>[start]</strong></i></li>\
            <li><i>/api/v1.0/<strong>[start]</strong>/<strong>[end]</strong></i></li>\
            </ul>"

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'precipitation' endpoint...")
    precipitation_query_results = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date).all() #querying the SQLite DB
    session.close() #closing connection to database

    precipitation_list = [] #list for storing the dictionary
    for date, prcp in precipitation_query_results: #for every date and precipitation value in the query results
        precipitation_dictionary = {} #dictionary used to keep the dates (as keys) and precipitation (as values) separate
        precipitation_dictionary[date] = prcp #for each row of the query results, the date will be the dictionary key and the precipitation will be the dictionary value
        precipitation_list.append(precipitation_dictionary) #append the dictionary to the list so later we can jsonify the data

    return jsonify(precipitation_list) #return the JSON representation of the list

@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'stations' endpoint...")
    station_query_results = session.query(Station.station).all() #query for getting all the weather station names
    station_list = []
    for element in station_query_results:
        station_list.append(element[0]) #iterating through the list of lists to get the 0th element of each inner list (station name)
    return jsonify(station_list) #return the JSON representation of the list

@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'tobs' endpoint...")
    return "Welcome to my 'tobs' endpoint!"

@app.route("/api/v1.0/<start>") #TODO
def startDate():
    print("Server received request for 'start' endpoint...")
    return "Welcome to my 'start' endpoint!"

@app.route("/api/v1.0/<start>/<end>") #TODO 
def startEndDate():
    print("Server received request for 'start/end' endpoint...")
    return "Welcome to my 'start/end' endpoint!"

if __name__ == "__main__":
    app.run(debug=True)