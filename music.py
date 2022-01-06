import discord
from discord.ext import commands
import youtube_dl 

class music(commands.Cog):
  def __init__(self, client):
    self.client = client 


  @commands.command()
  async def disconnect(self,ctx):
    await ctx.voice_client.disconnect()


  @commands.command()
  async def play(self,ctx,url):

    if ctx.author.voice is None: 
     await ctx.send(f"{ctx.author.mention} rejoins d'abord un vocal :smirk:")

    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()

      ctx.voice_client.stop()
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
      YDL_OPTIONS={'format':"bestaudio"}  
      vc = ctx.voice_client 

      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)
    else:
      await ctx.voice_client.move_to(voice_channel)


  @commands.command()
  async def pause(self,ctx):
    await ctx.voice_client.pause() 
    await ctx.send("Musique en pause :pause_button:")

  @commands.command()
  async def resume(self,ctx):
    await ctx.voice_client.resume() 
    await ctx.send("Musique résumée :arrow_forward:")

  @commands.command()
  async def leave(self,ctx):
    await ctx.voice_client.disconnect()
    await ctx.send("Bye :vulcan:")


# TODO : Queue , resume , remove 

def setup(client):
  client.add_cog(music(client))  