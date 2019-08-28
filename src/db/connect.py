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

def create_session(game_map, steam_id_usc, steam_id_man):
    c.execute('''INSERT INTO Sessions (Map, UscPlayer, ManPlayer)
        VALUES (?, ?, ?)''',
        (game_map, steam_id_usc, steam_id_man))
    conn.commit()

def create_kill(killer, victim, weapon, session_id):
    c.execute('''INSERT INTO Kills (Killer, Victim, Weapon, Session)
        VALUES (?, ?, ?)''',
        (killer, victim, weapon, session_id))
    conn.commit()

