import os
import discord
import requests
import json 

client = discord.Client()

# this function use an api to get random quote and convert it into json
# not really useful for the bot, but can be used as an exemple for later
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

# confirms that the your bot logged in with success
@client.event
async def on_ready(): 
  print('We have logged in as {0.user}'.format(client)) 

# liste to other users messages and answers in the same channel
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('j\'en ai marre'):
    quote = get_quote()
    await message.channel.send(quote)


# this line runs the bot , replace by your own bot token
client.run(os.environ['TOKEN'])