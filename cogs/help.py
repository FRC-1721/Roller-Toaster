import discord, datetime, os, json

from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # Pass in the bot object locally

    @commands.command(name='help') # This is a command, its name is flip
    async def advanced_help(self, ctx, verbose = None): # Pass in self and ctx (data about what triggered this cog)
        author = ctx.message.author # Get the author of the command

        helptextpath = os.getcwd() + '/data/helptext.json'
        with open(helptextpath) as f: # Load the config as f
            helptext = json.load(f) # Read the config out

        embed = discord.Embed( # An embed object
            description = "Help Menu", # Set the desc
            color = discord.Color.blue() # Set the color of the embed
        )

        embed.set_author(name='Help') # Set the author name 
        if (verbose == None): # If verbose is None (no command specified for verbose)
            for command in helptext['help'].keys(): # Print every command and the none verbose helptext
                embed.add_field(name = helptext['help'].get(command, {}).get('alias'), 
                                value=helptext['help'].get(command, {}).get('helptext'))
        else: # otherwise print a specific command and its verbose helptext
            if (verbose in helptext['help'].keys()):
                embed.add_field(name = helptext['help'].get(verbose, {}).get('alias'), 
                                value=helptext['help'].get(verbose, {}).get('verbose'))
            else:
                await ctx.send("Command '{0}'not found".format(verbose))

        await ctx.send(embed=embed)

def setup(bot): # Gets passed when created
    bot.add_cog(Help(bot)) # Add this cog
