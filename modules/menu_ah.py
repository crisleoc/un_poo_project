from . import config_app as CONFIG
from . import academic_history as AH


def mainMenuAH(connection):
    """Function to show the main menu of students:

    Args:
        connection (object): Connection to sqlite3.
    """
    exitMenuAH = False
    error = None
    message = None
    select = None
    while not exitMenuAH:
        CONFIG.clear()
        if error:
            CONFIG.printErrorApp(error)
        error = None
        if message:
            CONFIG.printMessageApp(message)
        message = None
        if select != None:
            CONFIG.printSelectAH(select)
        select = None
        AH_MENU = CONFIG.menuAcademicHistory()
        option = input(AH_MENU)
        if option == '1':
            try:
                message = AH.addSubject(connection)
            except Exception as e:
                error = "01. ERROR: " + str(e)
        elif option == '2':
            try:
                select = AH.readAcademicHistory(connection)
            except Exception as e:
                error = "02. ERROR: " + str(e)
        elif option == '3':
            try:
                message = AH.updateFinalNote(connection)
            except Exception as e:
                error = "03. ERROR: " + str(e)
        elif option == '4':
            try:
                message = AH.deleteSubject(connection)
            except Exception as e:
                error = "04. ERROR: " + str(e)
        elif option == '5':
            print("\033[0;31mOperation canceled!\033[0;m")
            exitMenuAH = True
        else:
            error = "ERROR: Invalid option"