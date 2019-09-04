from discord.ext import commands
from bot.QueueBot import QueueBot
from session_manager.PlayerQueue import PlayerQueue
import  db.connect 
import configparser 
from getservers import get_servers
from socket_layer.helper import create_socket
from socket_layer.socket_layer import start
from threading import Event
from session_manager.session_manager import start_session
# set up the config variables
config = configparser.ConfigParser()
config.read('config.ini')
print(config)
#initialize PlayerQueue object
pq = PlayerQueue()



#initialize socket process
start(pq)

#initialize session process
e = Event()
start_session(e)

# run bot
bot = commands.Bot(command_prefix="!")
bot.add_cog(QueueBot(bot, pq, e))
bot.run(config['bot']['client_key'])
