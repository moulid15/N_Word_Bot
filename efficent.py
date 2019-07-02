import discord
import json
import os
from json.decoder import JSONDecodeError
from collections import defaultdict

client = discord.Client()
token ='private'
serverID ='private'
datastore = defaultdict(int)


async def counter1(channel,count1):
    async for message in channel.history(limit=None):
        if message.content.lower().find('badword1') != -1 or message.content.lower().find('badword2') != -1:
            user = message.author.display_name
            if user in count1:
                count1[user] += 1
            else:
                count1[user]=1
@client.event
async def on_ready():
    filename = 'jsonFile.json'
    guild = client.get_guild(serverID)
    channel = guild.text_channels
    print("entering Ready....")


    # If the file name does not exists, write a JSON string into the file.
        # Writing JSON data
    print(datastore)
    print('file making....')
    if not os.path.exists(filename):
        for i in channel:
            await counter1(i,datastore) #store the data into a dict
        with open(filename, 'w') as f:
            l=dict(sorted(datastore.items(),key=lambda x: x[1]))
            json.dump(l,f, indent=4)
    print('exiting ready....')

@client.event
async def on_message(message):
    print("entering message.....")

    if message.content.lower().find('!ncount') != -1 and message.mentions:
        memebers=message.mentions
        filename = 'jsonFile.json'
        with open(filename,'r') as jsonFile:
            d = json.load(jsonFile)
        await message.channel.send(memebers[0].display_name+" you thot, you owe snow a cool "+'``'+'$'+str(d[memebers[0].display_name]*4)+'``')
    else:
        filename = 'jsonFile.json'
        with open(filename,'r') as jsonFile:
            d = json.load(jsonFile)
        await message.channel.send("Hey thot you owe Snow "+'``'+'$'+str(d[message.author.display_name]*4)+'``')


    if message.content.lower().find('!allncount') != -1:
        print("entering !allncount....")
        channel = message.channel
        buffer2=''
        filename = 'jsonFile.json'
        if os.path.exists(filename):
            with open(filename,'r') as jsonFile:
                d = (json.load(jsonFile))
            for i in d.keys():
                buffer1='|        '+ str(i)+ '    |        ' +'$'+str(d[i]*4) +  '     |'+'\n'
                buffer2 += buffer1
            await channel.send(" ``<-------------- bad Word Score board ---------------->\n"+buffer2 +'``')
        else:
            await channel.send('collecting data....')
        print("exiting !allncount.....")
    #     await counter2(message.channel)

    if message.content.lower().find('send1') != -1:
        await message.channel.send('nigger')
        
    if message.content.lower().find('badword1') != -1 or message.content.lower().find('badword2') != -1:
        print('someone said a bad word....')
        filename = 'jsonFile.json'
        if os.path.exists(filename):
            with open(filename,'r') as jsonFile:
                d = json.load(jsonFile)
            user = message.author.display_name
            if user in d:
                d[user] += 1
            else:
                d[user]=1
            with open(filename,'w') as f:
                l=dict(sorted(d.items(),key=lambda x: x[1],reverse=True))
                json.dump(l,f, indent=4)
        else:
            print('wait for the bot to start')

        print('finishing updating Jsonfile....')
client.run(token)
