from . import config_app as CONFIG


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
    BIRTH_DATE = "birthDate TEXT"
    ENTRY_DATE = "entryDate TEXT"
    PLACE_ORIGIN = "placeOrigin TEXT"
    EMAIL = "email TEXT"
    ENROLL_QUANTITY = "enrollQuantity INTEGER"
    PICTURE = "photograph TEXT"
    CREATE_STATEMENT = f"CREATE TABLE IF NOT EXISTS students({ID}, {NAME}, {LAST_NAME}, {CAREER}, {BIRTH_DATE}, {ENTRY_DATE}, {PLACE_ORIGIN}, {EMAIL}, {ENROLL_QUANTITY}, {PICTURE})"
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


def deleteStudent(connection, id):
    """Delete a student by id in the database:

    Args:
        connection (object): Connection to sqlite3.
        id (int): Id of the student.
    """
    CURSOR_OBJ = connection.cursor()
    DELETE_STATEMENT = "DELETE FROM students WHERE id = ?"
    CURSOR_OBJ.execute(DELETE_STATEMENT, (id,))
    connection.commit()


def updateStudent(connection, studentID):
    """Update a student in the database:

    Args:
        connection (object): Connection to sqlite3.
        student (int): Id of the student.
    """
    CURSOR_OBJ = connection.cursor()
    exitMenuUpdate = False
    error = None
    success = None

    while not exitMenuUpdate:
        CONFIG.clear()
        if error:
            CONFIG.printErrorApp(error)
        error = None
        if success:
            CONFIG.printSuccessApp(success)
        success = None
        UPDATE_MENU = CONFIG.menuUpdateStudent(studentID)
        option = input(UPDATE_MENU)
        if option == '1':
            try:
                newId = int(input("Enter the new id:  "))
                UPDATE_STATEMENT = f"UPDATE students SET id = ? WHERE id = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newId, studentID))
                connection.commit()
                success = f"The id was updated ({newId}) successfully"
            except Exception as e:
                error = "01. ERROR: " + str(e)
        elif option == '2':
            try:
                newName = input("Enter the new name:  ")
                UPDATE_STATEMENT = f"UPDATE students SET name = ? WHERE id = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newName, studentID))
                connection.commit()
                success = f"The name was updated ({newName}) successfully"
            except Exception as e:
                error = "02. ERROR: " + str(e)
        elif option == '3':
            try:
                newLastName = input("Enter the new last name: ")
                UPDATE_STATEMENT = f"UPDATE students SET lastname = ? WHERE id = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newLastName, studentID))
                connection.commit()
                success = f"The last name was updated ({newLastName}) successfully"
            except Exception as e:
                error = "03. ERROR: " + str(e)
        elif option == '4':
            try:
                newCareer = input("Enter the new career: ")
                UPDATE_STATEMENT = f"UPDATE students SET career = ? WHERE id = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newCareer, studentID))
                connection.commit()
                success = f"The career was updated ({newCareer}) successfully"
            except Exception as e:
                error = "04. ERROR: " + str(e)
        elif option == '5':
            try:
                newBornDate = input("Enter the new born date: ")
                UPDATE_STATEMENT = f"UPDATE students SET bornDate = ? WHERE id = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newBornDate, studentID))
                connection.commit()
                success = f"The born date was updated ({newBornDate}) successfully"
            except Exception as e:
                error = "05. ERROR: " + str(e)
        elif option == '6':
            try:
                newEntryDate = input("Enter the new entry date: ")
                UPDATE_STATEMENT = f"UPDATE students SET entryDate = ? WHERE id = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newEntryDate, studentID))
                connection.commit()
                success = f"The entry date was updated ({newEntryDate}) successfully"
            except Exception as e:
                error = "06. ERROR: " + str(e)
        elif option == '7':
            try:
                newPlaceOrigin = input("Enter the new place of origin: ")
                UPDATE_STATEMENT = f"UPDATE students SET placeOrigin = ? WHERE id = ?"
                CURSOR_OBJ.execute(
                    UPDATE_STATEMENT, (newPlaceOrigin, studentID))
                connection.commit()
                success = f"The place of origin was updated ({newPlaceOrigin}) successfully"
            except Exception as e:
                error = "07. ERROR: " + str(e)
        elif option == '8':
            try:
                newEmail = input("Enter the new email: ")
                UPDATE_STATEMENT = f"UPDATE students SET email = ? WHERE id = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newEmail, studentID))
                connection.commit()
                success = f"The email was updated ({newEmail}) successfully"
            except Exception as e:
                error = "08. ERROR: " + str(e)
        elif option == '9':
            try:
                newEnrollQuantity = int(
                    input("Enter the new enroll quantity: "))
                UPDATE_STATEMENT = f"UPDATE students SET enrollQuantity = ? WHERE id = ?"
                CURSOR_OBJ.execute(
                    UPDATE_STATEMENT, (newEnrollQuantity, studentID))
                connection.commit()
                success = f"The enroll quantity was updated ({newEnrollQuantity}) successfully"
            except Exception as e:
                error = "09. ERROR: " + str(e)
        elif option == '10':
            try:
                newPhotograph = input("Enter the new photograph: ")
                UPDATE_STATEMENT = f"UPDATE students SET photograph = ? WHERE id = ?"
                CURSOR_OBJ.execute(
                    UPDATE_STATEMENT, (newPhotograph, studentID))
                connection.commit()
                success = f"The photograph was updated ({newPhotograph}) successfully"
            except Exception as e:
                error = "10. ERROR: " + str(e)
        elif option == '11':
            try:
                newStudent = CONFIG.readDataUserStudent()
                UPDATE_STATEMENT = f"UPDATE students SET id = ?, name = ?, lastname = ?, career = ?, bornDate = ?, entryDate = ?, placeOrigin = ?, email = ?, enrollQuantity = ?, photograph = ? WHERE id = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newStudent[0], newStudent[1], newStudent[2], newStudent[3],
                                                      newStudent[4], newStudent[5], newStudent[6], newStudent[7], newStudent[8], newStudent[9], studentID))
                connection.commit()
                exitMenuUpdate = True
            except Exception as e:
                error = "11. ERROR: " + str(e)
        elif option == '12':
            print("\033[0;31mOperation canceled!\033[0;m")
            exitMenuUpdate = True
        else:
            error = 'ERROR: Invalid option'
