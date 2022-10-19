def createSubjectsTable(connection):
    """Create the subjects table in the database:

    Args:
        connection (object): Connection to sqlite3.
    """

    CURSOR_OBJ = connection.cursor()
    ID = "id INTEGER PRIMARY KEY NOT NULL UNIQUE"
    NAME = "name TEXT NOT NULL UNIQUE"
    SCHOOL = "school TEXT"
    DEPARTMENT = "department TEXT"
    CREDITS = "credits TEXT"
    LANGUAGE = "language TEXT"
    CREATE_STATEMENT = f"""CREATE TABLE IF NOT EXISTS subjects(
        {ID}, {NAME}, {SCHOOL}, {DEPARTMENT}, {CREDITS}, {LANGUAGE}
        )"""
    CURSOR_OBJ.execute(CREATE_STATEMENT)
    connection.commit()


def insertSubject(connection, subject):
    """Insert a subject in the subjects table:

    Args:
        connection (object): Connection to sqlite3.
        subject (tuple): Tuple containing the elements of the Subjects table.

    """
    cursor_obj = connection.cursor()
    create_statement = "INSERT INTO subject VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor_obj.execute(create_statement, subject)
    connection.commit()


def selectAllSubjects(connection):
    """Select all of the subjects in the Subjects table:

    Args:
        connection (object): Connection to sqlite3.

    Returns:
        list<tuple>: List of tuples with the data of the subjects.
    """
    cursor_obj = connection.cursor()
    create_statement = "SELECT * FROM subjects"
    cursor_obj.execute(create_statement)
    return cursor_obj.fetchall()
