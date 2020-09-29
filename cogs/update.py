import discord, git, os

from discord.ext import commands

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # Pass in the bot object locally

    def git_update(self):
        repo = git.cmd.Git(os.getcwd()) # set the repo location
        repo.pull() # Pull!
        return("Finished updating the bot. Restarting now.") # Message back


    @commands.command(name='update') # This is a command, its name is flip
    async def update(self, ctx): # Pass in self and ctx (data about what triggered this cog)
        role = discord.utils.find(lambda r: r.name == 'Discord Server Admin', ctx.guild.roles)
        if role in ctx.author.roles:
            await ctx.send("Updating bot.")
            await ctx.send(self.git_update())
            exit()
        else:
            await ctx.send("{} is not an admin. You must be an admin to update the bot remotely.".format(ctx.author.name))

def setup(bot): # Gets passed when created
    bot.add_cog(Update(bot)) # Add this cog
