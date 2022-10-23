import modules.connect_db as CONNECT_DB
 
def createAcademicHistoryTable(connection):
    """Create the academicHistory table in the database:
    Args:
        connection (object): Connection to sqlite3.
    """
    cursorObj = connection.cursor()#We traverse the database with the object cursorObj
    cursorObj.execute('''CREATE TABLE academicHistory(
                                    code integer,
                                    id integer,
                                    finalNote float,
                                    credits integer,
                                    PRIMARY KEY (code, id)
                                    FOREIGN KEY (code) REFERENCES subjects(code),
                                    FOREIGN KEY (id) REFERENCES students(id))''')#We create the table academicHistory
    connection.commit()#We ensure persistence by saving the table to disk

def addSubject(connection):
    """The add Subject function adds subjects to the academic History table.
    Args:
        connection (object): Connection to sqlite3.
    Returns:
        list<tuple>: List of tuples with the result of the process of adding subjects
    """
    print ('\n\nWelcome! Enter the information to create your academic history\n')
    key = input('Enter the code of the subject to update: ')
    identity = input('Enter your identity document: ')
    cursorObj = connection.cursor()#We traverse the database with the object cursorObj
    
    def useSelect(x):
        cursorObj.execute(x)#We consult the information in the academicHistory table
        rows = cursorObj.fetchall()#Read the registers in memory and return a list
        return rows

    readCode = "SELECT code FROM subjects WHERE code = "+key+""
    rows1 = useSelect(readCode)#We call the function that executes the SELECT
    for r in rows1:
        key = str(r[0])
   
    readId = "SELECT id FROM students WHERE id = "+identity+""
    rows2 = useSelect(readId)#We call the function that executes the SELECT
    for r in rows2:
        identity = str(r[0])

    if rows1 != [] and rows2 != []:

        validation2 = "SELECT * FROM academicHistory WHERE id = "+identity+" AND code = "+key+""
        rows = useSelect(validation2)#We call the function that executes the SELECT
        for r in rows:
            a = str(r[0])
        
        if rows == []:
            
            finalNote = input('Enter your final grade: ')
            credits = str(0)
            readCredits = "SELECT credits FROM subjects WHERE code = "+key+""
            rows = useSelect(readCredits)
            for r in rows:
                credits = str(r[0])
                
            infoSubject = 'INSERT INTO academicHistory VALUES('+key+','+identity+', '+finalNote+','+credits+')'#We assign the INSERT function to the infoSubject variable, and we relate the requested information with the corresponding field of the academicHistory table
            cursorObj.execute(infoSubject)#We insert the information in the academicHistory table
            connection.commit()#We ensure persistence by saving the table to disk
            print ('\nSubject successfully added to academic history!')

        else:
            print ('This document already has a grade for this subject!')
    else:
        print('one or both data is incorrect, please check and try again!')
    
def readAcademicHistory(connection):
    """The readAcademicHistory function queries the academicHistory table for information.
    Args:
        connection (object): Connection to sqlite3.
    Returns:
        list<tuple>: List of tuples with the data of the academic History.
    """
    print ('\n\nWelcome! Enter the information to see your academic history\n')
    identity = input('Enter the identification number: ')
    cursorObj = connection.cursor()#We traverse the database with the object cursorObj
   
    def useSelect(x):
        cursorObj.execute(x)#We consult the information in the academicHistory table
        rows = cursorObj.fetchall()#Read the registers in memory and return a list
        return rows
    
    readHistory = "SELECT * FROM academicHistory WHERE id = "+identity+""
    rows = useSelect(readHistory)#We call the function that executes the SELECT

    print ('\nAcademic History: ')
    for r in rows:#The for loop runs through the database and returns the information requested through the corresponding indices
        code = r[0]
        finalNote = r[2]
        credits = r[3]
        print ('\nSubject Code: ', code)
        print ('Final Note: ', finalNote)
        print ('Subject Credits: ', credits)

    if rows == []:#The conditional if verifies that the list is empty, and prints an incident message for the entered document
        print ('\nEmpty')
        print ('\nThis document does not have an academic history assigned!')

def deleteSubject(connection):
    """The function deleteSubject delete a subject that is registered in academicHistory
    Args:
        connection (object): Connection to sqlite3.
    """
    def checkDelete(x):
        cursorObj.execute(x)#We consult the information in the academicHistory table
        rows = cursorObj.fetchall()#Read the registers in memory and return a list
        return rows

    def modificateHistory(y):
        cursorObj.execute(y)#Delete the information in the academicHistory table
        connection.commit()#We ensure persistence by saving the table to disk

    print ('\n\nwelcome! Enter the information to remove a subject\n')
    code = input('Enter the subject code: ')
    identity = input('Enter the identification number: ')

    cursorObj = connection.cursor()#We traverse the database with the object cursorObj
    readHistory = "SELECT * FROM academicHistory WHERE id == "+identity+" AND code == "+code+""
    rows = checkDelete(readHistory)# We call the function that executes the SELECT
    
    for r in rows:#The for loop goes through the database and returns the information of the deleted subject
        code = str(r[0])
        finalNote = str(r[2])
        credits = str(r[3])
        print ('\nSubject Code: ', code)
        print ('Final Note: ', finalNote)
        print ('Subject Credits: ', credits)
        
    if rows == []:#The conditional if verifies that the list is empty, and prints an incident message with the entered document
        print ('\nThe data entered is incorrect or the subject was already deleted, please check and try again!')
    else:
        print ('\n<- This subject was successfully deleted!')

    deleteHistory = "DELETE FROM academicHistory Where id == "+identity+" AND code == "+code+""
    modificateHistory(deleteHistory)#The modificateHistory function executes the DELETE

def updateFinalNote(connection):
    """The updateFinalNote function updates the final grade of a subject in the academicHistory table.
    Args:
        connection (object): Connection to sqlite3.
    """
    def readNew(x):
        cursorObj.execute(x)#We consult the information in the academicHistory table
        rows = cursorObj.fetchall()#Read the registers in memory and return a list
        return rows

    def refreshNote(z):
        cursorObj.execute(z)#We update the information in the academic History table
        connection.commit()#We ensure persistence by saving the table to disk

    print ('\n\nWelcome! Enter the information to update the final note\n')
    code = input('Enter the subject code: ')
    identification = input('Enter the identification number: ')

    cursorObj = connection.cursor()#We traverse the database with the object cursorObj
    readHistory = "SELECT * FROM academicHistory WHERE id == "+identification+" AND code == "+code+""
    rows = readNew(readHistory)

    for r in rows:#The for loop goes through the database and returns the requested elements
            code = str(r[0])
            finalNote = str(r[2])
            credits = str(r[3])
            
    if rows == []:#The conditional if verifies that the list is empty, and prints an incident message for the entered document
        print ('\nThe data entered is incorrect, please check and try again!')
    
    else:
        
        newNote = input('Enter the new final note: ')#We request the new note to the user to perform the correct update
        updateHistory = "UPDATE academicHistory SET finalNote == "+newNote+" WHERE id == "+identification+" AND code == "+code+""
        refreshNote(updateHistory)# We call the function that executes the UPDATE
        rows = readNew(readHistory)#We call the function that executes the SELECT
        
        for r in rows:#The for loop goes through the database and returns the subject information with the updated grade
            code = str(r[0])
            finalNote = str(r[2])
            credits = str(r[3])
            print ('\nSubject Code: ', code)
            print ('New final Note: ', finalNote)
            print ('Subject Credits: ', credits)
            print ('\n<- This subject was successfully updated!')

def menu():

    my_connection = CONNECT_DB.connectionToDB()

    leave = False
    while not leave:
        mainMenu = input('''

                        Main Menu

                        0. createAcademicHistoryTable
                        1. addSubject
                        2. readAcademicHistory
                        3. deleteSubject
                        4. updateFinalNote
                    
                        select an option >>>: ''')
        
        if mainMenu == '0':
            createAcademicHistoryTable(my_connection)
            print('\n\nTable "academicHistory" created successfully')
        elif mainMenu == '1':
            addSubject (my_connection)
        elif mainMenu == '2':
            readAcademicHistory (my_connection)
        elif mainMenu == '3':
            deleteSubject(my_connection)
        elif mainMenu == '4':
            updateFinalNote(my_connection)
        else:
            print('\n\nIs not a valid option, please try again!')