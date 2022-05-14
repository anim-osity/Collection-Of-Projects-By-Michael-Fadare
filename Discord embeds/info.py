import discord
from dhooks import Webhook, Embed
import requests
import json
import re
import time
import google


hook = Webhook("discord webhook link")


embed1 = Embed(color=0x2F3136)
embed1.set_image(url="https://cdn.discordapp.com/attachments/883067094466437134/887502791290003466/abstrakt_channel_00000.jpg")
hook.send(embed=embed1)

embed = Embed(color=0x2F3136)
embed.set_author(name="Contacts", icon_url = "https://emoji.gg/assets/emoji/8694-wow.gif")
embed.add_field(name='⠀', value = "**Leader:** <@696018222465548298>", inline=False) #<@&696018222465548298)>
embed.add_field(name='⠀', value = "**Co-Leaders:** <@337220957137666049> & <@719853058846359632>", inline= False)
embed.set_thumbnail(url="https://i.imgur.com/5Ho0Qf1.png")
#embed.set_image(url='https://i.postimg.cc/6prrY8z5/gg4ca72c757a.gif') gif line
embed.set_footer(text = "Message these people for any questions⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
hook.send(embed=embed)

embed2 = Embed(color=0x2F3136)
embed2.set_author(name= "Channels", icon_url = "https://emoji.gg/assets/emoji/8694-wow.gif")
embed2.add_field(name='.', value = '''
> <#888797331116400690>
> Discord info + rules + rewards
''', inline= False)
embed2.add_field(name='.', value = '''
> <#887888308158464010>
> Rewards for boosting server
''', inline= False)
embed2.add_field(name='.', value = '''
> <#881364512899477605>
> Support the ABK Community
''', inline= False)
embed2.add_field(name='.', value = '''
> <#881364627651444797>
> Info for abstrakt applications
''', inline= False)
embed2.add_field(name='.', value = '''
> <#890715211575754772>
> Upcoming contest info: Monthly editing tournaments
''', inline= False)

embed2.set_image(url='https://i.postimg.cc/6prrY8z5/gg4ca72c757a.gif')
hook.send(embed=embed2)

embed3 = Embed(color=0x2F3136)
embed3.set_author(name="Links", icon_url = "https://emoji.gg/assets/emoji/8694-wow.gif" )
embed3.add_field(name= "__Instagram__⠀⠀⠀⠀⠀⠀⠀⠀⠀", value = "[Click](https://www.instagram.com/abstrakt_page/)", inline= True)
embed3.add_field(name= "__Youtube__⠀⠀⠀⠀⠀⠀⠀⠀⠀", value = "[Click](https://www.youtube.com/channel/UCx1ic5kl2WOb5klhyxuLQsQ)", inline= True)
embed3.add_field(name= "__ABK Links__⠀⠀⠀⠀⠀", value = "[Click](https://lynkfire.com/abstrakt)", inline= True)
embed3.add_field(name= "__Applications__⠀", value = "[Click](https://docs.google.com/forms/d/e/1FAIpQLSeBr5dfh4fWIWmPG00hg_z0sVyHs--UWVCWwIYcF1Z6IdQF0Q/viewform)", inline= True)
embed3.add_field(name= "__Discord__", value = "[Copy](https://discord.gg/4BabsK7XpA)", inline= True)
embed3.add_field(name= "__Tiktok__", value = "[Click](https://vm.tiktok.com/ZMRBuaYLf/)", inline= True)
#embed3.set_image(url='https://i.postimg.cc/6prrY8z5/gg4ca72c757a.gif') gif line
hook.send(embed=embed3)
