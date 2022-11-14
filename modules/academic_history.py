class academicHistory:
    
    def __init__(self):
        """this is the constructor method for the academic history class
        """
        code = None
        id = None
        finalNote = None
        credits = None    # we declare the attributes that have the class with a None value each
    
    def createAcademicHistoryTable(self, connection):
        """Create the academicHistory table in the database:
        Args:
            connection (object): Connection to sqlite3.
        """
        cursorObj = connection.cursor()  # We traverse the database with the object cursorObj
        cursorObj.execute('''CREATE TABLE IF NOT EXISTS academicHistory(
            code integer,
            id integer,
            finalNote float,
            credits integer,
            PRIMARY KEY (code, id)
            FOREIGN KEY (code) REFERENCES subjects(code),
            FOREIGN KEY (id) REFERENCES students(id))''')  # We create the table academicHistory
        connection.commit()  # We ensure persistence by saving the table to disk


    def addSubject(self, connection):
        """The add Subject function adds subjects to the academic History table.
        Args:
            connection (object): Connection to sqlite3.
        Returns:
            list<tuple>: List of tuples with the result of the process of adding subjects
        """
        key = input('Enter the code of the subject to update: ')
        identity = input('Enter your identity document: ')
        # We traverse the database with the object cursorObj
        cursorObj = connection.cursor()
        try:  # validates that input errors do not break the program
            def useSelect(x):
                # We consult the information in the academicHistory table
                cursorObj.execute(x)
                rows = cursorObj.fetchall()  # Read the registers in memory and return a list
                return rows
            readCode = "SELECT code FROM subjects WHERE code = "+key+""
            # We call the function that executes the SELECT
            rows1 = useSelect(readCode)
            for r in rows1:
                key = str(r[0])
            readId = "SELECT id FROM students WHERE id = "+identity+""
            # We call the function that executes the SELECT
            rows2 = useSelect(readId)
            for r in rows2:
                identity = str(r[0])
            if rows1 != [] and rows2 != []:
                validation2 = "SELECT * FROM academicHistory WHERE id = " + \
                    identity+" AND code = "+key+""
                # We call the function that executes the SELECT
                rows = useSelect(validation2)
                if rows == []:
                    finalNote = input('Enter your final grade: ')
                    # validate the str and it doesn't matter if the user writes the data with a comma or period
                    finalNote = finalNote.replace(',', '.')
                    credits = str(0)
                    readCredits = "SELECT credits FROM subjects WHERE code = "+key+""
                    rows = useSelect(readCredits)
                    for r in rows:
                        credits = str(r[0])
                    # We assign the INSERT function to the infoSubject variable, and we relate the requested information with the corresponding field of the academicHistory table
                    infoSubject = 'INSERT INTO academicHistory VALUES(' + \
                        key+','+identity+', '+finalNote+','+credits+')'
                    # We insert the information in the academicHistory table
                    cursorObj.execute(infoSubject)
                    connection.commit()  # We ensure persistence by saving the table to disk
                    return 'Subject successfully added to academic history!'
                else:
                    return 'This document already has a grade for this subject!'
            else:
                return 'One or both data is incorrect, please check and try again!'
        except:
            return 'ERROR: Please enter a valid input'


    def queryAcademicHistory(self, connection):
        """The queryAcademicHistory function queries the academicHistory table for information.
        Args:
            connection (object): Connection to sqlite3.
        Returns:
            list<tuple>: List of tuples with the data of the academic History.
        """
        try:  # validates that input errors do not break the program
            identity = input('Enter the identification number: ')
            # We traverse the database with the object cursorObj
            cursorObj = connection.cursor()

            def useSelect(x):
                # We consult the information in the academicHistory table
                cursorObj.execute(x)
                rows = cursorObj.fetchall()  # Read the registers in memory and return a list
                return rows

            readHistory = "SELECT * FROM academicHistory WHERE id = "+identity+""
            # We call the function that executes the SELECT
            rows = useSelect(readHistory)
            return rows
        except:
            return 'ERROR: Please enter a valid input'


    def deleteSubject(self, connection):
        """The function deleteSubject delete a subject that is registered in academicHistory
        Args:
            connection (object): Connection to sqlite3.
        """
        try:  # validates that input errors do not break the program
            def checkDelete(x):
                # We consult the information in the academicHistory table
                cursorObj.execute(x)
                rows = cursorObj.fetchall()  # Read the registers in memory and return a list
                return rows

            def modificateHistory(y):
                # Delete the information in the academicHistory table
                cursorObj.execute(y)
                connection.commit()  # We ensure persistence by saving the table to disk

            code = input('Enter the subject code: ')
            identity = input('Enter the identification number: ')
            # We traverse the database with the object cursorObj
            cursorObj = connection.cursor()
            readHistory = "SELECT * FROM academicHistory WHERE id == " + \
                identity+" AND code == "+code+""
            # We call the function that executes the SELECT
            rows = checkDelete(readHistory)
            deleteHistory = "DELETE FROM academicHistory Where id == " + \
                identity+" AND code == "+code+""
            # The modificateHistory function executes the DELETE
            modificateHistory(deleteHistory)
            if rows == []:  # The conditional if verifies that the list is empty, and prints an incident message with the entered document
                return 'The data entered is incorrect or the subject was already deleted, please check and try again!'
            else:
                return 'This subject was successfully deleted!'
        except:
            return 'ERROR: Please enter a valid input'


    def updateFinalNote(self, connection):
        """The updateFinalNote function updates the final grade of a subject in the academicHistory table.
        Args:
            connection (object): Connection to sqlite3.
        """
        try:  # validates that input errors do not break the program
            def readNew(x):
                # We consult the information in the academicHistory table
                cursorObj.execute(x)
                rows = cursorObj.fetchall()  # Read the registers in memory and return a list
                return rows

            def refreshNote(z):
                # We update the information in the academic History table
                cursorObj.execute(z)
                connection.commit()  # We ensure persistence by saving the table to disk

            code = input('Enter the subject code: ')
            identification = input('Enter the identification number: ')
            # We traverse the database with the object cursorObj
            cursorObj = connection.cursor()
            readHistory = "SELECT * FROM academicHistory WHERE id == " + \
                identification+" AND code == "+code+""
            rows = readNew(readHistory)
            if rows == []:  # The conditional if verifies that the list is empty, and prints an incident message for the entered document
                return 'The data entered is incorrect, please check and try again!'
            else:
                # We request the new note to the user to perform the correct update
                newNote = input('Enter the new final note: ')
                # validate the str and it doesn't matter if the user writes the data with a comma or period
                newNote = newNote.replace(',', '.')
                updateHistory = "UPDATE academicHistory SET finalNote == " + \
                    newNote+" WHERE id == "+identification+" AND code == "+code+""
                # We call the function that executes the UPDATE
                refreshNote(updateHistory)
                return 'The subject was successfully updated!'
        except:
            return 'ERROR: Please enter a valid input'
