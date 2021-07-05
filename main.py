import os
import discord

client = discord.Client()

@client.event
async def on_ready(): 
  print('We have logged in as {0.user}'.format(client)) 

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startwith('$hello'):
    await message.channel.send("hello toi-même")


# this line runs the bot  
client.run(os.environ['TOKEN'])