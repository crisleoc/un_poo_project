from . import config_app as CONFIG
from . import menu_students as MENU_STUDENTS
from . import menu_subjects as MENU_SUBJECTS
from . import menu_ah as MENU_ACADEMIC_HISTORY
from . import menu_classify as MENU_CLASSIFY
from . connect_db import fillDB


def mainMenu(connection):
    """Function to show the main menu of the application:

    Args:
    connection (object): Connection to sqlite3.
    """

    exitMenu = False
    error = None
    success = None
    while not exitMenu:  # an infinite while not iteration. Prints out the main menu options, every option is a table that the user can modify.
        CONFIG.clear()
        if error:
            CONFIG.printErrorApp(error)
        error = None
        if success:
            CONFIG.printSuccessApp(success)
        success = None
        MAIN_MENU = CONFIG.menuMain()
        option = input(MAIN_MENU)
        if option == '0':
            try:
                fillDB()
                success = "00. SUCCESS: Database filled with test data."
            except Exception as e:
                error = "00. ERROR: " + str(e)
        elif option == '1':  # starts another infinite iteration for each option; prints a submenu that allows the calling of the methods of the tables
            MENU_SUBJECTS.mainMenuSubjects(connection)
        elif option == '2':
            MENU_STUDENTS.mainMenuStudents(connection)
        elif option == '3':
            MENU_ACADEMIC_HISTORY.mainMenuAH(connection)
        elif option == '4':
            MENU_CLASSIFY.mainMenuClassify(connection)
        elif option == '5':  # exits the main menu if the input is 5
            print("\033[0;31mDone!\033[0;m")
            exitMenu = True
        else:  # prints out an error message. The main menu iteration continues
            error = "ERROR: Invalid option"
