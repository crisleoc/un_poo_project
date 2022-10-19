def createTableSubjects(connection):
    """Create the subjects table in the database:

    Args:
        connection (object): Connection to sqlite3.
    """

    cursor_obj = connection.cursor()
    code = "code INTEGER PRIMARY KEY NOT NULL UNIQUE"
    name = "name TEXT NOT NULL UNIQUE"
    school = "school TEXT"
    department = "department TEXT"
    credits = "credits TEXT"
    language = "language TEXT"
    create_statement = f"""CREATE TABLE IF NOT EXISTS subjects(
        {code}, {name}, {school}, {department}, {credits}, {language}
        )"""
    cursor_obj.execute(create_statement)
    connection.commit()  # Save DB


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
