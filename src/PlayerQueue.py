import queue
from datetime import timedelta, datetime 
from db.connect import get_player_discord
SESSION_TIME = 3

# A class representing any person that enters the queue. A player must have either an ign (in-game-name) or a steamid attributed to this account
class Player:
    def __init__(self, discord_id):
        self.discord_id = discord_id
        self.steam_id = ""
        self.ign = ""
        self.rating = 1000

    def set_steam (self):
        # look inside the database for a matching steam_id
        steam = get_player_discord(self.discord_id)
        if len(steam) > 0:
            self.steam_id = steam[0]

    def set_ign (self, ign):
        self.ign = ign

# A class representing a session, with a time delta
class Session:
    def __init__(self, man_player, usc_player):
        self.man_player = man_player
        self.usc_player = usc_player
        self.time_ending = datetime.now() + timedelta(minutes=SESSION_TIME)

    def is_session_active(self):
        return datetime.now() < self.time_ending

class PlayerQueue:
    def __init__(self, current_session=None):
        # queue for holding a list of the players in the queue
        self.players = queue.Queue()
        self.current_session = current_session

    def enter_queue_ign(self, discord_id, ign):
        player = Player(discord_id)
        player.set_ign(ign)
        self.players.put(player)

    def enter_queue_steamid(self, discord_id):
        player = Player(discord_id)
        player.set_steam()
        self.players.put(player)

    #requires that there is at least 2 players in queue
    def advance_queue(self):
        man_player = self.players.get()
        usc_player = self.players.get()
        current_session = Session(man_player, usc_player)
        self.current_session = current_session

    #returns if there is enough players to advance_queue
    def can_advance_queue(self):
        return len(self.players) > 1