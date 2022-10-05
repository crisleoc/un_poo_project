import sqlite3
from sqlite3 import Error


def connectionToDB():
    try:
        connection = sqlite3.connect(
            './res/database.db')  # Database connection
        return connection
    except Error:
        print(Error)


def createTableStudent(connection):
    cursor_obj = connection.cursor()
    id = "code INTEGER PRIMARY KEY"
    name = "name TEXT"
    last_name = "lastname TEXT"
    career = "career TEXT"
    born_date = "bornDate TEXT"
    entry_date = "entryDate TEXT"
    place_origin = "placeOrigin TEXT"
    email = "email TEXT"
    enroll_quantity = "enrolQuantity INTEGER"
    photograph = "photograph TEXT"
    create_statement = f"CREATE TABLE IF NOT EXISTS students({id}, {name}, {last_name}, {career}, {born_date}, {entry_date}, {place_origin}, {email}, {enroll_quantity}, {photograph})"
    cursor_obj.execute(create_statement)
    connection.commit()  # Save DB
