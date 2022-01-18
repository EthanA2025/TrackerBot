import discord
from discord.ext import commands
from discord.ext.commands import MemberConverter
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

'''
The on_ready() function tells when the bot has logged into discord
'''
@client.event
async def on_ready():
    print(f'Bot has logged in')

'''
The add command allows for the addition to a point on the scoreboard to a certain user
'''
@client.command(aliases=['Add', 'add'])
async def _add(ctx, name: discord.User):
    with open('tracker.json', 'r') as file: # Adds to the dictionary, the dictionary at that user increases by one simulating a point increase
        dictionary = json.load(file)
        dictionary[str(name.id)] += 1 

    with open("tracker.json", 'w') as file: # updates the dictionary by dumping json data
        json.dump(dictionary, file)

    await ctx.send(f'Added a point to {name}') # bot sends a message who the point got added too


'''
The remove command allows for the addition to a point on the scoreboard to a certain user
'''
@client.command(aliases=['Remove', 'remove'])
async def _remove(ctx, name: discord.User):
    with open('tracker.json', 'r') as file: # Adds to the dictionary, the dictionary at that user increases by one simulating a point increase
        dictionary = json.load(file)
        if dictionary[str(name.id)] < 1:
            await ctx.send("User cannot have negative points")
        else:
            dictionary[str(name.id)] -= 1 
            await ctx.send(f'Removed a point from {name}')

    with open("tracker.json", 'w') as file: # updates the dictionary by dumping json data
        json.dump(dictionary, file)

'''
The scoreboard command allows for users to print out the scoreboard by 
checking the data inside of it that comes from the json.
'''
@client.command()
async def scoreboard(ctx):
    converter = MemberConverter()
    with open('tracker.json') as file:
        data = json.load(file)
    message = ''
    # Message will be the string in the format: Discord user name, score and a newline for each user
    for key, value in data.items():
        member = await converter.convert(ctx, key) # Converts ID into a user as a string
        message += str(member) + ": " + str(value) + '\n'

    await ctx.send(message)

client.run(TOKEN)
