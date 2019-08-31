from discord.ext import commands
from bot.QueueBot import QueueBot
from PlayerQueue import PlayerQueue
import  db.connect 
import configparser 
from getservers import get_servers
from socket_layer.socket_layer import start
# set up the config variables
config = configparser.ConfigParser()
config.read('config.ini')
print(config)
#initialize PlayerQueue object
pq = PlayerQueue()

#initialize socket process
start(pq)

# run bot

bot = commands.Bot(command_prefix="!")
bot.add_cog(QueueBot(bot, pq))
bot.run(config['bot']['client_key'])
