

# About
This project sets up a mock PostgreSQL database for a fictional news website. 
This python script was created as an internal reporting tool to discover what 
kind of articles the site's reader's like. It connects to the database, use SQL 
queries to analyze the log data and prints out the answers to the following 
questions:

> Which are the most popular 3 articles of all time?
> Who are the most popular article authors of all time? 
> On which date(s) did more than 1% of requests lead to errors?

# Dependencies
1. PostgreSQL
2. Python 2.7
3. Psycopg2 module

# Getting Started

In order to get started, you'd need to get your local database set up by doing 
the following: 

## Get database
1. Download the database file used in this project 
([here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip))
2. Unzip the file and save it in the same directory of this project

## Load database
Load the file's data into your local database by running the following 
command in your command prompt, inside your project directory: 
`psql -d news -f newsdata.sql`. This command connects to your installed 
database server and executes the SQL commands in the downloaded file, creating 
tables and populating them with data.

## Create required views
Create the views that'll be used in the queries of our python script by 
running the following prompt: `psql -d news -f create_views.sql`. This command 
connects to your installed database server and executes the commands in the 
file, creating the required table views.
 
# Run the python script!
Execute the python script from your command prompt, inside the directory 
wherein it's stored, by running: `logs_project.py` or `python logs_project.py`.

