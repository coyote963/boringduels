from discord.ext import commands
from bot.QueueBot import QueueBot
from PlayerQueue import PlayerQueue
import  db.connect 
import configparser 
# set up the config variables
config = configparser.ConfigParser()
config.read('config.ini')

#initialize PlayerQueue object
pq = PlayerQueue()


# run bot
bot = commands.Bot(command_prefix="!")
bot.add_cog(QueueBot(bot, pq))
bot.run(config['bot']['client_key'])
