from . import config_app as CONFIG


def createSubjectsTable(connection):
    """Creates the subjects table in the database:

    Args:
        connection (object): Connection to sqlite3.

    """

    CURSOR_OBJ = connection.cursor()
    CODE = "code INTEGER PRIMARY KEY NOT NULL UNIQUE"
    NAME = "name TEXT NOT NULL UNIQUE"
    SCHOOL = "school TEXT"
    DEPARTMENT = "department TEXT"
    CREDITS = "credits TEXT"
    LANGUAGE = "language TEXT"
    CREATE_STATEMENT = f"""CREATE TABLE IF NOT EXISTS subjects(
        {CODE}, {NAME}, {SCHOOL}, {DEPARTMENT}, {CREDITS}, {LANGUAGE}
        )"""
    CURSOR_OBJ.execute(CREATE_STATEMENT)  # creates the table in the database
    connection.commit()  # Ensures persistence by saving the table to disk


def insertSubject(connection, subject):
    """Inserts a subject in the subjects table:

    Args:
        connection (object): Connection to sqlite3.
        subject (tuple): Tuple containing the elements of the Subjects table.

    """
    CURSOR_OBJ = connection.cursor()
    # uses string formatting to replace the ? characters with the elements contained in the subject list
    INSERT_STATEMENT = "INSERT INTO subjects VALUES(?, ?, ?, ?, ?, ?)"
    CURSOR_OBJ.execute(INSERT_STATEMENT, subject)
    connection.commit()


def deleteSubject(connection, id):
    """Delete a subject by id in the database:

    Args:
        connection (object): Connection to sqlite3.
        id (int): Id of the subject.
    """
    CURSOR_OBJ = connection.cursor()
    DELETE_STATEMENT = "DELETE FROM subjects WHERE code = ?"
    CURSOR_OBJ.execute(DELETE_STATEMENT, (id,))
    connection.commit()


def selectSubjectByID(connection, id):
    """Select a subject by id in the database:

    Args:
        connection (object): Connection to sqlite3.
        id (int): Id of the subject.

    Returns:
        list<tuple>: List of tuples with the data of the subjects that contains the id.
    """
    CURSOR_OBJ = connection.cursor()
    SELECT_STATEMENT = "SELECT * FROM subjects WHERE code = ?"
    CURSOR_OBJ.execute(SELECT_STATEMENT, (id,))
    return CURSOR_OBJ.fetchall()


def updateSubject(connection, subjectCode):
    """Update a subject in the database:

    Args:
        connection (object): Connection to sqlite3.
        subject (int): Id of the subject.
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
        UPDATE_MENU = CONFIG.menuUpdateSubject(subjectCode)
        option = input(UPDATE_MENU)
        if option == '1':
            try:
                newCode = int(input("Enter the new code:  "))
                UPDATE_STATEMENT = f"UPDATE subjects SET code = ? WHERE code = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newCode, subjectCode))
                connection.commit()
                success = f"The id was updated ({newCode}) successfully"
                exitMenuUpdate = True
            except Exception as e:
                error = "01. ERROR: " + str(e)
        elif option == '2':
            try:
                newName = input("Enter the new name:  ")
                UPDATE_STATEMENT = f"UPDATE subjects SET name = ? WHERE code = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newName, subjectCode))
                connection.commit()
                success = f"The name was updated ({newName}) successfully"
            except Exception as e:
                error = "02. ERROR: " + str(e)
        elif option == '3':
            try:
                newSchool = input("Enter the new school: ")
                UPDATE_STATEMENT = f"UPDATE subjects SET school = ? WHERE code = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newSchool, subjectCode))
                connection.commit()
                success = f"The school was updated ({newSchool}) successfully"
            except Exception as e:
                error = "03. ERROR: " + str(e)
        elif option == '4':
            try:
                newDepartment = input("Enter the new department: ")
                UPDATE_STATEMENT = f"UPDATE subjects SET department = ? WHERE code = ?"
                CURSOR_OBJ.execute(
                    UPDATE_STATEMENT, (newDepartment, subjectCode))
                connection.commit()
                success = f"The department was updated ({newDepartment}) successfully"
            except Exception as e:
                error = "04. ERROR: " + str(e)
        elif option == '5':
            try:
                newCredits = int(input("Enter the new credits: "))
                UPDATE_STATEMENT = f"UPDATE subjects SET credits = ? WHERE code = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newCredits, subjectCode))
                connection.commit()
                success = f"The credits was updated ({newCredits}) successfully"
            except Exception as e:
                error = "05. ERROR: " + str(e)
        elif option == '6':
            try:
                newLanguage = input("Enter the new language: ")
                UPDATE_STATEMENT = f"UPDATE subjects SET language = ? WHERE code = ?"
                CURSOR_OBJ.execute(
                    UPDATE_STATEMENT, (newLanguage, subjectCode))
                connection.commit()
                success = f"The language was updated ({newLanguage}) successfully"
            except Exception as e:
                error = "06. ERROR: " + str(e)
        elif option == '7':
            try:
                newSubject = CONFIG.readDataUserSubject()
                UPDATE_STATEMENT = f"UPDATE subjects SET code = ?, name = ?, school = ?, department = ?, credits = ?, language = ? WHERE code = ?"
                CURSOR_OBJ.execute(
                    UPDATE_STATEMENT, (newSubject[0], newSubject[1], newSubject[2], newSubject[3], newSubject[4], newSubject[5], subjectCode))
                connection.commit()
                exitMenuUpdate = True
            except Exception as e:
                error = "7. ERROR: " + str(e)
        elif option == '8':
            print("\033[0;31mOperation canceled!\033[0;m")
            exitMenuUpdate = True
        else:
            error = 'ERROR: Invalid option'
