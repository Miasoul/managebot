from collections import namedtuple
import re
from discord.ext import commands
from discord.ext.commands import Bot, Context
import discord
from discord.ext.commands.converter import clean_content
from discord.ext.commands.core import bot_has_guild_permissions
import discord.utils
import os

client = commands.Bot(command_prefix=".")

@client.command()
async def randomteam(ctx):
   print("뽑는중")
   user = random.choice(ctx.message.channel.guild.members)
   user2 = random.choice(ctx.message.channel.guild.members)
   user3 = random.choice(ctx.message.channel.guild.members)
   user4 = random.choice(ctx.message.channel.guild.members)
   user5 = random.choice(ctx.message.channel.guild.members)
   user6 = random.choice(ctx.message.channel.guild.members)
   user7 = random.choice(ctx.message.channel.guild.members)
   user8 = random.choice(ctx.message.channel.guild.members)

   embedVar = discord.Embed(title="랜덤팀", description="랜덤팀", color=0x00ff00)
   embedVar.add_field(name="주장", value=user, inline=False)
   embedVar.add_field(name="팀원", value=user2, inline=False)
   embedVar.add_field(name="팀원", value=user3, inline=False)
   embedVar.add_field(name="팀원", value=user4, inline=False)
   embedVar.add_field(name="팀2주장", value=user5, inline=False)
   embedVar.add_field(name="팀2원", value=user6, inline=False)
   embedVar.add_field(name="팀2원", value=user7, inline=False)
   embedVar.add_field(name="팀2원", value=user8, inline=False)
   
   await ctx.channel.send(embed=embedVar)









@client.event
async def on_message(message):
   
   if message.channel.name == "자신의닉네임쓰기":
      
      nick = message.content
      await message.author.edit(nick=nick)




access_token = os.environ['BOT_TOKEN']
client.run(access_token)
