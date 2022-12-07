from . import config_app as CONFIG
from .classes import academic_history as AH


def mainMenuAH(connection):
    """Function to show the main menu of academic history:

    Args:
        connection (object): Connection to sqlite3.
    """

    objectAH = AH.academicHistory()

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
                message = objectAH.addSubject(connection)
            except Exception as e:
                error = "01. ERROR: " + str(e)
        elif option == '2':
            try:
                identity = input('Enter the identification number: ')
                select = objectAH.queryAcademicHistory(connection, identity)
            except Exception as e:
                error = "02. ERROR: " + str(e)
        elif option == '3':
            try:
                message = objectAH.updateFinalNote(connection)
            except Exception as e:
                error = "03. ERROR: " + str(e)
        elif option == '4':
            try:
                message = objectAH.deleteSubject(connection)
            except Exception as e:
                error = "04. ERROR: " + str(e)
        elif option == '5':
            print("\033[0;31mOperation canceled!\033[0;m")
            exitMenuAH = True
        else:
            error = "ERROR: Invalid option"
