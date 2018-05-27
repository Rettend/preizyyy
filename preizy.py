import discord, logging, json, asyncio, time, random, aiohttp, re, datetime, traceback, os, sys, math
from discord.ext import commands

bot = commands.Bot(command_prefix='>>', description=None)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="diep.io"))

@bot.command(pass_context=True)
async def ben(user):
    if user == bot.user.name:
        bot.say("I wont ben myself xd")
    if user != bot.user.name:
        bot.say(f"{ctx.message.author} banned {user.name}...")



token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
