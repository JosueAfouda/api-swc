# api-swc
Create API for SportsWorldCentral Fantasy Football company

This project demonstrates API coding best practices using Python and FastAPI.

- Créer la database SQLite3 et les tables (par CLI ou script create_fantasy_db.py)

- Now that the tables are created, you will populate them with football data

    **par CLI** :

Turn on foreign key enforcement with the following statement:

sqlite> PRAGMA foreign_keys = ON;
Prepare the import statement to recognize CSV format with the following command:

sqlite> .mode csv
Run the following commands from the sqlite prompt to load the data. Run them in the order shown here:

sqlite> PRAGMA foreign_keys = ON;
sqlite> .mode csv
sqlite> .import --skip 1 data/player_data.csv player
sqlite> .import --skip 1 data/performance_data.csv performance
sqlite> .import --skip 1 data/league_data.csv league
sqlite> .import --skip 1 data/team_data.csv team
sqlite> .import --skip 1 data/team_player_data.csv team_player
sqlite>
Use the following commands to verify that the correct number of records was loaded into each table. The performance table has been loaded with records using two different last_changed_date values so that you can verify date searching functions are working correctly:

sqlite> select count(*) from player;
1018
sqlite> select count(*) from performance;
17306
sqlite> select count(*) from performance where last_changed_date > '2024-04-01';
2711
sqlite> select count(*) from league;
5
sqlite> select count(*) from team;
20
sqlite> select count(*) from team_player;
140
To exit the SQLite application, type .exit:

sqlite> .exit
$

    **Par script insert_csv_to_sqlite.py**

- Accessing Your Data Using Python

    You will now create the files that are required to query the database using Python.

    Filename	Purpose
crud.py         Helper function to query the database

database.py     Configures SQLAlchemy to use the SQLite database

models.py       Defines the SQLAlchemy classes related to the database tables

requirements.txt     Used to install specific versions of libraries with the pip package manager

test_crud.py       The pytest file to unit-test your SQLAlchemy files

The file named models.py will contain the Python representation of the data. The classes in this file will be used when you query databases in Python.

- Create the FastAPI code to use this data and publish it as a REST API.