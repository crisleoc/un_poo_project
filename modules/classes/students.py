from .. import config_app as CONFIG
from .Object import object


# This class inherits from the abstract class object
class student(object):

    _connection = None
    _student = None
    _id = None

    def __init__(self): pass

    def createStudentTable(self, connection):
        """Create a table in the database:

        Args:
            connection (object): Connection to sqlite3.
        """
        self._connection = connection
        CURSOR_OBJ = connection.cursor()
        ID = "id INTEGER PRIMARY KEY"
        NAME = "name TEXT"
        LAST_NAME = "lastname TEXT"
        CAREER = "career TEXT"
        BIRTH_DATE = "bornDate TEXT"
        ENTRY_DATE = "entryDate TEXT"
        PLACE_ORIGIN = "placeOrigin TEXT"
        EMAIL = "email TEXT"
        ENROLL_QUANTITY = "enrollQuantity INTEGER"
        PICTURE = "photograph TEXT"
        CREATE_STATEMENT = f"CREATE TABLE IF NOT EXISTS students({ID}, {NAME}, {LAST_NAME}, {CAREER}, {BIRTH_DATE}, {ENTRY_DATE}, {PLACE_ORIGIN}, {EMAIL}, {ENROLL_QUANTITY}, {PICTURE})"
        CURSOR_OBJ.execute(CREATE_STATEMENT)
        connection.commit()  # Ensures persistence

    def insertStudent(self, connection, student):
        """Insert a student in the database:

        Args:
            connection (object): Connection to sqlite3.
            student (tuple): Tuple with the data (10 spaces) of the student.
        """
        self._connection = connection
        self._student = student
        CURSOR_OBJ = connection.cursor()
        INSERT_STATEMENT = "INSERT INTO students VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # Replaces each ? character with its corresponding value inside the student tuple
        CURSOR_OBJ.execute(INSERT_STATEMENT, student)
        connection.commit()

    def selectStudentByID(self, connection, id):
        """Select a student by id in the database:

        Args:
            connection (object): Connection to sqlite3.
            id (int): Id of the student.

        Returns:
            list<tuple>: List of tuples with the data of the students that contains the id.
        """
        self._connection = connection
        self._id = id
        CURSOR_OBJ = connection.cursor()
        # Selects the row inside the students table with the associated id
        SELECT_STATEMENT = "SELECT * FROM students WHERE id = ?"
        CURSOR_OBJ.execute(SELECT_STATEMENT, (id,))
        return CURSOR_OBJ.fetchall()  # Returns a tuple containing all the values of the row

    def selectAllStudents(self, connection):
        """Select all students in the database:

        Args:
            connection (object): Connection to sqlite3.

        Returns:
            list<tuple>: List of tuples with the data of all the students.
        """
        self._connection = connection
        CURSOR_OBJ = connection.cursor()
        SELECT_STATEMENT = "SELECT * FROM students"
        CURSOR_OBJ.execute(SELECT_STATEMENT)
        return CURSOR_OBJ.fetchall()

    def deleteStudent(self, connection, id):
        self._connection = connection
        self._id = id
        """Delete a student by id in the database:

        Args:
            connection (object): Connection to sqlite3.
            id (int): Id of the student.
        """
        CURSOR_OBJ = connection.cursor()
        # Deletes from the DB the row associated with the id
        DELETE_STATEMENT = "DELETE FROM students WHERE id = ?"
        CURSOR_OBJ.execute(DELETE_STATEMENT, (id,))
        connection.commit()

    def updateStudent(self, connection, studentID):
        """Update a student in the database:

        Args:
            connection (object): Connection to sqlite3.
            student (int): Id of the student.
        """
        self._connection = connection
        self._id = studentID
        CURSOR_OBJ = connection.cursor()
        exitMenuUpdate = False  # Changes its value to True when the user closes the menu
        error = None  # Default value of the error value, changes its value when an exception occurs
        success = None  # Default value of the success value, changes its value when the selected method runs successfully

        while not exitMenuUpdate:
            CONFIG.clear()  # Clears the terminal in each iteration
            if error:
                # It's an user interface method that prints out the error message
                CONFIG.printErrorApp(error)
            error = None  # After printing the error the variable switches back to the None value
            if success:
                # It's an user interface method that prints out the success confirmation message
                CONFIG.printSuccessApp(success)
            success = None  # After printing the error the variable switches back to the None value
            # Initiates the Student menu using the ID entered by the user as an argument
            UPDATE_MENU = CONFIG.menuUpdateStudent(studentID)
            option = input(UPDATE_MENU)
            if option == '1':
                try:
                    newName = input("Enter the new name:  ")
                    # Replaces the old name value associated with the entered id with newName
                    UPDATE_STATEMENT = f"UPDATE students SET name = ? WHERE id = ?"
                    # Executes the statement, taking the old and new values as arguments
                    CURSOR_OBJ.execute(UPDATE_STATEMENT, (newName, studentID))
                    connection.commit()
                    # Initiates the success variable using the corresponding success confirmation message
                    success = f"The name was updated ({newName}) successfully"
                except Exception as e:
                    # Should an exception happen, it prints out the exception
                    error = "01. ERROR: " + str(e)
            elif option == '2':
                try:
                    newLastName = input("Enter the new last name: ")
                    UPDATE_STATEMENT = f"UPDATE students SET lastname = ? WHERE id = ?"
                    CURSOR_OBJ.execute(
                        UPDATE_STATEMENT, (newLastName, studentID))
                    connection.commit()
                    success = f"The last name was updated ({newLastName}) successfully"
                except Exception as e:
                    error = "02. ERROR: " + str(e)
            elif option == '3':
                try:
                    newCareer = input("Enter the new career: ")
                    UPDATE_STATEMENT = f"UPDATE students SET career = ? WHERE id = ?"
                    CURSOR_OBJ.execute(
                        UPDATE_STATEMENT, (newCareer, studentID))
                    connection.commit()
                    success = f"The career was updated ({newCareer}) successfully"
                except Exception as e:
                    error = "03. ERROR: " + str(e)
            elif option == '4':
                try:
                    newBornDate = CONFIG.get_data(
                        "Enter the new born date: ", "date")
                    UPDATE_STATEMENT = f"UPDATE students SET bornDate = ? WHERE id = ?"
                    CURSOR_OBJ.execute(
                        UPDATE_STATEMENT, (newBornDate, studentID))
                    connection.commit()
                    success = f"The born date was updated ({newBornDate}) successfully"
                except Exception as e:
                    error = "04. ERROR: " + str(e)
            elif option == '5':
                try:
                    newEntryDate = CONFIG.get_data(
                        "Enter the new entry date: ", "date")
                    UPDATE_STATEMENT = f"UPDATE students SET entryDate = ? WHERE id = ?"
                    CURSOR_OBJ.execute(
                        UPDATE_STATEMENT, (newEntryDate, studentID))
                    connection.commit()
                    success = f"The entry date was updated ({newEntryDate}) successfully"
                except Exception as e:
                    error = "05. ERROR: " + str(e)
            elif option == '6':
                try:
                    newPlaceOrigin = input("Enter the new place of origin: ")
                    UPDATE_STATEMENT = f"UPDATE students SET placeOrigin = ? WHERE id = ?"
                    CURSOR_OBJ.execute(
                        UPDATE_STATEMENT, (newPlaceOrigin, studentID))
                    connection.commit()
                    success = f"The place of origin was updated ({newPlaceOrigin}) successfully"
                except Exception as e:
                    error = "06. ERROR: " + str(e)
            elif option == '7':
                try:
                    newEmail = CONFIG.get_data(
                        "Enter the new email: ", "email")
                    UPDATE_STATEMENT = f"UPDATE students SET email = ? WHERE id = ?"
                    CURSOR_OBJ.execute(UPDATE_STATEMENT, (newEmail, studentID))
                    connection.commit()
                    success = f"The email was updated ({newEmail}) successfully"
                except Exception as e:
                    error = "07. ERROR: " + str(e)
            elif option == '8':
                try:
                    newEnrollQuantity = int(
                        input("Enter the new enroll quantity: "))
                    UPDATE_STATEMENT = f"UPDATE students SET enrollQuantity = ? WHERE id = ?"
                    CURSOR_OBJ.execute(
                        UPDATE_STATEMENT, (newEnrollQuantity, studentID))
                    connection.commit()
                    success = f"The enroll quantity was updated ({newEnrollQuantity}) successfully"
                except Exception as e:
                    error = "08. ERROR: " + str(e)
            elif option == '9':
                try:
                    newPhotograph = input("Enter the new photograph: ")
                    UPDATE_STATEMENT = f"UPDATE students SET photograph = ? WHERE id = ?"
                    CURSOR_OBJ.execute(
                        UPDATE_STATEMENT, (newPhotograph, studentID))
                    connection.commit()
                    success = f"The photograph was updated ({newPhotograph}) successfully"
                except Exception as e:
                    error = "9. ERROR: " + str(e)
            elif option == '10':
                try:
                    newStudent = CONFIG.readDataUserStudent(True)
                    UPDATE_STATEMENT = f"UPDATE students SET name = ?, lastname = ?, career = ?, bornDate = ?, entryDate = ?, placeOrigin = ?, email = ?, enrollQuantity = ?, photograph = ? WHERE id = ?"
                    # Replaces ALL of the values associated with the entered code with newStudent
                    CURSOR_OBJ.execute(UPDATE_STATEMENT, (newStudent[0], newStudent[1], newStudent[2], newStudent[3],
                                                          newStudent[4], newStudent[5], newStudent[6], newStudent[7], newStudent[8], studentID))
                    # Extracts each value of the newStudent tuple and replaces them in the ? characters
                    connection.commit()
                    exitMenuUpdate = True
                except Exception as e:
                    # Should the menu end abruptly, it prints out a warning message
                    error = "10. ERROR: " + str(e)
            elif option == '11':
                # Should the menu end abruptly, it prints out a warning message
                print("\033[0;31mOperation canceled!\033[0;m")
                exitMenuUpdate = True  # Ends the infinite While Not iteration
            else:
                error = 'ERROR: Invalid option'
