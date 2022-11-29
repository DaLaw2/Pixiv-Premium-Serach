import asyncio
import discord
from discord import message
from discord.ext import commands
from definition.Classes import Cog_Extension

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content == "泡麵" and message.author != self.bot.user:
            user_id = message.author.id
            message_channel = message.channel.id
            await message.channel.send(f"將在2分半後在<#{message_channel}>提醒<@{user_id}>該吃泡麵")
            await asyncio.sleep(150)
            await message.channel.send(f"<@{user_id}> 泡麵熟了")

async def setup(bot):
    await bot.add_cog(Event(bot))