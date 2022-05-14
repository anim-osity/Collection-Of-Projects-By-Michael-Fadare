import discord
from dhooks import Webhook, Embed
import requests
import json
import re
import time
import google


hook = Webhook("discord Webhook")


embed = Embed(color=0x2F3136)
embed1 = Embed(color=0x2F3136)
embed2 = Embed(color=0x2F3136)
embed1.set_image(url="https://cdn.discordapp.com/attachments/888059320468635718/888102631661273098/pink_00000.jpg")
hook.send(embed=embed1)

embed.set_author(name = "Nitro Rewards", icon_url = "https://emoji.gg/assets/emoji/8694-wow.gif")
embed.add_field(name='''
    ⠀''', value='There are **2** boost LVLs:', inline = False)
embed.add_field(name='⠀', value= '''
**__Tier 1 Boost:__** *Premium*
**1x: <a:nitrogem:888996173015318540> <@&900819807081996328> :** premium role + profile customization + access
to vip channels + Limited Edition Project Files
⠀
**__Tier 2 Boost:__** *Upgrade*
**2x: <a:nitrogem:888996173015318540> <@&890095445362237492> :** Tier 1 access + Member project files 
+ **ALL** Abstrakt editing packs + 1 on 1 editing tutorial on 
topics of your choice & ALL BENEFITS LISTED BELOW.

''', inline=False)
hook.send(embed=embed)

embed2.add_field(name='⠀', value= "**Premium + Upgrade Includes:**", inline=False)
#embed.add_field(name='⠀', value= "⠀", inline=False)
embed2.add_field(name='⠀', value= '''
> • ABK editing packs
> • PNG Textures & Overlays
> • CC + MBL.ffx presets
> • AE Transition Presets
> • [Member] Project files
> • [Private] Project files
> • 3D models + modeling packs
> • PBR texture presets & pro shaders
> • Cinematography software & exclusive plugins
> • Cinematic LUTs (pro cc)
> • AE scripts & Adobe add-on software


''', inline=False)
embed2.add_field(name='⠀', value= "*Thinking about boosting? Contact <@&883073455652749373> for any questions.*⠀⠀", inline=False)









hook.send(embed=embed2)
