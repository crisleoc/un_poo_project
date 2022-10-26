import os
import sqlite3
from sqlite3 import Error

fileName = './db/database.db'


def connectionToDB():
    """Create a connection to the database:

    Returns:
        connection: Connection object to sqlite3.
    """
    try:
        os.stat('./db/')
    except:
        os.mkdir('./db/')
    try:
        connection = sqlite3.connect(fileName)
        return connection
    except Error:
        print(Error)


def createTables():
    """Create tables in the database:
    """
    try:
        with open('./res/tables.sql', 'r', encoding='utf-8') as sql_file:
            sql = sql_file.read()
        connection = connectionToDB()
        CURSOR_OBJ = connection.cursor()
        CURSOR_OBJ.executescript(sql)
        connection.commit()
    except Error as e:
        print(e)


def fillDB():
    """Generate data in the database:
    """
    try:
        with open('./res/genData.sql', 'r', encoding='utf-8') as sql_file:
            sql = sql_file.read()
        connection = connectionToDB()
        CURSOR_OBJ = connection.cursor()
        CURSOR_OBJ.executescript(sql)
        connection.commit()
    except Error as e:
        raise e
