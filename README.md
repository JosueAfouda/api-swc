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

- Documenting your API


Updating your README.md

# SportsWorldCentral (SWC) Fantasy Football API Documentation

Thanks for using the SportsWorldCentral API. This is your one-stop shop for
accessing data from our fantasy football website, www.sportsworldcentral.com.


## Table of Contents

- [Public API](#public-api)                        
- [Getting Started](#getting-started)                          
  - [Analytics](#analytics)                     
  - [Player](#player)                    
  - [Scoring](#scoring)                 
  - [Membership](#membership)                 
- [Terms of Service](#terms-of-service)                  
- [Example Code](#example-code)                       
- [Software Development Kit (SDK)](#software-development-kit-sdk)                 

## Public API 

*Coming Soon*

We'll be deploying our application soon. Check back for the public API address.

## Getting Started

Since all of the data is public, the SWC API doesn't require any authentication. 
All of the the following data is available using GET endpoints that return 
JSON data.

### Analytics

Get information about the health of the API and counts of leagues, teams, 
and players.

### Player
You can get a list of all NFL players, or search for an individual player 
by player_id.

### Scoring

You can get a list of NFL player performances, including the fantasy points they 
scored using SWC league scoring.

### Membership
Get information about all the SWC fantasy football leagues and the teams in them.

## Terms of Service

By using the API, you agree to the following terms of service:

- **Usage Limits**: You are allowed up to 2000 requests per day. Exceeding this 
                    limit may result in your API key being suspended.
- **No Warranty**: We don't provide any warranty of the API or its operation.

## Example Code

Here is some Python example code for accessing the health check endpoint:

```
import httpx

HEALTH_CHECK_ENDPOINT = "/"
    
with httpx.Client(base_url=self.swc_base_url) as client:
    response = client.get(self.HEALTH_CHECK_ENDPOINT)
    print(response.json())
```

## Software Development Kit (SDK)
*Coming Soon*

Check back for the Python SDK for our API.