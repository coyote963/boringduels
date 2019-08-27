import os.path
import sqlite3

conn = sqlite3.connect("../data.db")
c = conn.cursor()

def test():
    c.execute('SELECT name from sqlite_master where type= "table"')
    print(c.fetchall())

def create_player(steam_id, discord_id):
    c.execute('''INSERT INTO Players (SteamId, DiscordId) 
        VALUES (?, ?)''',
        (steam_id, discord_id))
    conn.commit()