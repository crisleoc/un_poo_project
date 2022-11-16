from . import config_app as CONFIG
from .classes import students as STUDENTS


def mainMenuStudents(connection):
    """Function to show the main menu of students:

    Args:
        connection (object): Connection to sqlite3.
    """
    # Create the object student
    objectStudent = STUDENTS.student()

    exitMenuStudents = False
    error = None
    success = None
    select = None
    while not exitMenuStudents:
        CONFIG.clear()
        if error:
            CONFIG.printErrorApp(error)
        error = None
        if success:
            CONFIG.printSuccessApp(success)
        success = None
        if select != None:
            CONFIG.printSelectStudent(select)
        select = None
        STUDENT_MENU = CONFIG.menuStudents()
        option = input(STUDENT_MENU)
        if option == '1':
            try:
                objectStudent.insertStudent(
                    connection, CONFIG.readDataUserStudent())
                success = "01. SUCCESS: Student added successfully"
            except Exception as e:
                error = "01. ERROR: " + str(e)
        elif option == '2':
            try:
                studentID = int(input("Enter the student id: "))
                select = objectStudent.selectStudentByID(connection, studentID)
                success = "02. SUCCESS: Execution finished without errors."
            except Exception as e:
                error = "02. ERROR: " + str(e)
        elif option == '3':
            try:
                studentID = int(input("Enter the student id: "))
                studentExists = objectStudent.selectStudentByID(
                    connection, studentID)
                if studentExists:
                    objectStudent.updateStudent(connection, studentID)
                    success = "03. SUCCESS: Student updated successfully"
                else:
                    raise Exception("Student does not exist")
            except Exception as e:
                error = "03. ERROR: " + str(e)
        elif option == '4':
            try:
                studentID = int(input("Enter the student id: "))
                studentExists = objectStudent.selectStudentByID(
                    connection, studentID)
                if studentExists:
                    objectStudent.deleteStudent(connection, studentID)
                    success = "04. SUCCESS: Student deleted successfully"
                else:
                    raise Exception("Student does not exist")
            except Exception as e:
                error = "04. ERROR: " + str(e)
        elif option == '5':
            print("\033[0;31mOperation canceled!\033[0;m")
            exitMenuStudents = True
        else:
            error = "ERROR: Invalid option"
