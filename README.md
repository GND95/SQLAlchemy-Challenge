# SQLAlchemy-Challenge
Data analysis using SQLAlchemy as the ORM, a SQLite database, Pandas, Matplotlib, and creating a Flask-based API to serve the query results

## SQLAlchemy Queries
Querying weather database and plotting precipitation results: <br/>![1](/Images/1.png)<br/>
Querying weather database and building histogram from temperature observation data: <br/>![2](/Images/2.png)<br/>
Link to full analysis: https://github.com/GND95/SQLAlchemy-Challenge/blob/main/Climate%20Analysis.ipynb

## Flask API Endpoints
Home API endpoint displays the available routes/endpoints: <br/>![3](/Images/3.png)<br/>
<i>/api/v1.0/precipitation</i> endpoint queries the database for precipitation information and returns the results as JSON: <br/>![4](/Images/4.png)<br/>
<i>/api/v1.0/stations</i> endpoint queries the database for weather station information and returns the results as JSON: <br/>![5](/Images/5.png)<br/>
<i>/api/v1.0/tobs</i> endpoint queries the database for temperature information and returns the results as JSON: <br/>![6](/Images/6.png)<br/>
<i>/api/v1.0/**[start]**</i> endpoint queries the database starting at a user-defined start date and ending at the most recent weather data entry in the database. This endpoint will return the minimum, the average, and the maximum temperatures over the time period specified by the user: <br/>![7](/Images/7.png)<br/>
<i>Example format: http://127.0.0.1:5000/api/v1.0/2017-08-1</i><br/><br/>
<i>/api/v1.0/**[start]**/**[end]**</i> endpoint queries the database starting at a user-defined start date and ending at a user-defined end date. This endpoint will return the minimum, the average, and the maximum temperatures over the time period specified by the user: <br/>![8](/Images/8.png)<br/>
<i>Example format: http://127.0.0.1:5000/api/v1.0/2016-03-01/2017-08-17</i>
