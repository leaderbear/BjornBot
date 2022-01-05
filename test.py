import os
import discord
from discord.ext import commands, tasks
import music
import requests
import json 
from random import choice
import youtube_dl
from keep_alive import keep_alive

# this use replit integrated data base, you will maybe have to 
# implement your own data base like postgres sql or ... 
#from replit import db

cogs = [music] 

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix = '-')#, intents=intents)

#client = commands.Bot(command_prefix='#', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


@client.command() 
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


states = ['123 viva Algérie', 'Benab is the best', 'No more lil poop', 'honorer 3imed', 'Valorant', 'Dota 2', 'Making Gundam', 'Pizza New York', 'Leviosa', 'Minecraft', "Project zomboid", "League of Legends", "See Nayato in Youtube"] 


# confirms that the your bot logged in with success
@client.event
async def on_ready():
  change_status.start()
  print('We have logged in as {0.user}'.format(client)) 


# liste to other users messages and answers in the same channel
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  # we use message.content a lot, so let's make it simple for later
  msg = message.content

  if msg.startswith("3imed"): 
    await message.channel.send("tu veux dire malaise?")

  if msg.startswith("idir"): 
    await message.channel.send("Idir aime Benab")  
    
@client.command(name='nextstatus', help='This command skips the bot status')
async def skip():
  await change_status()

# switch bot status every 10 minuts   
@tasks.loop(seconds=600)
async def change_status():
  await client.change_presence(activity=discord.Game(choice(states)))


# runs the bot and keep it online , replace by your own bot token
keep_alive()
client.run(os.environ['TOKEN'])




