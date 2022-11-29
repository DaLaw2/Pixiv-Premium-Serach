import os
import json
import discord
import SerachFromDB
from discord.ext import commands
from definition.Classes import Cog_Extension

class Premium(Cog_Extension):
    # SERACH
    @commands.command()
    async def serach(self,ctx,Tag,rank,*args):
        Result = SerachFromDB.serach(Tag)
        if Result == "DNE":
            with open("/home/dalaw/PeriodEndReport/Finally/queue.json","r",encoding="utf_8") as queueFiles:
                queue = json.load(queueFiles)
                queueFiles.close()
            if f"{Tag}" in queue:
                embed=discord.Embed(title="Permium Serach", color=0x00bfff)
                embed.add_field(name="錯誤", value="仍在佇列中等待", inline=False)
                await ctx.send(embed=embed)
            else:
                queue.append(f"{Tag}")
                with open("/home/dalaw/PeriodEndReport/Finally/queue.json","w",encoding="utf_8") as queueFiles:
                    json.dump(queue,queueFiles,ensure_ascii=False)
                    queueFiles.close()
                embed=discord.Embed(title="Permium Serach", color=0x00bfff)
                embed.add_field(name="錯誤", value="沒有找到，已加入等待佇列", inline=False)
                await ctx.send(embed=embed)
        elif Result == []:
            embed=discord.Embed(title="Permium Serach", color=0x00bfff)
            embed.add_field(name="搜尋結果", value="None", inline=False)
            await ctx.send(embed=embed)
        else:
            if args == ():
                message = ""
                try:
                    rank = int(rank)
                    count = 1
                    for i in Result:
                        if count>=rank and count<rank+10:
                            message += f"https://www.pixiv.net/artworks/{i[0]}\n"
                        if count>=rank+10:
                            break
                        count+=1
                    embed=discord.Embed(title="Permium Serach", color=0x00bfff)
                    embed.add_field(name="搜尋結果", value=f"{message}", inline=False)
                    await ctx.send(embed=embed)
                except:
                    embed=discord.Embed(title="Permium Serach", color=0x00bfff)
                    embed.add_field(name="錯誤", value="引數錯誤", inline=False)
                    await ctx.send(embed=embed)
            else:
                message = ""
                try:
                    rank = int(rank)
                    count = 1
                    for i in Result:
                        if Confirm(i,args) == True:
                            if count>=rank and count<rank+10:
                                message += f"https://www.pixiv.net/artworks/{i[0]}\n"
                            count+=1
                        if count>=rank+10:
                            break
                    if message == "":
                        embed=discord.Embed(title="Permium Serach", color=0x00bfff)
                        embed.add_field(name="搜尋結果", value="None", inline=False)
                        await ctx.send(embed=embed)
                    else:
                        embed=discord.Embed(title="Permium Serach", color=0x00bfff)
                        embed.add_field(name="搜尋結果", value=f"{message}", inline=False)
                        await ctx.send(embed=embed)
                except:
                    embed=discord.Embed(title="Permium Serach", color=0x00bfff)
                    embed.add_field(name="錯誤", value="引數錯誤", inline=False)
                    await ctx.send(embed=embed)
    # QUEUE
    @commands.command()
    async def queue(self,ctx,Tag):
        with open("/home/dalaw/PeriodEndReport/Finally/queue.json","r",encoding="utf_8") as queueFiles:
            queue = json.load(queueFiles)
            queueFiles.close()
        if f"{Tag}" in queue:
            embed=discord.Embed(title="Discord Bot Status", color=0x00bfff)
            embed.add_field(name="Queue", value=f"Tag：{Tag} 已經在等待佇列中了", inline=False)
            await ctx.send(embed=embed)
        else:
            queue.append(f"{Tag}")
            embed=discord.Embed(title="Discord Bot Status", color=0x00bfff)
            embed.add_field(name="Queue", value=f"Tag：{Tag} 已加入等待佇列", inline=False)
            await ctx.send(embed=embed)
            with open("/home/dalaw/PeriodEndReport/Finally/queue.json","w",encoding="utf_8") as queueFiles:
                json.dump(queue,queueFiles,ensure_ascii=False)

def Confirm(Source,Option):
    Status = False
    i=0
    while i < len(Option):
        if Option[i] == "+t":
            if f"{Option[i+1]}" not in Source[2]:
                return False
            i+=1
        elif Option[i] == "-t":
            if f"{Option[i+1]}" in Source[2]:
                return False
            i+=1
        elif Option[i] == "+NSFW":
            if "R-18" not in Source[2]:
                return False
        elif Option[i] == "-NSFW":
            if "R-18" in Source[2]:
                return False
        i+=1
    return True

async def setup(bot):
    await bot.add_cog(Premium(bot))