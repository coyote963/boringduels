# Boring Duels
This websites is designed to facilitate boring man duels

It has two major portions: a sqlite database for maintaining records, a discord bot to handle user settings, and an application for handling logic and socket operations.

There are three components: discord bot, a socket layer, and database layer

Discord bot: has commands for user interaction. Doesn't have any logic, but calls the other layers

Socket layer: interfaces with the game

Database layer: executes SQL statements

