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
async def mute(ctx, member: discord.Member):
     if ctx.message.author.guild_permissions.administrator:
        
        mutedRole = discord.utils.get(member.guild.roles, name='뮤트')
        defRole = discord.utils.get(member.guild.roles, name ='Normal')
        await member.add_roles(mutedRole)
        await member.remove_roles(defRole)
        
        embed=discord.Embed(title="뮤트성공", description="**{0}** 이가  **{1}** 에게 뮤트 당했습니다!".format(member, ctx.message.author), color=0xff00f6)
        await ctx.send(embed=embed)
        
     else:
        embed=discord.Embed(title="권한거부", description="너 권한 없는뎅??", color=0xff00f6)
        await ctx.send(embed=embed)

@client.command()
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.guild_permissions.administrator:
        
        mutedRole = discord.utils.get(member.guild.roles, name='뮤트')
        defRole = discord.utils.get(member.guild.roles, name ='Normal')
        await member.add_roles(defRole)
        await member.remove_roles(mutedRole)
        
        embed=discord.Embed(title="언뮤트성공", description="**{1}** 이가  **{0}** 을 언뮤트 했습니다!".format(member, ctx.message.author), color=0xff00f6)
        await ctx.send(embed=embed)
        
     else:
        embed=discord.Embed(title="권한거부", description="너 권한 없는뎅??", color=0xff00f6)
        await ctx.send(embed=embed)

@client.event
async def on_message(message):
   if message.channel.id == '873829277752242196':
      nick = message.content
      await message.author.edit(nick=nick)




access_token = os.environ['BOT_TOKEN']
client.run(access_token)
