import os.path
import sqlite3

conn = sqlite3.connect("../data.db")
c = conn.cursor()


# Inserts a new player
def create_player(steam_id, discord_id):
    c.execute('''INSERT INTO Players (SteamId, DiscordId) 
        VALUES (?, ?)''',
        (steam_id, discord_id))
    conn.commit()

# Inserts a new session
def create_session(game_map, steam_id_usc, steam_id_man):
    c.execute('''INSERT INTO Sessions (Map, UscPlayer, ManPlayer)
        VALUES (?, ?, ?)''',
        (game_map, steam_id_usc, steam_id_man))
    conn.commit()


# Inserts a new kill
def create_kill(killer, victim, weapon, session_id):
    c.execute('''INSERT INTO Kills (Killer, Victim, Weapon, Session)
        VALUES (?, ?, ?)''',
        (killer, victim, weapon, session_id))
    conn.commit()

# Gets the player for a steam_id
def get_player(steam_id):
    c.execute('''SELECT * FROM Players WHERE SteamId=?''', (steam_id,))
    return c.fetchall()

# Gets the player for a discord_id
def get_player_discord(discord_id):
    c.execute('''SELECT * FROM Players WHERE DiscordId=?''', (discord_id,))
    return c.fetchall()

# Gets the sessions for a steamid
def get_session(steam_id):
    c.execute('''SELECT * FROM Players WHERE UscPlayer=? OR ManPlayer=?''', (steam_id,))
    return c.fetchall()