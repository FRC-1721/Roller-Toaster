import discord
import random

from discord.ext import commands

class CoinFlip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='flip')
    async def cool_bot(self, chan):
        if (random.randint(0, 1) == 0):
            await chan.send('Heads')
        else:
            await chan.send("Tails")

def setup(bot):
    bot.add_cog(CoinFlip(bot))
