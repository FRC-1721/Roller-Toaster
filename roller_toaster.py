import discord, json, os
from discord.ext import commands

def get_prefix(bot, message):
    prefixes = ['>', 'rawr ', '!']

    # If outside a guild (in a dm)
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

# Extensions (commands a user can excecute basicly)
initial_extensions = ['cogs.coinflip',
                      'cogs.subteam',
                      'cogs.update']

bot = commands.Bot(command_prefix=get_prefix, description='A Robot')

# Load in each cog (game)
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

    configpath = os.getcwd() + 'config.json'
    print(configpath)
    with open(configpath) as f: # Load the config as f
        config = json.load(f) # Read the config out


@bot.event
async def on_ready():
    # Runs when ready

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    await bot.change_presence(activity=discord.Game(name="Playing nothing"))
    print(f'Successfully logged in and booted...!')


bot.run(config.get('token', None), bot=True, reconnect=True) # Start the bot using the token from dict config