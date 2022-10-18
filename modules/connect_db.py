import sqlite3
from sqlite3 import Error


def connectionToDB():
    """Create a connection to the database:

    Returns:
        connection: Connection object to sqlite3.
    """
    try:
        connection = sqlite3.connect(
            './db/database.db')
        return connection
    except Error:
        print(Error)
