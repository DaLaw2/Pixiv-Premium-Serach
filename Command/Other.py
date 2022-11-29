import os
import discord
import datetime
from discord.ext import commands
from definition.Classes import Cog_Extension

class Other(Cog_Extension):
    # DELAY
    @commands.command()
    async def delay(self,ctx):
        embed=discord.Embed(title="Discord Bot Status", color=0x00bfff)
        embed.add_field(name="目前延遲", value=f"{round(self.bot.latency * 1000)}毫秒", inline=False)
        await ctx.send(embed=embed)
    # INFO
    @commands.command()
    async def info(self,ctx):
        embed=discord.Embed(title="Discord Bot Info", url="https://www.ncpb.gov.tw/sub/index.aspx?m1=21", color=0x00bfff,timestamp=datetime.datetime.now())
        embed.set_thumbnail(url="https://truth.bahamut.com.tw/s01/202103/6f079374478e3be3675ce13c32d68333.JPG")
        embed.add_field(name="我叫你刪", value="主要功能：Pixiv.net 熱門度搜尋", inline=True)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Other(bot))