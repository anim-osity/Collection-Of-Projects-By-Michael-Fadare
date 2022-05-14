import random
import discord
from dhooks import Webhook, Embed
import requests
import json
import re
import time
import google

# Must enable INTENTS in the discord developer portal and have this added to access the memebership of the server 
client = discord.Client()
intents = discord.Intents.default() 
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_member_join(member):
    random_number = random.randint(0, 6) #randomly generates a number between 1-7
    ListOfHooks = ["", "", "", "", "","", ""]
    #Colors associated with the webhooks in order: Green, blue, magenta, orange, purple, red, whiteish, yellow
    Hoook = ListOfHooks[random_number] #picks a random webhook from the list of webhooks
    
    ListOfImages = ["https://cdn.discordapp.com/attachments/889319712293523476/889323545858023424/ABK_Logo_00000.png", "https://cdn.discordapp.com/attachments/889319712293523476/889322395645653023/4_00000.png",
    "https://cdn.discordapp.com/attachments/889319712293523476/889323025604956180/6_00000.png", "https://cdn.discordapp.com/attachments/889319712293523476/889323202122252368/7_00000.png",
    "https://cdn.discordapp.com/attachments/889319712293523476/889323835277586472/ABK_Logo_00000.png",
    "https://cdn.discordapp.com/attachments/889319712293523476/889324817432596510/ABK_Logo_00000.png", "https://cdn.discordapp.com/attachments/889319712293523476/890413103748087838/ABK_Logo_00000.png"]
    
    EmbedColors = [0x3CD822,0x16B3FB, 0xFD0B7E, 0xFB5812, 0xFB1011, 0xC0F4FF, 0xFBFF00]
    
    
    
    general_channel = client.get_channel(123)
    
    
    testtz = member.mention 
    Welcomee = "Hello %s!" % testtz #mentions / pings the user that just joined
    
    hook = Webhook(Hoook)
    embed = Embed(color=EmbedColors[random_number]) #makes the embed color one of the random embed hexnumbers
    
    embed.set_author(name="Abstrakt", icon_url= ListOfImages[random_number])
    embed.add_field(name="⠀", value = Welcomee)
    embed.add_field(name="**Welcome to abstrakt**", value = '''
    > - Read <#881364376483938365> for General team information
    > - Please read <#888797331116400690> for server info + rules
    > - React to get roles in <#889236950576427018>
    ''', inline= False)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/883068795877490688/886766650798534666/ABK-LOGO2.gif")

    hook.send(embed=embed)

@client.event
async def on_message(message):
    if "MessageType.premium_guild" in str(message.type): #if the user just joined the server
        general_channel = client.get_channel(123)
        
        booster = message.author
        
        hook = Webhook("https://discord.com/api/webhooks/907453738560679966/EDEv6OU2bZeS1kL3wCHFz6IQu-f3r0nue41e_FcIIaqg5nYIkdNs7bDTyK2LrW32p6ze")
        embed = Embed(color=0xF209E5)
        embed.set_author(name="Abstrakt", icon_url= "https://cdn.discordapp.com/attachments/889319712293523476/889322696217878558/5_00000.png")
        embed.add_field(name="⠀", value = "Thank you %s for boosting the server!" % booster) 
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/883068795877490688/886766650798534666/ABK-LOGO2.gif")
    
        hook.send(embed=embed)

















client.run('Discord bot Token')
