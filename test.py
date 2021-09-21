from collections import namedtuple
import re
from discord.ext import commands
from discord.ext.commands import Bot, Context
import discord
from discord.ext.commands.converter import clean_content
from discord.ext.commands.core import bot_has_guild_permissions
import discord.utils
import os
from discord.ext.commands import has_permissions
client = commands.Bot(command_prefix=".")










@client.command(pass_context=True)

async def 강변(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    
  
@client.command()
async def random_members(ctx):
    guild = ctx.guild # you can also use bot.get_guild(guild_id)
    # role = guild.get_role('889691235713945672')
    # members = role.members
    # I'm using `random.sample` so I don't get any duplicates
    random_members = random.choice(ctx.message.channel.guild.members)

    await ctx.send(f'Members picked: `{random_members}`')
    



@client.event
async def on_message(message):
   
   if message.channel.name == "자신의닉네임쓰기":
      
      nick = message.content
      await message.author.edit(nick=nick)


access_token = os.environ['BOT_TOKEN']
client.run(access_token)
