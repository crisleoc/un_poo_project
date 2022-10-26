import modules.connect_db as CONNECT_DB
import modules.students as STUDENTS
import modules.subjects as SUBJECTS
import modules.classification as CLASSIFY
import modules.academic_history as ACADEMIC_HISTORY
from . import config_app as CONFIG
from . import menu_students as MENU_STUDENTS
from . import menu_subjects as MENU_SUBJECTS
from . import menu_ah as MENU_ACADEMIC_HISTORY


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
        if option == '1':  # starts another infinite iteration for each option; prints a submenu that allows the calling of the methods of the tables
            MENU_SUBJECTS.mainMenuSubjects(connection)
        elif option == '2':
            MENU_STUDENTS.mainMenuStudents(connection)
        elif option == '3':
            MENU_ACADEMIC_HISTORY.mainMenuAH(connection)
        elif option == '4':
            pass
        elif option == '5':  # exits the main menu if the input is 5
            print("\033[0;31mDone!\033[0;m")
            exitMenu = True
        else:  # prints out an error message. The main menu iteration continues
            error = "ERROR: Invalid option"
