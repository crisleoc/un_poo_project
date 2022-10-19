import sqlite3  # importar SQLITE
from sqlite3 import Error  # generación de errores de SQLITE


def connectionToDB():
    try:
        connection = sqlite3.connect(
            './res/database.db')  # Database connection
        return connection
    except Error:
        print(Error)


def crearTablaClasificación(connection):
    # recorremos la base de datos con el objeto de conexión
    cursorObj = connection.cursor()
    # creamos la tabla materias
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Clasificación(identificación integer PRIMARY KEY, Nombre text, Apellido text,  CantMateTomadas text, creditosAcumulados integer, Promedio integer)")
    connection.commit()  # aseguramos la persistencia guardando la tabla en el disco


def insertarInfoClasificación(connection):
    cursorObj = connection.cursor()
    identificación = input("inserte la identificación del estudiante")
    # ajustar el codigo a la izquierda 12 posiciones
    identificación = identificación.ljust(12)
    Nombre = input("inserte el nombre del estudiante")
    Apellido = input("inserte el apellido del estudiante")
    CantMateTomadas = input("inserte la cantidad de materias tomadas")
    creditosAcumulados = input("inserte los creditos acumulados")
    Promedio = input("placeholder del promedio")
    clas = (identificación, Nombre, Apellido, CantMateTomadas,
            creditosAcumulados, Promedio)  # tupla de insert
    cursorObj.execute('INSERT INTO Clasificación VALUES(?,?,?,?,?,?)', clas)
    connection.commit()
