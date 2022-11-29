import os
import discord
from discord.ext import commands
from definition.Classes import Cog_Extension

class Core(Cog_Extension):
    # LOAD
    @commands.command()
    async def load(self,ctx,Module):
        if Module == "all":
            for Filename in os.listdir("./Command"):
                if Filename.endswith(".py") and not Filename.startswith("Core"):
                    await self.bot.load_extension(f"Command.{Filename[:-3]}")
            embed=discord.Embed(title="Discord Bot Status", color=0x00bfff)
            embed.add_field(name="Load", value=f"加載所有模組成功", inline=False)
            await ctx.send(embed=embed)
        elif Module == "Core":
            embed=discord.Embed(title="Discord Bot Status", color=0x00bfff)
            embed.add_field(name="Load", value="錯誤 該模組不可被加載", inline=False)
            await ctx.send(embed=embed)
        elif os.path.isfile(f"./Command/{Module}.py")!=True:
            embed=discord.Embed(title="Discord Bot Status", color=0x00bfff)
            embed.add_field(name="Load", value="錯誤 該模組不存在", inline=False)
            await ctx.send(embed=embed)
        else:
            await self.bot.load_extension(f"Command.{Module}")
            embed=discord.Embed(title="Discord Bot Status", color=0x00bfff)
            embed.add_field(name="Load", value=f"加載{Module}模組成功", inline=False)
            await ctx.send(embed=embed)
    # UNLOAD
    @commands.command()
    async def unload(self,ctx,Module):
        if Module == "all":
            for Filename in os.listdir("./Command"):
                if Filename.endswith(".py") and not Filename.startswith("Core"):
                    await self.bot.unload_extension(f"Command.{Filename[:-3]}")
            embed=discord.Embed(title="Discord Bot Status", color=0x00bfff)
            embed.add_field(name="Unload", value=f"卸載所有模組成功", inline=False)
            await ctx.send(embed=embed)
        elif Module == "Core":
            embed=discord.Embed(title="Discord Bot Status", color=0x00bfff)
            embed.add_field(name="Unload", value="錯誤 該模組不可被卸載", inline=False)
            await ctx.send(embed=embed)
        elif os.path.isfile(f"./Command/{Module}.py")!=True:
            embed=discord.Embed(title="Discord Bot Status", color=0x00bfff)
            embed.add_field(name="Unload", value="錯誤 該模組不存在", inline=False)
            await ctx.send(embed=embed)
        else:
            await self.bot.unload_extension(f"Command.{Module}")
            embed=discord.Embed(title="Discord Bot Status", color=0x00bfff)
            embed.add_field(name="Unload", value=f"卸載{Module}模組成功", inline=False)
            await ctx.send(embed=embed)
    # RELOAD
    @commands.command()
    async def reload(self,ctx,Module):
        if Module == "all":
            for Filename in os.listdir("./Command"):
                if Filename.endswith(".py"):
                    await self.bot.reload_extension(f"Command.{Filename[:-3]}")
            embed=discord.Embed(title="Discord Bot Status", color=0x00bfff)
            embed.add_field(name="Reload", value="重新加載所有模組成功", inline=False)
            await ctx.send(embed=embed)
        elif os.path.isfile(f"./Command/{Module}.py")!=True:
            embed=discord.Embed(title="Discord Bot Status", color=0x00bfff)
            embed.add_field(name="Reload", value="錯誤 該模組不存在", inline=False)
            await ctx.send(embed=embed)
        else:
            self.bot.reload_extension(f"Command.{Module}")
            embed=discord.Embed(title="Discord Bot Status", color=0x00bfff)
            embed.add_field(name="Reload", value=f"重新加載{Module}模組成功", inline=False)
            await ctx.send(embed=embed)
    # HELP
    @commands.command()
    async def help(self,ctx,*command):
        if command == ():
            embed=discord.Embed(title="Help List", color=0x00bfff)
            embed.add_field(name="!info", value="顯示機器人資訊", inline=False)
            embed.add_field(name="!load + All/Name", value="加載所有/指定模組", inline=True)
            embed.add_field(name="!unload + All/Name", value="卸載所有/指定模組", inline=True)
            embed.add_field(name="!reload + All/Name", value="重新加載所有/指定模組", inline=True)
            embed.add_field(name="!serach +Tag +Rank (+args", value="搜尋該Tag並返回第Rank名結果", inline=True)
            embed.add_field(name="!queue +Tag", value="將Tag加入等待佇列", inline=True)
            embed.add_field(name="!delay", value="取得機器人與伺服器延遲時間", inline=False)
            embed.add_field(name="!help", value="顯示此則訊息", inline=False)
            await ctx.send(embed=embed)
        elif command == ('info',):
            embed=discord.Embed(title="Command Help", color=0x00bfff)
            embed.add_field(name="!info", value="顯示機器人資訊", inline=False)
            await ctx.send(embed=embed)
        elif command == ('load',):
            embed=discord.Embed(title="Command Help", color=0x00bfff)
            embed.add_field(name="!load + All/Name", value="加載所有/指定模組", inline=False)
            await ctx.send(embed=embed)
        elif command == ('unload',):
            embed=discord.Embed(title="Command Help", color=0x00bfff)
            embed.add_field(name="!unload + All/Name", value="卸載所有/指定模組", inline=False)
            await ctx.send(embed=embed)
        elif command == ('reload',):
            embed=discord.Embed(title="Command Help", color=0x00bfff)
            embed.add_field(name="!reload + All/Name", value="重新加載所有/指定模組", inline=False)
            await ctx.send(embed=embed)
        elif command == ('serach',):
            embed=discord.Embed(title="Command Help", color=0x00bfff)
            embed.add_field(name="!serach", value="!serach+Tag +Rank (+args\nTag：要搜尋的Tag\nRank：篩選過後最熱門的第幾名\nArgs：\n+t 篩選搜尋結果必須包含某Tag\n-t 篩選搜尋結果必須不包含某Tag\n+NSFW 篩選搜尋結果僅有R18\n-NSFW 篩選搜尋結果僅有全年齡", inline=False)
            await ctx.send(embed=embed)
        elif command == ('queue',):
            embed=discord.Embed(title="Command Help", color=0x00bfff)
            embed.add_field(name="!queue +Tag", value="將Tag加入等待佇列", inline=False)
            await ctx.send(embed=embed)
        elif command == ('delay',):
            embed=discord.Embed(title="Command Help", color=0x00bfff)
            embed.add_field(name="!delay", value="取得機器人與伺服器延遲時間", inline=False)
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Core(bot))