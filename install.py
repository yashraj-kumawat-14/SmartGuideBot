import sqlite3

conn = sqlite3.connect("smartguidebot.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS data")
conn.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, prompt TEXT, response TEXT, audio TEXT, video TEXT, image TEXT)")
conn.commit()

conn.close()




