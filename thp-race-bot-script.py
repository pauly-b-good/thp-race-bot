import discord
from discord.ext import commands
import asyncio
import json

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
    bot_token = config_data.get('token')

prefix = "/"
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def countdown(ctx):
    try:
        for i in range(10, 0, -1):
            await ctx.send(f"{i}...")
            await asyncio.sleep(1)
        await ctx.send("GOOOOOOOOOOOOO!")
    except Exception as e:
        print(f"An error occurred: {e}")

@bot.command()
async def about(ctx):
    print("")




bot.run(bot_token)