import json
import time
import asyncio
import GetWebData
import InsertToDB

def Manager():
    while True:
        with open("queue.json","r",encoding="utf_8") as queueFiles:
            queue = json.load(queueFiles)
            queueFiles.close()
        if queue == []:
            time.sleep(10)
            continue
        else:
            Tag = queue[0]
            print(f"Start Get {Tag}")
            asyncio.run(GetWebData.GetAndWrite(Tag))
            print(f"Get {Tag} Success")
            print(f"Start Insert {Tag} Into DB")
            InsertToDB.insert(Tag)
            print(f"Insert {Tag} Into DB Success")       
            with open("queue.json","r",encoding="utf_8") as queueFiles:
                queue = json.load(queueFiles)
                queueFiles.close()
            queue.pop(0) 
            with open("queue.json","w",encoding="utf_8") as queueFiles:
                json.dump(queue,queueFiles,ensure_ascii=False)
            continue

if __name__ == "__main__":
    Manager()