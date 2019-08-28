from discord.ext import commands
from bot.QueueBot import QueueBot
from db.connect import test, create_player
import configparser 
# set up the config variables
config = configparser.ConfigParser()
config.read('config.ini')

#initialize database

# run bot
bot = commands.Bot(command_prefix="!")
bot.add_cog(QueueBot(bot))
bot.run(config['bot']['client_key'])
