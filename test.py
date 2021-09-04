import discord
from discord.ext import commands
import os
import random
from discord.ext.commands.core import check
from discord_components import *
from discordTogether import DiscordTogether
client = commands.Bot(command_prefix=".")
togec = DiscordTogether(client)

@client.event
async def on_ready():
    print("ready")
    DiscordComponents(client)
    

@client.command()
async def 유튜브보기(ctx):
    await ctx.send("음성채널에 들어간뒤 아래버튼을 클릭하고 ", components
    = [Button(label = "CLICK me")])
    interaction = await client.wait_for("button_click",
    check = lambda i: i.component.label.startswith
    ("CLICK"))
    link = await togec.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"{link}")

@client.command()
async def start(ctx):
    link = await togec.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"{link}")

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
