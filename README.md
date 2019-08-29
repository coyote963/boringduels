# Boring Duels
This websites is designed to facilitate boring man duels

It has two major portions: a sqlite database for maintaining records, a discord bot to handle user settings, and an application for handling logic and socket operations.

There are three components: discord bot, a socket layer, and database layer

Discord bot: has commands for user interaction. Doesn't have any logic, but calls the other layers

Socket layer: interfaces with the game

Database layer: executes SQL statements

And then there is a session object that keeps track of the current game in progress.

### Set up
clone this repo

pip install requirements.txt

(optionally start a virtual environment)

install sqlite database

initialize a database in project root

name the database: data.db

run the createtable sql script

create a config file with:

client_key = "YOUR_DISCORD_BOT_KEY_GOES_HERE"

You are all set, run the program with python main.py