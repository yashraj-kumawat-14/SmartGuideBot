import sqlite3

conn = sqlite3.connect("smartguidebot.db")

cursor = conn.cursor()

cursor.execute("SELECT response, audio, video, image FROM data")
audio_info = dict()

datalist = cursor.fetchall()

for item in datalist:
    audio_info[item[0]] = [item[1], item[2], item[3]]

