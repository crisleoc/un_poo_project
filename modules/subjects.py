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


def readDataUserSubject():
    code = input("insert the subject code: ")
    name = input("insert the subject name: ")
    school = input("insert the school the subject belongs to: ")
    department = input(
        "select the department to which the subject belongs to: ")
    credits = input("write how many credits the subject is worth: ")
    language = input("in what language will the subject be dictated?: ")
    subject = (code, name, school, department, credits, language)
    return subject


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


def updateSubjects(connection, codmat):
    """Updates and changes the Subjects table's data:

    Args:
        connection (object): Connection to sqlite3.
        codmat (int): Integer that contains the code of a specific subject that we want to modify.

    """
    CURSOR_OBJ = connection.cursor()
    exitMenu = False
    while not exitMenu:  # starts an infitite while not iteration. Stops when exitMenu = True.
        opc = input("""
        Option's Menu:
        1. Modify Code
        2. Modify Name
        3. Modify School
        4. Modify Department
        5. Modify Credits
        6. Modify Language
        7. Modify Everything

        0. Exit

        Enter Option>>>: """)
        print("You entered: "+opc)
        if opc == '1':
            try:
                newCode = input("Enter a new code: ")
                # searches in the table for the code that the user entered and replaces it with a new one
                create_statement = 'UPDATE subjects SET CODE="' + \
                    newCode+'" WHERE CODE ="'+codmat+'"'
                CURSOR_OBJ.execute(create_statement)
                connection.commit()  # persistence ensurance
                print("Subject's code has been modified successfully:")
                opc = input("Press 1 to close the menu, 0 to return >>>: ")
                if opc == '1':
                    exitMenu = True
                else:
                    exitMenu = False
            except:  # if the code is not regitered in the table, prints an error message and the iteration continues
                print("ERROR: Please enter a valid code")
        elif opc == '2':
            try:
                newNAME = input("Enter a new name: ")
                # searches in the table for the code that the user entered and replaces the name associated with it
                create_statement = 'UPDATE subjects SET NAME="' + \
                    newNAME+'" WHERE CODE ="'+codmat+'"'
                CURSOR_OBJ.execute(create_statement)
                connection.commit()
                print("""Subject's name has been modified successfully""")
                opc = input("Press 1 to close the menu, 0 to return >>>: ")
                if opc == '1':
                    exitMenu = True
                else:
                    exitMenu = False
            except:  # if the code is not regitered in the table, prints an error message and the iteration continues
                print("ERROR: Please enter a valid input")
        elif opc == '3':
            try:
                newSCHOOL = input("Enter a new school: ")
                # searches in the table for the code that the user entered and replaces the school associated with it
                create_statement = 'UPDATE subjects SET SCHOOL="' + \
                    newSCHOOL+'" WHERE CODE ="'+codmat+'"'
                CURSOR_OBJ.execute(create_statement)
                connection.commit()
                print("""Subject's school has been modified successfully""")
                opc = input("Press 1 to close the menu, 0 to return >>>: ")
                if opc == '1':
                    exitMenu = True
                else:
                    exitMenu = False
            except:  # if the code is not regitered in the table, prints an error message and the iteration continues
                print("ERROR: Please enter a valid input")
        elif opc == '4':
            try:
                newDEPARTMENT = input("Enter a new department: ")
                # searches in the table for the code that the user entered and replaces the department associated with it
                create_statement = 'UPDATE subjects SET DEPARTMENT="' + \
                    newDEPARTMENT+'" WHERE CODE ="'+codmat+'"'
                CURSOR_OBJ.execute(create_statement)
                connection.commit()
                print("""Subject's department has been modified successfully""")
                opc = input("Press 1 to close the menu, 0 to return >>>: ")
                if opc == '1':
                    exitMenu = True
                else:
                    exitMenu = False
            except:
                print("ERROR: Please enter a valid input")
        elif opc == '5':
            try:
                newCREDITS = input(
                    "Enter a new number of credits: ")
                # searches in the table for the code that the user entered and replaces the number of credits associated with it
                create_statement = 'UPDATE subjects SET CREDITS="' + \
                    newCREDITS+'" WHERE CODE ="'+codmat+'"'
                CURSOR_OBJ.execute(create_statement)
                connection.commit()
                print("""Subject's credits has been modified successfully""")
                opc = input("Press 1 to close the menu, 0 to return >>>: ")
                if opc == '1':
                    exitMenu = True
                else:
                    exitMenu = False
            except:
                print("ERROR: Please enter a valid input")
        elif opc == '6':
            try:
                # searches in the table for the code that the user entered and replaces the language associated with it
                newLANGUAGE = input("Enter a new language: ")
                create_statement = 'UPDATE subjects SET LANGUAGE="' + \
                    newLANGUAGE+'" WHERE CODE ="'+codmat+'"'
                CURSOR_OBJ.execute(create_statement)
                connection.commit()
                print("""Subject's language has been modified successfully""")
                opc = input("Press 1 to close the menu, 0 to return >>>: ")
                if opc == '1':
                    exitMenu = True
                else:
                    exitMenu = False
            except:  # if the code is not regitered in the table, prints an error message and the iteration continues
                print("ERROR: Please enter a valid input")
        elif opc == '7':
            try:  # replaces every single value of a row using the code entered by the user
                newCODE = input("Enter a new code: ")
                newNAME = input("Enter a new name: ")
                newSCHOOL = input("Enter a new school: ")
                newDEPARTMENT = input("Enter a new department: ")
                newCREDITS = input("Enter a new number of credits: ")
                newLANGUAGE = input("Enter a new language: ")
                create_statement = 'UPDATE subjects SET CODE="' + \
                    newCODE+'", NAME="' + \
                    newNAME+'", SCHOOL="' + \
                    newSCHOOL+'", DEPARTMENT="' + \
                    newDEPARTMENT+'", CREDITS="' + \
                    newCREDITS+'", LANGUAGE="' + \
                    newLANGUAGE+'" WHERE CODE ="'+codmat+'"'
                CURSOR_OBJ.execute(create_statement)
                connection.commit()
                print("""Subject's data has been modified successfully""")
                opc = input("Press 1 to close the menu, 0 to return >>>: ")
                if opc == '1':
                    exitMenu = True
                else:
                    exitMenu = False
            except:
                print("ERROR: Please enter a valid input")
        elif opc == '0':
            exitMenu = True
        else:  # prints out an error message if the input is not a valid option. The iteration continues
            print("ERROR: Enter a valid option")
    connection.commit()


def querySubjects(connection, codmat):
    """Queries a specific subject using its code as reference:

    Args:
        connection (object): Connection to sqlite3.
        codmat (int): Integer that contains the code of a specific subject that we want to query.

    """
    count = 0  # allows extracting the first index of all the rows inside the dataList list
    rowIsFound = False  # changes its value to True if the Code entered by the user matches one of the codes registered in the table
    cursorObj = connection.cursor()
    # extracts all the rows from the subjects table and puts it in the dataList
    cursorObj.execute("SELECT * FROM subjects")
    dataList = cursorObj.fetchall()
    for row in dataList:
        # if the entered code exists inside the table, prints the row associated with the code
        if codmat == int(dataList[count][0]):
            print(row)
            rowIsFound = True
            break  # breaks the for iteration when the row has been found
        else:
            count += 1
            continue
    if rowIsFound == False:  # if its value's still false after iterating through all the rows of the table, it prints an error message
        print(
            "ERROR: The subject doesn't exist/ Code you entered isn't linked to any subject")
    return dataList


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
