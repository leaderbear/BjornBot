import os
import discord
import requests
import json 
import random
from keep_alive import keep_alive

# this use replit integrated data base, you will maybe have to 
# implement your own data base like postgres sql or ... 
from replit import db

client = discord.Client()

# some list of word that the bot will answer to 
sad_words = ["triste", "aled", "im done" , "help" , "im out", "not worth it", "ma tchass est ratée"]

# list of answers to random word that can be extended by users in server
starter_answers = ["away continue comme ca", "lache pa", "t'es capable"]

# this function use an api to get random quote and convert it into json
# not really useful for the bot, but can be used as an exemple for later
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

# function to uptade (add or delete msg) answers in db by user in server
def uptade_answers(answer): 
  if "answers" in db.keys():
    answers = db["answers"]
    answers.append(answer)
    db["answers"] = answers 
  else: 
    db["answers"] = [answer]

def delete_answers(index):
  answers = db["answers"]
  if len(answers) > index: 
    del answers[index]
  db["answers"] = answers


# confirms that the your bot logged in with success
@client.event
async def on_ready(): 
  print('We have logged in as {0.user}'.format(client)) 

# liste to other users messages and answers in the same channel
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  # we use message.content a lot, so let's make it simple for later
  msg = message.content

  if msg.startswith('j\'en ai marre'):
    quote = get_quote()
    await message.channel.send(quote)

  options = starter_answers
  if "answers" in db.keys():
    options = options + list(db['answers'])
  
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(options))


  if msg.startswith("3imed"): 
    await message.channel.send("tu veux dire malaise?")
  
  if msg.startswith("$ajouter"):
    userword = msg.split("$ajouter ",1)[1] # we want the word alfter the command
    uptade_answers(userword)
    await message.channel.send("Votre mot a été ajouté aux mots d'encouragements")

  if msg.startswith("$supprimer"):
    temp_answers = []
    if "answers" in db.keys():
      index = int(msg.split("$supprimer",1)[1])
      delete_answers(index)
      temp_answers = db["answers"]
    await message.channel.send(temp_answers)

  if msg.startswith("$afficher"):
    await message.channel.send(db["answers"])


# this line runs the bot , replace by your own bot token
keep_alive()
client.run(os.environ['TOKEN'])