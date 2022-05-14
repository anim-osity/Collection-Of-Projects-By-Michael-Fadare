import discord
import asyncio
import requests, re
import time
import json
import webbrowser
import pyautogui
import os
import socket



TOKEN_AUTH = "Discord Token" # discord Token
client = discord.Client()
ID = 123 #id of the channel 
messages = ""
percentage = 0
price = 0
name = ""
link = ""
CheckLink = ["hi"] #array used to check if the link is the same every second

cookie = 'Roblox account Cookie'
auth_response = requests.post("https://auth.roblox.com/v1/logout", headers = {"cookie": f".ROBLOSECURITY={cookie}"}) #checks the response of the request
token = None

#checks if the cookie is valid and can be used
if auth_response.status_code == 403:
    if "x-csrf-token" in auth_response.headers:
        token = auth_response.headers["x-csrf-token"]
        print("Token authorized") 

headers = {
"cookie": f".ROBLOSECURITY={cookie}",
"x-csrf-token": token
}




def find_all(a_str, sub): #function to find all the occurances of a character in a string
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) 





@client.event
async def on_ready():
    counter = 0 #to check if the link is not the same as the last link
    HowLong = 0 #counter for elasped time
    while True: #infinite loop
        
        #sometimes my dad would block my pc from using the wifi by mac address so this was a way to bypass that for whenever it happens
        IPaddress=socket.gethostbyname(socket.gethostname())
        if IPaddress=="127.0.0.1":
            print("Attempting to reconnect")
            os.system('spoof-mac.py randomize wi-fi')
            time.sleep(10)
        
    
        channel = client.get_channel(123) # gets the channel of the deals bot
        messages = await channel.history(limit=1).flatten() #gets the latest message
        for i in messages:
            Real = i.content #gets the contents of the message
            # print(Real)

        placements = (list(find_all(Real, '|'))) # finds all the occurances of | within the latest message of the channel

        percentage = Real[placements[0]+2:placements[1]-2] #gets the percentage of the item
        price = Real[placements[1]+2:placements[2]-1] #gets the price of the item
        name = Real[placements[2]+2:placements[3]-1] #gets the name of the item
        link = Real[placements[3]+3:len(Real)-1] #gets the link to the item
        price = int(price) # converts the string of the price to an int
        percentage = int(percentage) # converts the string of the percentage to an int
        
        Findd = (list(find_all(link, '/'))) #within the link, finds all occurances of the /
        ID = int(link[Findd[3]+1:Findd[4]]) #gets the ID of the item from the link
        CheckLink.append(link) 
        counter += 1
        
        #list of items that I DO NOT WANT TO BUY
        Blacklisted = ["https://www.roblox.com/catalog/6807134749/Gucci-Geometric-Bag", "https://www.roblox.com/catalog/321570512/Chill-Cap", "https://www.roblox.com/catalog/8769448867/Vans-x-The-North-Face-Helmet", "https://www.roblox.com/catalog/44113968/Kuddle-E-Koala", "https://www.roblox.com/catalog/27345567/Fiery-Egg-of-Egg-Testing", "https://www.roblox.com/catalog/6803423284/Gucci-Headband", "https://www.roblox.com/catalog/20573078/Shaggy", "https://www.roblox.com/catalog/6815676017/Gucci-Feather-and-Crystals-Headpiece", "https://www.roblox.com/catalog/8763364938/Super-Bowl-LVI-Crown", "https://www.roblox.com/catalog/8853111709/Gucci-Glam-Rock-Shoulder-Pads-x-Achille-Lauro-30", "https://www.roblox.com/catalog/6807133411/Gucci-Horsebit-1955-Shoulder-Bag", "https://www.roblox.com/catalog/8194165059/Ralph-Lauren-Snow-Beach-Backpack", "https://www.roblox.com/catalog/24826683/Egg-of-Equinox-Night", "https://www.roblox.com/catalog/1533893/Bluesteel-Egg-of-Genius", "https://www.roblox.com/catalog/7212280564/Sequined-Boxing-Mask-KSI", "https://www.roblox.com/catalog/24826737/POW!-To-the-Moon!-Egg", "https://www.roblox.com/catalog/74174927/Panda-Knit", "https://www.roblox.com/catalog/2830432345/Ornate-Creature-Horns", " https://www.roblox.com/catalog/2830416348/Ivory-Bloom-Pauldrons", "https://www.roblox.com/catalog/2830411358/Crimson-Bloom-Pauldrons", "https://www.roblox.com/catalog/244160118/Purple-Steampunk-Robin-Hood", " https://www.roblox.com/catalog/1974901902/Aqua-Emperor-Of-The-Sky", "https://www.roblox.com/catalog/2620416387/Noob-Assist-Gingerbread-Gratitude", "https://www.roblox.com/catalog/24832618/Red-Fabergé-Egg", "https://www.roblox.com/catalog/1744071203/The-Locksmiths-Secret", "https://www.roblox.com/catalog/98421766/Turkey-Tie-2012", "https://www.roblox.com/catalog/1532381/Blinking-Egg-of-Relocation", "https://www.roblox.com/catalog/7592004548/Vans-Checkerboard-Bucket-Hat", "https://www.roblox.com/catalog/493496072/Snakepack", "https://www.roblox.com/catalog/1744198126/Casual-Sunglasses-Pocket", "https://www.roblox.com/catalog/6803395856/Gucci-Guitar-Case", "https://www.roblox.com/catalog/63239668/Bat-Tie", "https://www.roblox.com/catalog/24826725/Scenic-Egg-of-the-Clouds", "https://www.roblox.com/catalog/1117744489/Dangerous-Eye-Patch", "https://www.roblox.com/catalog/1533893/Bluesteel-Egg-of-Genius", "https://www.roblox.com/catalog/8769478056/Vans-x-The-North-Face-Snowboard", "https://www.roblox.com/catalog/102631707/Eggrachnophobia", "https://www.roblox.com/catalog/24830979/Blue-Fabergé-Egg", "https://www.roblox.com/catalog/76692101/Charles-Babbage-Fabergé-Egg", "https://www.roblox.com/catalog/5785985/Rusty-Tetramino-of-Competence", "https://www.roblox.com/catalog/331486631/Portrait-of-a-Hero-in-ROBLOX", "https://www.roblox.com/catalog/7212291640/Royal-Crown-KSI", "https://www.roblox.com/catalog/8769448867/Vans-x-The-North-Face-Helmet", "https://www.roblox.com/catalog/24826704/Radioactive-Egg-of-Undead-Apocalypse", "https://www.roblox.com/catalog/20064349/2010-Fireworks", "https://www.roblox.com/catalog/24826640/Chrome-Egg-of-Speeding-Bullet", "https://www.roblox.com/catalog/9527968627/NFL-Draft-Chain", "https://www.roblox.com/catalog/6807135859/Gucci-Spiked-Basketball-Bag", "https://www.roblox.com/catalog/6803412842/Gucci-Diamond-Framed-Sunglasses", "https://www.roblox.com/catalog/8785294898/Los-Angeles-Rams-Super-Bowl-LVI-Helmet", "https://www.roblox.com/catalog/6807139994/GucciGhost-Bag", "https://www.roblox.com/catalog/6803410579/Gucci-Wide-Brim-Felt-Hat", "https://www.roblox.com/catalog/8853117992/Gucci-Queen-Elizabeth-Gorget-x-Achille-Lauro-1-0", "https://www.roblox.com/catalog/6803403781/Gucci-GG-Marmont-Bag", "https://www.roblox.com/catalog/8785277745/Cincinnati-Bengals-Super-Bowl-LVI-Helmet", "https://www.roblox.com/catalog/6803407328/Gucci-Bloom-Perfume", "https://www.roblox.com/catalog/6803405665/Gucci-Dionysus-Bag", "https://www.roblox.com/catalog/7592026396/Vans-Checkerboard-Era-Necklace", "https://www.roblox.com/catalog/7212273948/Boxing-Gloves-KSI", "https://www.roblox.com/catalog/24826640/Chrome-Egg-of-Speeding-Bullet", "https://www.roblox.com/catalog/8274214179/NFL-Wilson-Golden-Football-Head", "https://www.roblox.com/catalog/152980562/Elegant-Faberg-Egg-of-Fancy-Times", "https://www.roblox.com/catalog/24826725/Scenic-Egg-of-the-Clouds", "https://www.roblox.com/catalog/24826853/Vicious-Egg-of-Singularity", "https://www.roblox.com/catalog/102614621/Dreamweaver-Faberg-Egg", "https://www.roblox.com/catalog/76692101/Charles-Babbage-Faberg-Egg", "https://www.roblox.com/catalog/493496072/Snakepack"]
        
        
        if CheckLink[counter] != CheckLink[counter -1] and link not in Blacklisted: #if the previous link is not the same as the previous | this was done to prevent trying to buy the same item multiple times
                
            
            
            
            if percentage >= 39 and price < 3000: #if the deal is greater or equal to 34% the script attempts to buy it
                
                url = link #sets the url that will be opened in chrome as the link to the item
                chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe' #path of chrome in my C drive's directory
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path)) 
                webbrowser.get('chrome').open_new_tab(url) #opens up chrome with the link
                
                
                
                #purchasing the item through simulated clicks
                time.sleep(1.5)
                pyautogui.click(1310, 260)
                time.sleep(.1)
                pyautogui.click(654, 580)
                time.sleep(3)
                os.system("taskkill /im chrome.exe")
                InventoryCheck = requests.get("https://avatar.roblox.com/v1/recent-items/All/list", headers = headers)
                Inventoryy = InventoryCheck.text
                
                #checks if the item that was attempted to be purchases is actually in my inventory, and if it is then it will send a message in a discord server that the item was brought
                if Inventoryy.find(str(ID)) != -1:
                    print("Item purchased!")
                    Alert = client.get_channel(123)
                    await Alert.send("Item purchased!        Price: " + str(price) + " Item: " + name + " Link: " + link)
                else:
                    os.system("taskkill /im chrome.exe")
            

        time.sleep(1.1)
        HowLong+=1 
        
        
                    


client.run(TOKEN_AUTH, bot=False)
