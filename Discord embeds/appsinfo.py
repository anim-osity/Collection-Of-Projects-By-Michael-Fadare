import discord
from dhooks import Webhook, Embed
import requests
import json
import re
import time
import google


hook = Webhook("discord webhook link")

embed1 = Embed(color=0x2F3136)
embed1.set_image(url="https://cdn.discordapp.com/attachments/888105050038226944/889313257054154813/apps_info_00000.jpg")
hook.send(embed=embed1)

embed = Embed(color=0x2F3136)

embed.set_author(name="How to Apply")
embed.add_field(name='''1. submit your best work to:
    ⠀''', value='[FORM](https://docs.google.com/forms/d/e/1FAIpQLSeBr5dfh4fWIWmPG00hg_z0sVyHs--UWVCWwIYcF1Z6IdQF0Q/viewform)', inline=False)
embed.add_field(name='⠀', value= "**2. check <#881364885185916979> channel for your verdict**", inline=False)
embed.add_field(name='⠀', value= "**3. Judges will mark you with one of the following:**", inline=False)
embed.add_field(name='⠀', value= '''> ``Accept`` - You have been accepted as an ABK member <a:verifyblack:889723943173390418>
>  
> ``Trial`` - You have one month to make and edit to prove your 
> apptitude & ability to improve
>  
> ***Warning:***  If you are not able to prove this you may be subjected 
> .decline
>  
> ``Reapp`` - Your edits are decent but may lack complexity or
> understanding of certain concepts, you may use our tutorials 
> and assets to help you get better, then Re-apply when you are 
> ready
>  
> ``Decline`` - Your Application is declined. Edit lacks all forms of 
> understanding of editing in general, you may not re-apply

 **Application Rules**: 
  
> •  Edit must be longer than 10 seconds
> 
> •  No scraps, raw, remakes, collabs, or low quality edits
> 
> •  All edits must me your own
> 
> •  Must be in the abstrakt discord server to apply
> 

   *Those who submit stolen edits  will be banned without warning*

''', inline=False)


embed.set_footer("*If you have any further questions dm the Lead / Co-Leads / Admins / Mods*")


hook.send(embed=embed)
