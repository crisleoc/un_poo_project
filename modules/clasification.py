from lib2to3.pgen2.token import NAME
import sqlite3 #importar SQLITE
from sqlite3 import Error #generación de errores de SQLITE

def connectionToDB():
    try:
        connection = sqlite3.connect(
            './res/database.db')  # Database connection
        return connection
    except Error:
        print(Error)

def createTableClasification(connection):
    cursorObj=connection.cursor()#recorremos la base de datos con el objeto de conexión
    STUDENTID = "studentid INTEGER PRIMARY KEY"
    NAME = "name TEXT"
    LAST_NAME = "lastname TEXT"
    AMOUNT_SUBJECTS = "amountsubjects INTEGER"
    CREDIT_SUM = "creditsum INTEGER"
    AVERAGE = "average INTEGER"
    CREATE_STATEMENT =f"CREATE TABLE IF NOT EXISTS clasification({STUDENTID},{NAME},{LAST_NAME},{AMOUNT_SUBJECTS},{CREDIT_SUM},{AVERAGE})"
    cursorObj.execute(CREATE_STATEMENT) #creamos la tabla materias
    connection.commit() #aseguramos la persistencia guardando la tabla en el disco

