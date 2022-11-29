import mysql.connector

def serach(Tag):
    conn = mysql.connector.connect(host = '',user = '',password = '',port = 3306,db = '',charset='utf8mb4',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    cursor.execute(f"SELECT table_name FROM information_schema.TABLES WHERE table_name ='{Tag}';")
    exist = cursor.fetchone()
    if exist == None:
        return "DNE"
    else:
        cursor.execute(f"SELECT * FROM `{Tag}` ORDER BY likes DESC")
    result = cursor.fetchall()
    return result