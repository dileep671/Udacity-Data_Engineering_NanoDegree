Project Datawarehouse

Project description
Sparkify is a music streaming startup with a growing user base and song database.Their user activity and songs metadata data resides in json files in S3. The goal of the current project is to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.

Run the cluster_creation script to set up the needed infrastructure for this project.

$ python cluster_creation.py

Run the create_tables script to set up the database staging and analytical tables

$ python create_tables.py

Finally, run the etl script to extract data from the files in S3, stage it in redshift, and finally store it in the dimension and fact tables.

$ python etl.py

Below are the count of records of all analytical tables

Running select COUNT(*) AS total FROM artists
    10025
Running select COUNT(*) AS total FROM songs
    14896
Running select COUNT(*) AS total FROM time
    6813
Running select COUNT(*) AS total FROM users
    104
Running select COUNT(*) AS total FROM songplays
    9957

Steps followed on this project

Create Table Schemas

Design schemas for your fact and dimension tables
Write a SQL CREATE statement for each of these tables in sql_queries.py
Complete the logic in create_tables.py to connect to the database and create these tables
Write SQL DROP statements to drop tables in the beginning of - create_tables.py if the tables already exist. This way, you can run create_tables.py whenever you want to reset your database and test your ETL pipeline.
Launch a redshift cluster and create an IAM role that has read access to S3.
Add redshift database and IAM role info to dwh.cfg.
Test by running create_tables.py and checking the table schemas in your redshift database. You can use Query Editor in the AWS Redshift console for this.

Build ETL Pipeline

Implement the logic in etl.py to load data from S3 to staging tables on Redshift.
Implement the logic in etl.py to load data from staging tables to analytics tables on Redshift.
Test by running etl.py after running create_tables.py and running the analytic queries on your Redshift database to compare your results with the expected results.

Delete your redshift cluster when finished.

Document Process Do the following steps in your README.md file.

