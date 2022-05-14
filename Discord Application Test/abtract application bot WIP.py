import discord
from dhooks import Webhook, Embed
import requests
import json
import re
import time
import google
import os
from apscheduler.schedulers.background import BlockingScheduler

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account

import github
from github import Github
from github import InputGitTreeElement
from git import Repo

token = '' #token for the github repo
g = Github(token)
repo = g.get_user().get_repo('Test') 
contents = repo.get_contents("Links.txt")

RawData = requests.get('link to the repo that will be edited')
Raw = RawData.text

hook = Webhook("discord webhook")

ccounter = 2
TempCheck = [''] # creates an empty array, put outside the loop to prevent repeating
aoa = [["", "", "", "", ""]] #clears the input

IsFull = True


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = 'Id of the spreadsheets'

service = build('sheets', 'v4', credentials=creds)




def RunTheScript():
    global ccounter
    global aoa
    global IsFull

    RowCounter = "B" + str(ccounter) + ":" + "E" + str(ccounter)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range= RowCounter).execute()
    values = result.get('values', [])
    print(values)

    if values == []: #checks if the row is empty
        print('Empty')
        print(ccounter)
    else:
        
        userinput = (next(iter(values)))
        name = userinput[0]
        LinkToEdit = userinput[1]
        DiscordUser = userinput[2]
        LinkToSocials = userinput[3]

        #if LinkToEdit in Raw: 
        #    UpdatedRaw = Raw + " " + LinkToEdit
        #    repo.update_file(contents.path, "H", UpdatedRaw, contents.sha, branch="master")

        TempCheck.append(LinkToEdit)

        RowCounter = "A" + str(ccounter)

        for x,y in zip(TempCheck,TempCheck[1:]): #checks if the link is the same as the previous one
            if x == y:
                print('Same edit')
            else:
                request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=RowCounter, valueInputOption="USER_ENTERED", body={"values":aoa}).execute() #clears the input


        print(values)
        print(request)
        print(TempCheck)
        print(ccounter)


        usermessage = ''

            # do stuff

        embed = Embed(
            color=0x2F3136,
            timestamp='now'
            )




        embed.set_author(name="Abstrakt Application",url="https://docs.google.com/forms/d/e/1FAIpQLSeBr5dfh4fWIWmPG00hg_z0sVyHs--UWVCWwIYcF1Z6IdQF0Q/viewform", icon_url="https://i.imgur.com/5Ho0Qf1.png")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/883068795877490688/886766650798534666/ABK-LOGO2.gif")
        embed.add_field(name=' | Name:', value= name, inline=False)
        embed.add_field(name=' | Link to edit: ', value= LinkToEdit, inline=False)
        embed.add_field(name=' | Discord:', value= DiscordUser, inline=False)
        embed.add_field(name=' | Link to socials:', value= LinkToSocials, inline=False)



        hook.send("<@&DiscordRoleForAdmins>")
        hook.send(embed=embed)
        ccounter += 1


sched = BlockingScheduler()
sched.add_job(RunTheScript, 'interval', seconds =60) #will do the print_t work for every 60 seconds
sched.start()
