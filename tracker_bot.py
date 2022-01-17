import discord
from discord.ext import commands
from discord.ext.commands import UserConverter
import json

''' 
TrackerBot v1 
author @EthanA2025 / Ethan Abbate
A simple discord bot that tracks score 
'''

TOKEN = '' # discord token
client = commands.Bot(command_prefix= "*") # All the commands for this bot starts with a "*"

with open('tracker.json') as file: # Load dictionary (scoreboard) at the start 
    data = json.load(file)

# Function tells when the bot has logged into discord
@client.event
async def on_ready():
    print(f'Bot has logged in')

# This commands function is to add a point to the scoreboard for the specified user 
@client.command(aliases=['Add', 'add'])
async def _add(ctx, name: discord.User):
    with open('tracker.json', 'r') as file: # Adds to the dictionary, the dictionary at that user increases by one simulating a point increase
        dictionary = json.load(file)
        dictionary[str(name.id)] += 1 

    with open("tracker.json", 'w') as file: # updates the dictionary by dumping json data
        json.dump(dictionary, file)

    await ctx.send(f'Added a point to {name}') # bot sends a message who the point got added too

# Prints the scoreboard out
@client.command()
async def scoreboard(ctx):
    with open('tracker.json') as file:
        data = json.load(file)
    message = ''
    # Message will be the string in the format: Discord user name, score and a newline for each user
    for key, value in data.items():
        message += str(key) + ": " + str(value) + '\n'

    await ctx.send(message)

client.run(TOKEN)