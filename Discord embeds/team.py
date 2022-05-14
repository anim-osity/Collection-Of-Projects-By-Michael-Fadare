import discord
from dhooks import Webhook, Embed
import requests
import json
import re
import time
import google


hook = Webhook("Discord Web Hook")



embed1 = Embed(color=0x2F3136)
embed1.set_image(url="https://cdn.discordapp.com/attachments/888158123599224863/888158302385602610/light_blue_00000.jpg")
hook.send(embed=embed1)

embed = Embed(color=0x2F3136)
embed.set_author(name="Links")
embed.add_field(name= "__ABK Logo__⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", value = "[use the logo in you edits](https://drive.google.com/drive/folders/1sUZo-9Gx1ZEnMRstpX0M-I8aj2mEmwOh?usp=sharing)", inline= True)
embed.add_field(name= "__Youtube Drive__⠀⠀ ⠀⠀⠀⠀⠀⠀⠀ ", value = "[Edits for the *youtube* page](https://rebrand.ly/youtube-edits)", inline= True)
embed.add_field(name= "__Instagram Drive__", value = "[Edits for the *instagram* page](https://rebrand.ly/instagram-edits)", inline= False)
hook.send(embed=embed)

embed2 = Embed(color=0x2F3136)
embed2.add_field(name="<a:wowgem:889731678644359168> Regulations:", value = '''
⠀
**1.** You must make atleast one edit a month to stay part of the team 
 ⠀ 
**2.** Be respectful to your fellow members

**3.** You hereby fall under the jurisdiction of the Abstrakt team guidlines,
 you may use our editing packs and project files to develop 
 your editing techniques. 
 
 **However, Please Note:** The privileges that are given can be taken 
 away, failure to comply to the rules may be deemed excommunicado
 and will no longer be able to continue their services 
 as a member of Abstrakt.
 
**4.** We will be doing monthly re-evaluation of each member 
in order to ensure productivity. (information listed below)


''', inline = False)
hook.send(embed=embed2)


embed3 = Embed(color=0x2F3136)
embed3.add_field(name="<a:wowgem:889731678644359168> Monthly Re-evaluation:⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", value = '''
Each member is subject to a re-evaluation of their ability levels each⠀⠀
month. The terms will be based on your:
''', inline = False)
embed3.add_field(name='⠀', value= ''' 
> - Activity status
> - Best edit pertaining to the month
> - Integration onto the team & intereactions with other members
''', inline = False)
embed3.add_field(name= "⠀", value = "*If you have any questions, please contact administration*")

hook.send(embed=embed3)
