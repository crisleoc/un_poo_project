from . import config_app as CONFIG
from .classes import subjects as SUBJECTS


def mainMenuSubjects(connection):
    """Function to show the main menu of subjects:

    Args:
        connection (object): Connection to sqlite3.
    """

    objectSubject = SUBJECTS.subject()

    exitMenuSubjects = False
    error = None
    success = None
    select = None
    while not exitMenuSubjects:
        CONFIG.clear()
        if error:
            CONFIG.printErrorApp(error)
        error = None
        if success:
            CONFIG.printSuccessApp(success)
        success = None
        if select != None:
            CONFIG.printSelectSubject(select)
        select = None
        SUBJECT_MENU = CONFIG.menuSubjects()
        option = input(SUBJECT_MENU)
        if option == '1':
            try:
                objectSubject.insertSubject(
                    connection, CONFIG.readDataUserSubject())
                success = "01. SUCCESS: Subject added successfully"
            except Exception as e:
                error = "01. ERROR: " + str(e)
        elif option == '2':
            try:
                subjectCode = int(input("Enter the subject code: "))
                select = objectSubject.selectSubjectByID(
                    connection, subjectCode)
                success = "02. SUCCESS: Execution finished without errors."
            except Exception as e:
                error = "02. ERROR: " + str(e)
        elif option == '3':
            try:
                subjectCode = int(input("Enter the subject code: "))
                subjectExists = objectSubject.selectSubjectByID(
                    connection, subjectCode)
                if subjectExists:
                    objectSubject.updateSubject(connection, subjectCode)
                    success = "03. SUCCESS: Subject updated successfully"
                else:
                    raise Exception("Subject does not exist")
            except Exception as e:
                error = "03. ERROR: " + str(e)
        elif option == '4':
            try:
                subjectCode = int(input("Enter the subject code: "))
                subjectExists = objectSubject.selectSubjectByID(
                    connection, subjectCode)
                if subjectExists:
                    objectSubject.deleteSubject(connection, subjectCode)
                    success = "04. SUCCESS: Subject deleted successfully"
                else:
                    raise Exception("Subject does not exist")
            except Exception as e:
                error = "04. ERROR: " + str(e)
        elif option == '5':
            print("\033[0;31mOperation canceled!\033[0;m")
            exitMenuSubjects = True
        else:
            error = "ERROR: Invalid option"
