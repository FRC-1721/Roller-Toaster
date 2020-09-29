import discord
import random

from discord.ext import commands

class Rolling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='role') #role in the initial argument
    async def role(self, chan, *, chain = None): #chan is message information, chain is an additional argument, and the * means that after the seccond argument can include spaces
        if chain is None:
            await chan.send("give me args plz")
        else:
            await chan.send(str(chain))

def setup(bot):
    bot.add_cog(Rolling(bot))
