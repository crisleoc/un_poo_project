def createSubjectsTable(connection):
    """Creates the subjects table in the database:

    Args:
        connection (object): Connection to sqlite3.

    """

    CURSOR_OBJ = connection.cursor()
    CODE = "id INTEGER PRIMARY KEY NOT NULL UNIQUE"
    NAME = "name TEXT NOT NULL UNIQUE"
    SCHOOL = "school TEXT"
    DEPARTMENT = "department TEXT"
    CREDITS = "credits TEXT"
    LANGUAGE = "language TEXT"
    CREATE_STATEMENT = f"""CREATE TABLE IF NOT EXISTS subjects(
        {CODE}, {NAME}, {SCHOOL}, {DEPARTMENT}, {CREDITS}, {LANGUAGE}
        )"""
    CURSOR_OBJ.execute(CREATE_STATEMENT)
    connection.commit()


def insertSubject(connection, subject):
    """Inserts a subject in the subjects table:

    Args:
        connection (object): Connection to sqlite3.
        subject (tuple): Tuple containing the elements of the Subjects table.

    """
    cursor_obj = connection.cursor()
    # uses string formatting to replace the ? characters with the elements contained in the subject list
    create_statement = "INSERT INTO subject VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor_obj.execute(create_statement, subject)
    connection.commit()


def selectAllSubjects(connection):
    """Returns a list containing all the subjects registered in the Subjects table:

    Args:
        connection (object): Connection to sqlite3.

    Returns:
        list<tuple>: List of tuples with the data of the subjects.
    """
    cursor_obj = connection.cursor()
    create_statement = "SELECT * FROM subjects"
    cursor_obj.execute(create_statement)
    return cursor_obj.fetchall()


def updateSubjects(connection, codmat):
    """Updates and changes the Subjects table's data:

    Args:
        connection (object): Connection to sqlite3.
        codmat (int): Integer that contains the code of a specific subject that we want to modify.

    """
    cursor_obj = connection.cursor()
    exitMenu = False
    while not exitMenu:
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
                create_statement = 'UPDATE subjects SET CODE="' + \
                    newCode+'" WHERE CODE ="'+codmat+'"'
                cursor_obj.execute(create_statement)
                connection.commit()
                print("Subject's code has been modified successfully:")
                opc = input("Press 1 to close the menu, 0 to return >>>: ")
                if opc == '1':
                    exitMenu = True
                else:
                    exitMenu = False
            except:
                print("ERROR: Please enter a valid code")
        elif opc == '2':
            try:
                newNAME = input("Enter a new name: ")
                create_statement = 'UPDATE subjects SET NAME="' + \
                    newNAME+'" WHERE CODE ="'+codmat+'"'
                cursor_obj.execute(create_statement)
                connection.commit()
                print("""Subject's name has been modified successfully""")
                opc = input("Press 1 to close the menu, 0 to return >>>: ")
                if opc == '1':
                    exitMenu = True
                else:
                    exitMenu = False
            except:
                print("ERROR: Please enter a valid input")
        elif opc == '3':
            try:
                newSCHOOL = input("Enter a new school: ")
                create_statement = 'UPDATE subjects SET SCHOOL="' + \
                    newSCHOOL+'" WHERE CODE ="'+codmat+'"'
                cursor_obj.execute(create_statement)
                connection.commit()
                print("""Subject's school has been modified successfully""")
                opc = input("Press 1 to close the menu, 0 to return >>>: ")
                if opc == '1':
                    exitMenu = True
                else:
                    exitMenu = False
            except:
                print("ERROR: Please enter a valid input")
        elif opc == '4':
            try:
                newDEPARTMENT = input("Enter a new department: ")
                create_statement = 'UPDATE subjects SET DEPARTMENT="' + \
                    newDEPARTMENT+'" WHERE CODE ="'+codmat+'"'
                cursor_obj.execute(create_statement)
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
                create_statement = 'UPDATE subjects SET CREDITS="' + \
                    newCREDITS+'" WHERE CODE ="'+codmat+'"'
                cursor_obj.execute(create_statement)
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
                newLANGUAGE = input("Enter a new language: ")
                create_statement = 'UPDATE subjects SET LANGUAGE="' + \
                    newLANGUAGE+'" WHERE CODE ="'+codmat+'"'
                cursor_obj.execute(create_statement)
                connection.commit()
                print("""Subject's language has been modified successfully""")
                opc = input("Press 1 to close the menu, 0 to return >>>: ")
                if opc == '1':
                    exitMenu = True
                else:
                    exitMenu = False
            except:
                print("ERROR: Please enter a valid input")
        elif opc == '7':
            try:
                newID = input("Enter a new code: ")
                newNAME = input("Enter a new name: ")
                newSCHOOL = input("Enter a new school: ")
                newDEPARTMENT = input("Enter a new department: ")
                newCREDITS = input("Enter a new number of credits: ")
                newLANGUAGE = input("Enter a new language: ")
                create_statement = 'UPDATE subjects SET CODE="' + \
                    newID+'", NAME="' + \
                    newNAME+'", SCHOOL="' + \
                    newSCHOOL+'", DEPARTMENT="' + \
                    newDEPARTMENT+'", CREDITS="' + \
                    newCREDITS+'", LANGUAGE="' + \
                    newLANGUAGE+'" WHERE CODE ="'+codmat+'"'
                cursor_obj.execute(create_statement)
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
        else:
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
