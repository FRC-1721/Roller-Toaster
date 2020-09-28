import discord
import random

from discord.ext import commands

class Subteam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='subteam')
    async def cool_bot(self, chan):
        await chan.send('I have not been written yet. Lol!')

def setup(bot):
    bot.add_cog(Subteam(bot))