# bot.py
import os

import discord
from dotenv import load_dotenv

newUserMessage = """ # Welcome to the BCSWomen Lovelace Discord Server

We’re expecting about 200 people (more or less) to join for the conference so please:

*  Set your nickname to be your actual name (matching the name on your poster, if you’re a poster presenter).
*  Post chatter in the various -chat channels rather than those on a particular topic
*  Be nice to people!
*  Remember we have a Code of Conduct 
https://bcswomenlovelace.bcs.org/?page_id=8 
*  If you're after help, there's a discord-help channel and you can ask any questions there
*  It'd be nice if you posted a short intro to yourself in the introductions-and-bios channel, but you don't have to... it's a nice first post though!

If you've not used Discord before or if you're not sure what's going on,
check out this document with some tips:
    
https://docs.google.com/document/d/1HzAhHyfoHPmGfgOHTh1jfEn-g7r0GiGKMpWUq7WIm7o/edit

We also have a short video about the use of Discord for this event.

https://www.youtube.com/watch?v=ZXlUz_oM1AA


Thanks!
Lovelace Discord Welcome-bot

"""


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client=discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    try: 
        channel = await member.create_dm()
        await channel.send(newUserMessage)
        print("Sent message to " + member.name)
    except:
        print("Couldn't message " + member.name)



client.run(TOKEN)

