import sqlite3
from sqlite3 import Error

cnn = None
fileName = './db/database.db'

try:
    with open('./res/test1.sql', 'r', encoding='utf-8') as sql_file:
        sql = sql_file.read()
    cnn = sqlite3.connect(fileName)
    cs = cnn.cursor()
    cs.executescript(sql)
    cnn.commit()
except Error as e:
    print(e)
finally:
    if cnn:
        cnn.close()
