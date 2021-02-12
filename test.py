
import discord
import asyncio
import os
import datetime
from discord.ext import commands
from discord.utils import get


client = discord.Client()
client = commands.Bot(command_prefix=".")


game = discord.Game("상태메세지")

@client.event
async def on_ready():
    print('Bot Online')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    bad = ['ㅅㅂ','시발','씨발','ㅇㅁ','ㄴㅇㅁ','ㅗ','ㅆㅂ','ㅗㅗ','엿멋어','니애미','ㅗㅗㅗ','ㅈㄲ']
    site = ['https','http']
    role = discord.utils.get(message.guild.roles, name = "링크")
    if message.author.bot:
        return None
   

    if message.content.startswith('!!설명'):
        
        embed = discord.Embed(title="클랜설명", description="클마:Fxxk.#6338", color=0x62c1cc,timestamp=datetime.datetime.utcnow()) #Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다   하단에 들어가는 조그마한 설명을 잡아줍니다   embed를 포함 한 채로 메시지를 전송합니다.
        embed.set_footer(text="궁금증이 해결되셨나요?? 안되셨으면 클마한테 문의 ㄱ")
        embed.add_field(name="부마", value="ZxxT4L_-#0001", inline=True)
        embed.add_field(name="매니저", value="Nxxħɍøn-_#9080", inline=True)
        embed.add_field(name="기본사항", value="저희 ADW  스배 많이합니다", inline=True)
        await message.channel.send(embed=embed)
    
    
    if message.content.startswith('!!사이트'):
        await message.channel.send("없는뎅ㅎ")
    
 
    

    if message.content.startswith('!!프사'):
        await message.channel.send(file=discord.File('클프사.png'))
        
    if message.content.startswith('!!명령어'):
        embed=discord.Embed(title='명령어 목록', description = "", color = 0xff0000, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="!!프사", value="프로필을 업로드합니다", inline=True)
        embed.add_field(name="!!사이트", value="사이트를 보여줌니다", inline=True)
        embed.add_field(name="!!내정보", value=message.author.name + "님의 이름, 서버이름, 디스코드가입일, 아이디를 보여줍니다", inline=True)
        await message.channel.send(embed=embed)

       
    if message.content.startswith('!!help'):
        embed=discord.Embed(title='명령어 목록', description = "", color = 0xff0000, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="!!프사", value="프로필을 업로드합니다", inline=True)
        embed.add_field(name="!!사이트", value="사이트를 보여줌니다", inline=True)
        embed.add_field(name="!!내정보", value=message.author.name + "님의 이름, 서버이름, 디스코드가입일, 아이디를 보여줍니다", inline=True)
        await message.channel.send(embed=embed)

        
    if message.content.startswith('횬준이바보'):
        await message.channel.send("ㅇㅈ")
    
    if message.content.startswith('!!내정보'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff0, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="디스코드가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    
    
    
    
    
    if message.content.startswith('횬준이형바보'):
        await message.channel.send("ㅇㅈ")
        
    if message.content.startswith('!!스크림'):
        await message.channel.send("https://discord.gg/wFVspUQKYJ")
        
        
    if message.content.startswith('!!횬준이의만행'):
        if message.channel.name == '💬클랜채팅방💬':
            await message.channel.send(file=discord.File('unknown.png'))
        else:
            return
        
        
    if message.content.startswith('!!ytps'):
        if message.channel.name == 'nlg유튭방':
            embed=discord.Embed(title='NLG클랜 유튭비번, 아이디', description = message.author.name + "님이 명령어를쓰심", color = 0xff0000, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="아이디:", value="nlg102938@gmail.com", inline=True)
            embed.add_field(name="비번:", value="nlgisgod!", inline=True)
            await message.channel.send(embed=embed)
            await message.delete()
        else:
            await message.channel.send("이 채널에선 실행이 불가능합니다.")
            await message.delete()

    for i in site:
        if i in message.content:
            if message.author.guild_permissions.manage_channels:
                return
            elif role in message.author.roles:
                return
            else:
                await message.delete()           
          
           
        
            
            
            
            
   

       
    

    
        
        
        
        
        
  
        
access_token = os.environ['BOT_TOKEN']
client.run(access_token)
