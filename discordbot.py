import discord, time, asyncio, wikipedia
from discord.ext.commands import Bot
from discord.ext import commands


Client = discord.Client()
client = commands.Bot(command_prefix = '$')
f = open("whattheysay.txt","w+")

@client.event
async def on_message(message):
    content = message.content
    author = message.author
    if message.content.startswith('$carlton'):
        content = content[8:]
        await client.send_message(client.get_channel(id='428658439129006090'), content)
@client.event
async def on_message(message):
    content = message.content
    author = message.author
    if message.content.startswith('$wikipedia'):
        content = content[10:]
        dog = wikipedia.summary(content)
        await client.send_message(message.channel, dog)
@client.event
async def on_message(message):
    content = message.content
    author = message.author
    if message.content.startswith('$picture'):
        content = content[7:]
        chicken = ('https://i.imgur.com/7bkRfim.gif')
        await client.send_message(message.channel, chicken)
@client.event
async def on_message(message):
    content = message.content
    author = message.author
    if 'fuck' or 'shit' or 'damn' in content:
        await client.kick(author)





client.run("NDY0NTY2Nzc4NjU2MTk0NTcw.DiA9eQ.jlQrfs8zzPtsF4hD1shZ5tvids8")
