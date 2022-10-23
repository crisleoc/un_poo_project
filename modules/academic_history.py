import modules.connect_db as CONNECT_DB

def createAcademicHistoryTable(connection):
    cursorObj = connection.cursor()
    cursorObj.execute('''CREATE TABLE academicHistory(
                                    code integer,
                                    id integer,
                                    finalNote float,
                                    credits integer,

                                    PRIMARY KEY (code, id)
                                    FOREIGN KEY (code) REFERENCES subjects(code),
                                    FOREIGN KEY (id) REFERENCES students(id))''')
    connection.commit()

def addSubject(connection):

    print ('\n\nWelcome! Enter the information to create your academic history\n')
    key = input('Enter the code of the subject to update: ')
    identity = input('Enter the identification number: ')
    cursorObj = connection.cursor()
    
    def useSelect(x):
        cursorObj.execute(x)
        rows = cursorObj.fetchall()
        return rows

    readCode = "SELECT code FROM subjects WHERE code = "+key+""
    rows1 = useSelect(readCode)
    for r in rows1:
        key = str(r[0])
   
    readId = "SELECT id FROM students WHERE id = "+identity+""
    rows2 = useSelect(readId)
    for r in rows2:
        identity = str(r[0])

    if rows1 != [] and rows2 != []:

        validation2 = "SELECT * FROM academicHistory WHERE id = "+identity+" AND code = "+key+""
        rows = useSelect(validation2)
        for r in rows:
            a = str(r[0])
        
        if rows == []:
            
            finalNote = input('Enter your final grade: ')
            credits = str(0)
            readCredits = "SELECT credits FROM subjects WHERE code = "+key+""
            rows = useSelect(readCredits)
            for r in rows:
                credits = str(r[0])
                
            infoSubject = 'INSERT INTO academicHistory VALUES('+key+','+identity+', '+finalNote+','+credits+')'
            cursorObj.execute(infoSubject)
            connection.commit()
            print ('\nSubject successfully added to academic history!')

        else:
            print ('This document already has a grade for this subject!')
    else:
        print('one or both data is incorrect, please check and try again!')
    
def readAcademicHistory(connection):
    
    print ('\n\nWelcome! Enter the information to see your academic history\n')
    identity = input('Enter the identification number: ')
    cursorObj = connection.cursor()
   
    def useSelect(x):
        cursorObj.execute(x)
        rows = cursorObj.fetchall()
        return rows
    
    readHistory = "SELECT * FROM academicHistory WHERE id = "+identity+""
    rows = useSelect(readHistory)

    print ('\nAcademic History: ')
    for r in rows:
        code = r[0]
        finalNote = r[2]
        credits = r[3]
        print ('\nSubject Code: ', code)
        print ('Final Note: ', finalNote)
        print ('Subject Credits: ', credits)

    if rows == []:
        print ('\nEmpty')
        print ('\nThis document does not have an academic history assigned!')

def deleteSubject(connection):

    def checkDelete(x):
        cursorObj.execute(x)
        rows = cursorObj.fetchall()
        return rows

    def modificateHistory(y):
        cursorObj.execute(y)
        connection.commit()

    print ('\n\nwelcome! Enter the information to remove a subject\n')
    code = input('Enter the subject code: ')
    identity = input('Enter the identification number: ')

    cursorObj = connection.cursor()
    readHistory = "SELECT * FROM academicHistory WHERE id == "+identity+" AND code == "+code+""
    rows = checkDelete(readHistory)
    
    for r in rows:
        code = str(r[0])
        finalNote = str(r[2])
        credits = str(r[3])
        print ('\nSubject Code: ', code)
        print ('Final Note: ', finalNote)
        print ('Subject Credits: ', credits)
        
    if rows == []:
        print ('\nThe data entered is incorrect or the subject was already deleted, please check and try again!')
    else:
        print ('\n<- This subject was successfully deleted!')

    deleteHistory = "DELETE FROM academicHistory Where id == "+identity+" AND code == "+code+"" 
    modificateHistory(deleteHistory)

def updateFinalNote(connection):

    def readNew(x):
        cursorObj.execute(x)
        rows = cursorObj.fetchall()
        return rows

    def refreshNote(z):
        cursorObj.execute(z)
        connection.commit()

    print ('\n\nWelcome! Enter the information to update the final note\n')
    code = input('Enter the subject code: ')
    identification = input('Enter the identification number: ')

    cursorObj = connection.cursor()
    readHistory = "SELECT * FROM academicHistory WHERE id == "+identification+" AND code == "+code+""
    rows = readNew(readHistory)

    for r in rows:
            code = str(r[0])
            finalNote = str(r[2])
            credits = str(r[3])
            
    if rows == []:
        print ('\nThe data entered is incorrect, please check and try again!')
    
    else:
        
        newNote = input('Enter the new final note: ')
        updateHistory = "UPDATE academicHistory SET finalNote == "+newNote+" WHERE id == "+identification+" AND code == "+code+""
        refreshNote(updateHistory)
        rows = readNew(readHistory)
        
        for r in rows:
            code = str(r[0])
            finalNote = str(r[2])
            credits = str(r[3])
            print ('\nSubject Code: ', code)
            print ('New final Note: ', finalNote)
            print ('Subject Credits: ', credits)
            print ('\n<- This subject was successfully updated!')

def close_db(connection):
    connection.close()

def eraseAcademicHistoryTable(connection):

    cursorObj = connection.cursor()
    cursorObj.execute('DROP TABLE academicHistory')
    connection.commit()

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
                        5. close_db
                        6. exit
                        7. eraseAcademicHistoryTable
                        8. createSubjectsTable
                        9. createStudentTable
                        
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
        elif mainMenu == '5':
            close_db(my_connection)
            print ('\n\nThe database "academicHistory" has been closed!')
        elif mainMenu == '6':
            leave = True
            print('\n\nProgram closed, see you soon!')
        elif mainMenu == '7':
            eraseAcademicHistoryTable(my_connection)
            print('\n\nThe database "academicHistory" has been dropped!')
        else:
            print('\n\nIs not a valid option, please try again!')