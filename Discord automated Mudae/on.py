import time
from selenium import webdriver
import discord
import asyncio
import requests, re
import time
import json
import webbrowser
import pyautogui
import os
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
import emoji


PATH = "C:\Program Files (x86)\chromedriver.exe" 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(PATH, chrome_options=options) 

TOKEN_AUTH = "discord token for the account" # discord Token
client = discord.Client()
keyboard = Controller() 

def add_reaction(channelid, messageid, emoji): #function to add a reaction to a discord message 
    headers = {
    'authorization': 'Discord Token'
    }                                                       #channel id                 #message id
    r = requests.put(f'https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{emoji}/@me?location=Message', headers=headers)

channelid = 0 #defines and intalizes the variable that will be used to store the discord channelid's id

driver.get("Link to the discord Channel") ##opens the link


time.sleep(1) 
pyautogui.click(362, 526) #clicks a location on my screen where the account email goes
#couldn't figure out how to import cookies to selenium so i just had it automate keystroke simulations :(
for char in "My Acccount Email":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.1)
time.sleep(.1)
pyautogui.click(352, 614)
for char in "My Account Password":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.1)
pyautogui.click(406, 708)
time.sleep(3)






@client.event
async def on_ready():

    channel = client.get_channel(123) #creates an object for the channel where I want to roll 
    channelid = 123 #channel id of where I want to roll
    Me = None # defines and intializes a variable that will be used to determine if an element exist
    NumRolls = 8 #number of times that I want to run the loop, the number of rolls I have for the channel's instance
    Claimed = False # defines and intializes a variable that will be used to determine if I claimed a card
    
    while True:        #infinite loop
        while NumRolls != 0 and Claimed is not True: # continue to run the loop while I still have rolls AND I have not claimed a card
            
            
            pyautogui.click(443, 981) #clicks the textbox
            for char in "/wa": #simulates keystrokes
                keyboard.press(char)
                keyboard.release(char)
                time.sleep(0.12)
            time.sleep(0.6)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(0.12)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(0.6)
            
            
            messages = await channel.history(limit=1).flatten() #gets the latest message of the channel
            CheckIfMudae = messages[0].author.name #checks if the author of the most latest message if from the bot
            id = messages[0].id #gets the id of most recent message in the channel
            
            
            if CheckIfMudae == "Mudae": #if the author of the most recent message is Mudae
                if driver.find_element_by_xpath("//li[@id='chat-messages-%s']//div[@class='repliedMessage-3Z6XBG executedCommand-14-SNW']" % id): #if the most recent message has an element that is a reply
                    Me = driver.find_element_by_xpath("//li[@id='chat-messages-%s']//div[@class='repliedMessage-3Z6XBG executedCommand-14-SNW']" % id).text #gets the contents of the message that the bot replied to
                    print(Me) #prints the contents of the replied message | did this just for verifcation so I can actually see what's being stored
                    time.sleep(1)
                    if "@Anim_osity" in Me: #if the user that the bot is replying to is ME 
                        worth = driver.find_element_by_css_selector("div[id='message-accessories-%s'] strong" % id).text #finds the element that has the worth of the card and stores it within a variable
                        if driver.find_elements_by_css_selector("div[id='message-accessories-%s'] span[class='embedFooterText-2Mc7H9']" % id): #checks if card hasn't been claimed | checks if the most recent message has a footer element
                            BelongsTo = driver.find_element_by_css_selector("div[id='message-accessories-%s'] span[class='embedFooterText-2Mc7H9']" % id).text #if the card has a footer, gets the text of the footer 
                            if "Belong" in BelongsTo: #if the footer has the word "belong" then it knows that the card has been claimed which means that kakera can be reacted 
                                print ("Card has already been claimed, going for the kakera")
                                add_reaction(channelid,id,":kakeraY:") # attempts to add all of these reactions to the message, because I do not have nitro then it will only react to an emote that has already been reacted 
                                time.sleep(.1)
                                add_reaction(channelid,id,":kakeraP:")
                                time.sleep(.2)
                                add_reaction(channelid,id,":kakeraR:")
                                time.sleep(.3)
                                add_reaction(channelid,id,":kakeraL:")
                                time.sleep(.4)
                                add_reaction(channelid,id,":kakeraG:")
                            else:
                                print(worth) #prints the worth in kakera for the card
                                if int(worth) > 300: #if the worth of the card is more than 300 kakera it will react to the card so I can claim it
                                    time.sleep(1)
                                    add_reaction(channelid,id,(emoji.emojize(':thumbs_up:')))
                                    time.sleep(1)
                                    add_reaction(channelid,id,(emoji.emojize(':weary:')))
                                    Claimed = True
                                    print("Claimed!")
                                    time.sleep(10800) #becuase the bot only allows you to claim every 3 hours, it will sleep for 3 hours and then start the loop again
                                    continue
                                else:
                                    print("not worth") 
                    
                        
                        else:
                            print(worth)
                            if int(worth) > 300:
                                time.sleep(1)
                                add_reaction(channelid,id,(emoji.emojize(':thumbs_up:')))
                                time.sleep(3)
                                add_reaction(channelid,id,(emoji.emojize(':weary:')))
                                Claimed = True
                                print("Claimed!")
                                time.sleep(10800)
                                continue
                            else:
                                print("not worth")
            
                    else:
                        #if the most recent message is not from mudae, then searches the 3 most recent messages for the bot 
                        print("Not mudae, looking for the bot rn") 
                        WhereIsMudae = await channel.history(limit=3).flatten() #gets the 3 latest messages
                
                        counter = 0
                        while counter != 3: #checks the 3 most recent messages for where the bot is 
                             CheckIfMudae = WhereIsMudae[counter].author.name
                             if CheckIfMudae == "Mudae": 
                                 print("Found mudae on the " + str(counter) + " most recent message")
                                 Found = WhereIsMudae[counter].id
                                 counter = 3
                                 
                                
                                 Me = driver.find_element_by_xpath("//li[@id='chat-messages-%s']//div[@class='repliedMessage-3Z6XBG executedCommand-14-SNW']" % id).text ##clciks the the comfirm button
                                 print(Me)
                                 time.sleep(1)
                                 if "@Anim_osity" in Me:
                                     worth = driver.find_element_by_css_selector("div[id='message-accessories-%s'] strong" % id).text
                                     if driver.find_elements_by_css_selector("div[id='message-accessories-%s'] span[class='embedFooterText-2Mc7H9']" % id): #checks if card hasn't been claimed
                                         print ("Card has already been claimed, going for the kakera")
                                         add_reaction(channelid,id,":kakeraY:")
                                         time.sleep(.1)
                                         add_reaction(channelid,id,":kakeraP:")
                                         time.sleep(.2)
                                         add_reaction(channelid,id,":kakeraR:")
                                         time.sleep(.3)
                                         add_reaction(channelid,id,":kakeraL:")
                                         time.sleep(.4)
                                         add_reaction(channelid,id,":kakeraG:")
                                 
                                     
                                     else:
                                         print(worth)
                                         if int(worth) > 300:
                                             time.sleep(.6)
                                             add_reaction(channelid,id,(emoji.emojize(':thumbs_up:')))
                                             Claimed = True
                                             print("Claimed!")
                                             time.sleep(10800)
                                             continue
                                         else:
                                             print("not worth")
                                
                                 
                                 
                                 
                                 
                             else:
                                counter+=1
                        
                        
                        
                        
                        
                        
                
            
            
            
            
            
                else:
                    print("Not mudae, looking for the bot rn")
                    WhereIsMudae = await channel.history(limit=3).flatten() #gets the latest message
            
                    counter = 0
                    while counter != 3:
                         CheckIfMudae = WhereIsMudae[counter].author.name
                         if CheckIfMudae == "Mudae":
                             print("Found mudae on the " + str(counter) + " most recent message")
                             Found = WhereIsMudae[counter].id
                             counter = 3
                             
                            
                             Me = driver.find_element_by_xpath("//li[@id='chat-messages-%s']//div[@class='repliedMessage-3Z6XBG executedCommand-14-SNW']" % Found).text ##clciks the the comfirm button
                             print(Me)
                             time.sleep(1)
                             if "@Anim_osity" in Me:
                                 worth = driver.find_element_by_css_selector("div[id='message-accessories-%s'] strong" % Found).text
                                 if driver.find_elements_by_css_selector("div[id='message-accessories-%s'] span[class='embedFooterText-2Mc7H9']" % Found): #checks if card hasn't been claimed
                                     print ("Card has already been claimed, going for the kakera")
                                     add_reaction(channelid,id,":kakeraY:")
                                     time.sleep(.1)
                                     add_reaction(channelid,id,":kakeraP:")
                                     time.sleep(.2)
                                     add_reaction(channelid,id,":kakeraR:")
                                     time.sleep(.3)
                                     add_reaction(channelid,id,":kakeraL:")
                                     time.sleep(.4)
                                     add_reaction(channelid,id,":kakeraG:")
                             
                                 
                                 else:
                                     print(worth)
                                     if int(worth) > 300:
                                         time.sleep(1)
                                         add_reaction(channelid,id,(emoji.emojize(':thumbs_up:')))
                                         time.sleep(3)
                                         add_reaction(channelid,id,(emoji.emojize(':weary:')))
                                         Claimed = True
                                         print("Claimed!")
                                         time.sleep(10800)
                                         continue
                                     else:
                                         print("not worth")
                            
                             
                             
                             
                             
                         else:
                            counter+=1
                    
                    
                    
                    
                   
            else:
                print("Not mudae, looking for the bot rn")
                WhereIsMudae = await channel.history(limit=3).flatten() #gets the latest message

                counter = 0
                while counter != 3:
                     CheckIfMudae = WhereIsMudae[counter].author.name
                     if CheckIfMudae == "Mudae":
                         print("Found mudae on the " + str(counter) + " most recent message")
                         Found = WhereIsMudae[counter].id
                         counter = 3
                         
                        
                         Me = driver.find_element_by_xpath("//li[@id='chat-messages-%s']//div[@class='repliedMessage-3Z6XBG executedCommand-14-SNW']" % Found).text ##clciks the the comfirm button
                         print(Me)
                         time.sleep(1)
                         worth = driver.find_element_by_css_selector("div[id='message-accessories-%s'] strong" % Found).text
                         print(worth)
                         if int(worth) > 40:
                            add_reaction(channelid,Found,(emoji.emojize(':thumbs_up:')))
                         else:
                            print("not worth")
                        
                         
                         
                         
                         
                     else:
                        counter+=1
            NumRolls-=1
            time.sleep(.5)
    if NumRolls == 0:
        print("No good rolls :(") #if the rolls run out then waits an hour to restart the loop
        time.sleep(3600)
        
    
    
client.run(TOKEN_AUTH, bot=False)
