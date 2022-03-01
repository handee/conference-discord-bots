# bot.py
import os

import discord
from dotenv import load_dotenv
import csv
from os import path

#update for 2022
# we have four poster categories - first 2nd 3rd year and MSc

cats=["1st","2nd","3rd","MSc"]


# csv file has following format 
# column1 = studentname in lowercase, which matches the name of the image file containing their poster
# column2 = poster ID, where 1.01 is the first poster in the first year contest and 2.03 is the third poster in the second year contest. 
# column3 is the submission ID (ignored)
# column4 is the student's full name
# column5 is the university name (ignored)
# column6 is the poster title (ignored)
# column7 is the poster abstract (ignored)
# column8 is the long name of the contest (ignored)


with open('ch.csv', newline='') as file:
    reader = csv.reader(file)
    res = list(map(tuple, reader))



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client=discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    # get the guild object and check we're on the right server
    g=client.guilds[0]
    print(g)
    for student in res:
        imfile="imgs/"+student[0]+".png"
        sid=student[1]
        name=student[3]

        # create a message to post to the student's channel
        if (path.exists(imfile)):
            message=("Here's the poster for "+student[3]+", :thumbsup: to vote for this in the People's Choice")
            print(imfile, message)
        else :
            imfile="placeholder.png"
            message=("We're still waiting for a poster for "+student[3])
            print(imfile, message)

        # set up a channel name for the student
        channelname=student[1]+"-"+student[3]
        # work out what category the channel should be in (1st, 2nd, 3rd, MSc)
        catname=cats[int(channelname[0])-1]
        chan=discord.utils.get(g.categories,name=catname)

        # create a voice channel and a text channel for the student
        newvchannel=await g.create_voice_channel(channelname,category=chan)
        newchannel=await g.create_text_channel(channelname,category=chan)

        # send the message with the poster image to the new text channel
        await newchannel.send(message, file=discord.File(imfile))





client.run(TOKEN)

