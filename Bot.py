import os
import json
import asyncio
import discord
from discord.ext import commands
from discord.flags import Intents

with open("config.json" , "r" ,encoding="utf8") as configFiles:  
    config = json.load(configFiles)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents,help_command=None)

@bot.event
async def on_ready():
    print("✔Bot is online")
    Status = discord.Status.idle
    Activity = discord.Activity(type=discord.ActivityType.playing,name="神秘公權力")
    await bot.change_presence(status=Status,activity=Activity)

async def main():
    async with bot:
        await load_extensions()
        await bot.start(config["Token"])

async def load_extensions():
    for Filename in os.listdir("./Command"):
        if Filename.endswith(".py"):
            await bot.load_extension(f"Command.{Filename[:-3]}")

if __name__=="__main__":
    asyncio.run(main())