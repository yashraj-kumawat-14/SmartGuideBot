import sqlite3

conn = sqlite3.connect("smartguidebot.db")
cursor = conn.cursor()

cursor.execute("SELECT prompt, response  FROM data")

data = dict()

datalist = cursor.fetchall()
for item in datalist:
    data[item[0]] = item[1]

