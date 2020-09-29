import discord, datetime, os, json

helptextpath = os.getcwd() + '/helptext.json'
with open(helptextpath) as f: # Load the config as f
    helptext = json.load(f) # Read the config out

for command in helptext['help'].keys():
    print(command)
    print(helptext['help'].get(command, {}).get('alias'))