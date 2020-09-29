import discord, datetime, os, json

from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # Pass in the bot object locally

    @commands.command(name='help') # This is a command, its name is flip
    async def advanced_help(self, ctx): # Pass in self and ctx (data about what triggered this cog)
        author = ctx.message.author # Get the author of the command

        helptextpath = os.getcwd() + '/helptext.json'
        with open(helptextpath) as f: # Load the config as f
            helptext = json.load(f) # Read the config out

        embed = discord.Embed( # An embed object
            description = "Help Menu",
            color = discord.Color.blue()
        )

        embed.set_author(name='help')
        for command in helptext['help'].keys():
            embed.add_field(name=helptext['help'].get(command, {}).get('alias'), value=helptext['help'].get(command, {}).get('helptext'))

        await ctx.send(embed=embed)

def setup(bot): # Gets passed when created
    bot.add_cog(Help(bot)) # Add this cog
