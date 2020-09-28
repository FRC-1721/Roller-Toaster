import discord
import random

from discord.ext import commands

class CoinFlip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # Pass in the bot object locally

    @commands.command(name='flip') # This is a command, its name is flip
    async def coinflip(self, ctx): # Pass in self and ctx (data about what triggered this cog)
        if (random.randint(0, 1) == 0): # Randomize
            await ctx.send('Heads')
        else:
            await ctx.send("Tails")

def setup(bot): # Gets passed when created
    bot.add_cog(CoinFlip(bot)) # Add this cog
