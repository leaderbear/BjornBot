import os
import discord
from discord.ext import commands
from keep_alive import keep_alive
import music


bot = commands.Bot(command_prefix="-")

cogs = [music] 
for i in range(len(cogs)):
  cogs[i].setup(bot)

@bot.event
async def on_ready():
  print("Bot is online")
  await bot.change_presence(activity=discord.Game("Try -aled"))
 
@bot.command()
async def aled(ctx):
  await ctx.send(f"{ctx.author.mention} Je suis en bêta, bientôt! :hourglass:")


@bot.command() 
async def ping(ctx):
  await ctx.send(f'**Pong!** {round(bot.latency * 1000)}ms')


keep_alive()
bot.run(os.environ['TOKEN'])