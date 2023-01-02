from asyncio.windows_events import NULL
import threading
import time
import asyncio

import threading

import os

import discord 
from dotenv import load_dotenv
from discord.ext import tasks


load_dotenv()

BRIANCHANNELID = 843655338259120140
BRIANBOTID = 275777377202733056
BENID = 232990331644149770

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

messageTime = time.time_ns()
waiting = False


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name = GUILD)
    print(
        f'{client.user} has connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    global messageTime
    global waiting
    channel = message.channel
    targetChannelid = 843655338259120140
    user = message.author
    guild = message.guild
    currTime = time.time_ns()



    if message.author == client.user:
        return



    #Ben Stuff
    if message.author.id == BENID:
        await message.channel.send("@Benjamin Button#1185 https://tenor.com/view/ben-not-funny-annoying-kanye-gif-19515770")

    if message.author.id != BRIANBOTID or message.channel.id != BRIANCHANNELID or waiting:
        return

    if(message.content.find("Leaderboard") != -1 or message.content.find("streak") != -1):
        return

    timeRemaining = ''.join(filter(lambda i: i.isdigit(), message.content))


    try:
        timeRemaining = (float(timeRemaining))/100
        await message.channel.send(timeRemaining)
    except:
        timeRemaining = NULL
        waiting = True
        await asyncio.sleep(timeRemaining)
        waiting = False
        await message.channel.send("brian please")
        return

    minutes = False

    if(message.content.find("min") != -1):
        minutes = True
    
    if minutes:
        timeRemaining = timeRemaining - 0.5
        timeRemaining = timeRemaining*60 #Gives seconds

    waiting = True
    await asyncio.sleep(timeRemaining) #This should make the sleep async for a single thread
    waiting = False
    currTime = time.time_ns()
    timeDiff = (currTime-messageTime)/1000000000
    await message.channel.send("brian please " + str(timeRemaining) + " " + str(timeDiff))
    messageTime = currTime



    







client.run(TOKEN)





        

#await message.channel.send(response)