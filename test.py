from collections import namedtuple
import re
from discord.ext import commands
from discord.ext.commands import Bot, Context
import discord
from discord.ext.commands.converter import clean_content
from discord.ext.commands.core import bot_has_guild_permissions
import discord.utils
import os
client = discord.Client()



@client.event
async def on_message(message):
   
   if message.channel.name == "자신의닉네임쓰기":
      
      nick = message.content
      await message.author.edit(nick=nick)




access_token = os.environ['BOT_TOKEN']
client.run(access_token)
