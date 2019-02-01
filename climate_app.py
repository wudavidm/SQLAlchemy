# 1. import Flask
import sqlalchemy
import numpy as np
import pandas as pd
import datetime as dt
from flask import Flask, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# Create the connection engine to the sqlite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask Routes
@app.route("/")
def homepage():
    """List of all returnable API routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of Dates and Temp."""
	  results = session.query(Measurement).all()
	  precipitation_list  = []
	  for result in results:
		row = {}
		row = ['date'] = Measurement.date
		row = ['tobs'] = Measurement.tobs
		
	return jsonify (precipitation_list)
	
@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations"""
	  results = session.query(Station).all()
	  station_list = []
	  for result in results:
		row = {}
		row = ['name'] = Station.name
		row = ['station'] = Station.station
		row = ['elevation'] = Station.elevation
	return jsonify (station_list)
		
	  
@app.route("/api/v1.0/tobs")
def temp_obs():
    """Return a list of tobs."""