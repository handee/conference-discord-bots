# bot.py
import os

import discord
from dotenv import load_dotenv
import aiohttp
import aiofiles



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client=discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
    # check we're on the right server
    g=client.guilds[0]
    print(g)
    # find the channel with the intros on it
    chan=discord.utils.get(g.channels,name="introductions-and-bios")
    # download all the message objects
    messages = await chan.history(limit=200).flatten()
    
    
    for m in messages:
        if len(m.attachments)>0 :
            screen_name=m.author.name 
            ofilename=screen_name.replace(" ","")+".jpg"
            print("Downloading...")
            print(m.attachments[0].url)
            print("To...")
            print(ofilename)
            async with aiohttp.ClientSession() as session:
                async with session.get(m.attachments[0].url) as resp:
                    if resp.status ==200:
                        f = await aiofiles.open(ofilename,mode='wb')
                        await f.write(await resp.read())
                        await f.close()





client.run(TOKEN)

