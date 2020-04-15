# conference-discord-bots


This repo contains three Discord bots which I wrote to help run the BCSWomen Lovelace Colloquium

They might be useful to other people running conferences, so I thought I'd put them up here.

To get them running you need to install discord.py and follow the instructions for setting up a new bot - there are lots of tutorials online. I found this one https://realpython.com/how-to-make-a-discord-bot-python/ really very clear.

## welcomebot

Welcomebot sends a direct message to everyone who joins your channel. I used this to send a bit of "how to Discord" info and also to remind all attendees of the code of conduct.  This needs to run continually (so either on a server, or just leave your computer on if you're lazy like me).

## posterbot

Student presenters submitted posters to us as A1 PDF and I converted these to PNG files entitled studentname.png. Posterbot takes a CSV file with the image filenames, and student names, and some extraneous stuff (it's all quite hacky) and ...
 
  * creates a voice channel for each student 
  * creates a text channel for each student
  * makes the first post in the text channel, including the poster image 
  
our posters are in 4 categories (1st, 2nd, 3rd, MSc) and the bot manages to get  the channels in the right categories.

This makes the channels when it first connects to the server so you can run it once then turn it off.

## photobot

We asked attendees to post a quick intro + image to our introductions-and-bios channel. In order to stitch these together and make an attendees group photo I wanted to download all the pictures... so obviously I wrote a bot rather than do it by hand. Photobot is that bot. It is very hacky - it saves every attachment as discordname.jpg which is stupid given that some of the attachments aren't actually jpgs. It does download all attachments from a channel though so it goes quite a long way to solving the problem (if you do have to rename all the png files after the fact).

This downloads the attachments when it first connects to the server so you can run it once then turn it off.

