import re
import json
import random
import asyncio
import aiohttp
from math import ceil

async def GetTotal(tag,session):
    with open("config.json","r",encoding="utf_8") as configFiles:
        config = json.load(configFiles)
        configFiles.close()
    user_agent = config["user_agent"]
    cookie = config["cookie"]
    referer = f"https://www.pixiv.net/tags/{tag}/artworks".encode()
    headers = {"user-agent":f"{user_agent}","cookie":f"{cookie}","referer":f"{referer}"}
    url = f"https://www.pixiv.net/ajax/search/artworks/{tag}?word={tag}&order=date_d&mode=all&p=1&s_mode=s_tag_full&type=all&lang=zh_tw"
    while True:
        await asyncio.sleep(random.uniform(0,1))
        try:
            async with await session.get(url=url,headers=headers) as Req:
                ReqData = await Req.json()
                total = ReqData["body"]["illustManga"]["total"]
                if Req.status == 200:
                    if ReqData["body"]["illustManga"]["data"] == []:
                        await asyncio.sleep(200)
                        continue
                    break
                else:
                    await asyncio.sleep(200)
                    continue
        except:
            continue
    return total

async def GetTagDetail(tag,page,session):
    with open("config.json","r",encoding="utf_8") as configFiles:
        config = json.load(configFiles)
        configFiles.close()
    user_agent = config["user_agent"]
    cookie = config["cookie"]
    referer = f"https://www.pixiv.net/tags/{tag}/artworks".encode()
    headers = {"user-agent":f"{user_agent}","cookie":f"{cookie}","referer":f"{referer}"}
    url = f"https://www.pixiv.net/ajax/search/artworks/{tag}?word={tag}&order=date_d&mode=all&p={page}&s_mode=s_tag_full&type=all&lang=zh_tw"
    while True:
        await asyncio.sleep(random.uniform(0,1))
        try:
            async with await session.get(url=url,headers=headers) as Req:
                ReqData = await Req.json()
                if Req.status == 200:
                    Req_result = ReqData["body"]["illustManga"]["data"]
                    if Req_result == []:
                        await asyncio.sleep(200)
                        continue
                    break
                else:
                    await asyncio.sleep(200)
                    continue
        except:
            continue
    return Req_result

async def GetIDLikes(id,session):
    with open("config.json","r",encoding="utf_8") as configFiles:
        config = json.load(configFiles)
        configFiles.close()
    user_agent = config["user_agent"]
    cookie = config["cookie"]
    referer = f"https://www.pixiv.net/artworks/{id}".encode()
    url = f"https://www.pixiv.net/bookmark_detail.php?illust_id={id}"
    headers = {"user-agent":f"{user_agent}","cookie":f"{cookie}","referer":f"{referer}"}
    while True:
        await asyncio.sleep(random.uniform(0,1))
        try:
            async with await session.get(url=url,headers=headers) as Req:
                ReqData = await Req.text()
                if Req.status == 200:
                    try:
                        likes = re.findall('<span class="count-badge">\d+人',ReqData)[0][26:-1]
                        break
                    except:
                        likes = 0
                        break
                else:
                    await asyncio.sleep(200)
                    continue
        except:
            continue
    Result = {f"{id}":likes}
    return Result

async def GetAndWrite(tag):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(GetTotal(tag,session))]
        total = await asyncio.gather(*tasks)
        total = total[0]
    if total == 0:
        with open(f"./Finally/RequestData/{tag}.json", "w",encoding="utf8") as resultFiles:
            json.dump({},resultFiles,ensure_ascii=False)
        exit()
    page = ceil((total)/60)
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(GetTagDetail(tag,page,session)) for page in range(1,page+1,1)]
        AllTag = await asyncio.gather(*tasks)
    AllTagDetail = {}
    for i in AllTag:
        for j in i:
            id = j["id"]
            other = {"title":j["title"],"tags":j["tags"],"userId":j["userId"],"userName":j["userName"],"updateDate":j["updateDate"]}
            AllTagDetail[f"{id}"] = other
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(GetIDLikes(id,session)) for id in AllTagDetail.keys()]
        AllTagLikes = await asyncio.gather(*tasks)
    Result = AllTagDetail
    for i in AllTagLikes:
        id = list(i.keys())[0]
        likes = i[f"{id}"]
        Result[f"{id}"]["likes"] = likes
    with open(f"./RequestData/{tag}.json", "w",encoding="utf8") as resultFiles:
        json.dump(Result,resultFiles,ensure_ascii=False)