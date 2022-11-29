import json
import mysql.connector

def insert(tag):
    with open(f"./RequestData/{tag}.json","r",encoding="utf_8") as source:
        data = json.load(source)
    conn = mysql.connector.connect(host = '',user = '',password = '',port = 3306,db = '',charset='utf8mb4',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE  IF EXISTS `{tag}`;")
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS `{tag}`  (id INT UNSIGNED NOT NULL, title varchar(50), tags varchar(500), userId INT UNSIGNED, userName varchar(50), updateDate varchar(50), likes INT UNSIGNED);''')
    for id in data.keys():
        id = int(id)
        title = data[f"{id}"].get("title")
        title = escape_string(title)
        tags = json.dumps(data[f"{id}"].get("tags"),ensure_ascii=False)
        if tags == "null":
            tags = None
        tags = escape_string(tags)
        userId = data[f"{id}"].get("userId")
        userName = data[f"{id}"].get("userName")
        userName = escape_string(userName)
        updateDate = data[f"{id}"].get("updateDate")
        updateDate = escape_string(updateDate)
        likes = data[f"{id}"].get("likes")
        if likes != None:
            likes = int(likes)
        sql= f"INSERT INTO `{tag}` VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (id,title,tags,userId,userName,updateDate,likes)
        cursor.execute(sql,val)
    conn.commit()
    cursor.close()
    conn.close()

def escape_string(input):
    if input == None:
        return None
    input = input.replace("'","\'\'")
    input = input.replace("\\","\\\\")
    return input