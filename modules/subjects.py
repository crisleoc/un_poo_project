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
    # replaces the ? characters in the INSERT_STATEMENT with a corresponding subject tuple's value
    CURSOR_OBJ.execute(INSERT_STATEMENT, subject)
    connection.commit()  # Ensures persistence


def deleteSubject(connection, id):
    """Delete a subject by id in the database:

    Args:
        connection (object): Connection to sqlite3.
        id (int): Id of the subject.
    """
    CURSOR_OBJ = connection.cursor()
    DELETE_STATEMENT = "DELETE FROM subjects WHERE code = ?"
    # Deletes the subject using its code as reference
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
    return CURSOR_OBJ.fetchall()  # Returns the row as a tuple


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
        CONFIG.clear()  # Clears the terminal at the start of every iteration
        if error:
            # If an error occurs, prints out the corresponding error message
            CONFIG.printErrorApp(error)
        error = None  # Clears the error variable of any value
        if success:
            # If the selected method runs successfully, prints out a confirmation message
            CONFIG.printSuccessApp(success)
        success = None  # Clears the success variable of any value
        # Receives the code entered by the user, creating the subject menu for that code
        UPDATE_MENU = CONFIG.menuUpdateSubject(subjectCode)
        # Prints the subject menu, and receives an option entered by the user.
        option = input(UPDATE_MENU)
        if option == '1':
            try:  # Try Except statement for exception handling
                newCode = int(input("Enter the new code:  "))
                # Replaces the old code with a new one entered by the user
                UPDATE_STATEMENT = f"UPDATE subjects SET code = ? WHERE code = ?"
                # Executes the statement, taking the old and new codes as arguments
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newCode, subjectCode))
                connection.commit()  # Ensures persistence in the data base
                # Initiates the success variable using the corresponding success confirmation message
                success = f"The id was updated ({newCode}) successfully"
            except Exception as e:
                # Should an exception happen, it prints out the exception
                error = "01. ERROR: " + str(e)
        elif option == '2':
            try:  # Try Except statement for exception handling
                newName = input("Enter the new name:  ")
                # Replaces the old name value associated with the entered code with newName
                UPDATE_STATEMENT = f"UPDATE subjects SET name = ? WHERE code = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newName, subjectCode))
                connection.commit()
                # Initiates the success variable using the corresponding success confirmation message
                success = f"The name was updated ({newName}) successfully"
            except Exception as e:
                # Should an exception happen, it prints out the exception
                error = "02. ERROR: " + str(e)
        elif option == '3':
            try:  # Try Except statement for exception handling
                newSchool = input("Enter the new school: ")
                # Replaces the old school value associated with the entered code with newSchool
                UPDATE_STATEMENT = f"UPDATE subjects SET school = ? WHERE code = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newSchool, subjectCode))
                connection.commit()
                success = f"The school was updated ({newSchool}) successfully"
            except Exception as e:
                error = "03. ERROR: " + str(e)
        elif option == '4':
            try:  # Try Except statement for exception handling
                newDepartment = input("Enter the new department: ")
                # Replaces the old department value associated with the entered code with newDepartment
                UPDATE_STATEMENT = f"UPDATE subjects SET department = ? WHERE code = ?"
                CURSOR_OBJ.execute(
                    UPDATE_STATEMENT, (newDepartment, subjectCode))
                connection.commit()
                success = f"The department was updated ({newDepartment}) successfully"
            except Exception as e:
                error = "04. ERROR: " + str(e)
        elif option == '5':
            try:  # Try Except statement for exception handling
                newCredits = int(input("Enter the new credits: "))
                # Replaces the old credits value associated with the entered code with newCredits
                UPDATE_STATEMENT = f"UPDATE subjects SET credits = ? WHERE code = ?"
                CURSOR_OBJ.execute(UPDATE_STATEMENT, (newCredits, subjectCode))
                connection.commit()
                success = f"The credits was updated ({newCredits}) successfully"
            except Exception as e:
                error = "05. ERROR: " + str(e)
        elif option == '6':
            try:  # Try Except statement for exception handling
                newLanguage = input("Enter the new language: ")
                # Replaces the old language value associated with the entered code with newLanguage
                UPDATE_STATEMENT = f"UPDATE subjects SET language = ? WHERE code = ?"
                CURSOR_OBJ.execute(
                    UPDATE_STATEMENT, (newLanguage, subjectCode))
                connection.commit()
                success = f"The language was updated ({newLanguage}) successfully"
            except Exception as e:
                error = "06. ERROR: " + str(e)
        elif option == '7':
            try:  # Try Except statement for exception handling
                newSubject = CONFIG.readDataUserSubject()
                # Replaces ALL of the values associated with the entered code with newSubject
                UPDATE_STATEMENT = f"UPDATE subjects SET code = ?, name = ?, school = ?, department = ?, credits = ?, language = ? WHERE code = ?"
                CURSOR_OBJ.execute(
                    UPDATE_STATEMENT, (newSubject[0], newSubject[1], newSubject[2], newSubject[3], newSubject[4], newSubject[5], subjectCode))  # Extracts each value of the newSubject tuple and replaces them in the ? characters
                connection.commit()
                exitMenuUpdate = True
            except Exception as e:
                error = "7. ERROR: " + str(e)
        elif option == '8':
            # Should the menu end abruptly, it prints out a warning message
            print("\033[0;31mOperation canceled!\033[0;m")
            exitMenuUpdate = True  # Ends the infinite While Not iteration
        else:
            error = 'ERROR: Invalid option'
