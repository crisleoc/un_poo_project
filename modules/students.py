def createStudentTable(connection):
    """Create a table in the database:

    Args:
        connection (object): Connection to sqlite3.
    """
    CURSOR_OBJ = connection.cursor()
    ID = "id INTEGER PRIMARY KEY"
    NAME = "name TEXT"
    LAST_NAME = "lastname TEXT"
    CAREER = "career TEXT"
    BORN_DATE = "bornDate TEXT"
    ENTRY_DATE = "entryDate TEXT"
    PLACE_ORIGIN = "placeOrigin TEXT"
    EMAIL = "email TEXT"
    ENROLL_QUANTITY = "enrollQuantity INTEGER"
    PICTURE = "photograph TEXT"
    CREATE_STATEMENT = f"CREATE TABLE IF NOT EXISTS students({ID}, {NAME}, {LAST_NAME}, {CAREER}, {BORN_DATE}, {ENTRY_DATE}, {PLACE_ORIGIN}, {EMAIL}, {ENROLL_QUANTITY}, {PICTURE})"
    CURSOR_OBJ.execute(CREATE_STATEMENT)
    connection.commit()


def insertStudent(connection, student):
    """Insert a student in the database:

    Args:
        connection (object): Connection to sqlite3.
        student (tuple): Tuple with the data (10 spaces) of the student.
    """
    CURSOR_OBJ = connection.cursor()
    INSERT_STATEMENT = "INSERT INTO students VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    CURSOR_OBJ.execute(INSERT_STATEMENT, student)
    connection.commit()


def selectAllStudents(connection):
    """Select all students in the database:

    Args:
        connection (object): Connection to sqlite3.

    Returns:
        list<tuple>: List of tuples with the data of the students.
    """
    CURSOR_OBJ = connection.cursor()
    SELECT_STATEMENT = "SELECT * FROM students"
    CURSOR_OBJ.execute(SELECT_STATEMENT)
    return CURSOR_OBJ.fetchall()


def selectStudentByID(connection, id):
    """Select a student by id in the database:

    Args:
        connection (object): Connection to sqlite3.
        id (int): Id of the student.

    Returns:
        list<tuple>: List of tuples with the data of the students that contains the id.
    """
    CURSOR_OBJ = connection.cursor()
    SELECT_STATEMENT = "SELECT * FROM students WHERE id = ?"
    CURSOR_OBJ.execute(SELECT_STATEMENT, (id,))
    return CURSOR_OBJ.fetchall()
