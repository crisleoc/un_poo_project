import sqlite3
from sqlite3 import Error


def connectionToDB():
    try:
        connection = sqlite3.connect(
            './res/database.db')  # Database connection
        return connection
    except Error:
        print(Error)


def createTableSubjects(connection):
    cursor_obj = connection.cursor()
    codigo = "Código INTEGER PRIMARY KEY NOT NULL UNIQUE" 
    nombre = "Nombre TEXT NOT NULL UNIQUE"
    facu = "Dacultad TEXT"
    dep = "Departamento TEXT"
    cred = "Créditos TEXT"
    idioma = "Idioma TEXT"
    create_statement = f"""CREATE TABLE IF NOT EXISTS students(
        {codigo}, {nombre}, {facu}, {dep}, {cred}, {idioma}
        )"""
    cursor_obj.execute(create_statement)
    connection.commit()  # Save DB
    connection.close()

