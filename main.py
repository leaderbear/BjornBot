import os
import discord
from discord.ext import commands
from keep_alive import keep_alive
import music

cogs = [music] 

bot = commands.Bot(command_prefix="-")

for i in range(len(cogs)):
  cogs[i].setup(bot)





@bot.event
async def on_connect():
  print("Bot is online")
 




@bot.command()
async def test(ctx):
  await ctx.send("Hello")




keep_alive()
bot.run(os.environ['TOKEN'])