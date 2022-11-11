import discord
import os
import requests
import json
from dotenv import load_dotenv
from discord.ext import commands
from weather import *


command_prefix = 'w.'
#token = process.env.DISCORD_TOKEN;
#applicationId = process.env.DISCORD_APPLICATION_ID;
load_dotenv()
token = os.getenv('TOKEN')

#Working Code
bot = commands.Bot(command_prefix)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{command_prefix}[location]'))

@bot.event
async def on_message(message):
    if message.author != bot.user and message.content.startswith(command_prefix):
        location = message.content.replace(command_prefix, '').lower()
        if len(location) >= 1:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'
            try:
                data = parse_data(json.loads(requests.get(url).content)['main'])
                await message.channel.send(embed=weather_message(data, location))
            except KeyError:
                await message.channel.send(embed=error_message(location))
    await bot.process_commands(message)
###Questionable below - do i need this CTX command if i use what's bot.event above?
#@bot.command()
#async def on_message(ctx, command_prefix, message): #???
#    if message.author !=bot.user and message.content.startswith(command_prefix):
#        location = message.content.replace(command_prefix, '').lower()
#        if len(location) >= 1:
#            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'
#            try:
#                data = parse_data(json.loads(requests.get(url).content)['main'])
#                await message.send(embed=weather_message(data, location))
#            except KeyError:
#                await message.send(embed=error_message(location))
#    await ctx.send(ctx, message)
bot.run(token)
##

####Old code - Below is using the client Discord commands before coverting to bot commands
# client = discord.Client()

# @client.event
# async def on_ready():
#     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{command_prefix}[location]'))

# @client.event
# async def on_message(message):
#     if message.author != client.user and message.content.startswith(command_prefix):
#         location = message.content.replace(command_prefix, '').lower()
#         if len(location) >= 1:
#             url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'
#             try:
#                 data = parse_data(json.loads(requests.get(url).content)['main'])
#                 await message.channel.send(embed=weather_message(data, location))
#             except KeyError:
#                 await message.channel.send(embed=error_message(location))

#client.run(token)
####