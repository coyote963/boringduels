import discord
import queue

from discord.ext import commands
bot = commands.Bot(command_prefix='$')
class QueueBot(commands.Cog):
    def __init__(self, bot, player_queue):
        self.bot = bot
        self._last_member = None
        self.nature = ["dog","cat","fish","bird"]
        self.player_queue = player_queue
        print("bot initted")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        print("Message received")
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

    @commands.command()
    async def animal(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        print(self.nature[0])
        self._last_member = member
    
    @commands.command()
    async def register(self, ctx, arg= None):
        if (arg == None):
            ctx.send("You need to provide your boring man in game name, see pins")
        else:
            await ctx.send("Your in game name can now join the server: " + arg)

    @commands.command()
    async def join(self, ctx):
        await ctx.send("i added u into the queue")

    @commands.command()
    async def info(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        
        await member.send("hello")
       