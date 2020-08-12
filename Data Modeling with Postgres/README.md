Data Modeling with Postgres - Sparkify

Purpose:
The purpose of this project is to define a database for a music streaming company called Sparkify, which helps its analytical teams to identify user activity on songs played in their app, so that they can take intelligent decisions to expand thier business.

Database Design
The database has 4 dimension(songs, artists, users, time) tables and 1 fact(songplays) table. Database is designed in star schema to query on the user historical activity. As the analytics deals with huge data, we have created the database in star schema as it needs less joins.

List of files in the workspace.

create_tables.py - This script creates schema, drops and create tables in the database.
sql_queries.py - This script has drop, create and insert queries
etl.py - This script loads the data into all the tables.

How to load the data into database.

This job will drop and create tables.
First script to run : create_tables.py
Command : python create_tables.py

The below script will insert the data into dimension and fact tables.
Second script to run - etl.py
Command : python etl.py

