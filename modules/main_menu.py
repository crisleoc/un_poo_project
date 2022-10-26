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
        MAIN_MENU = CONFIG.menuMain()
        option = input(MAIN_MENU)
        if option == '1':  # starts another infinite iteration for each option; prints a submenu that allows the calling of the methods of the tables
            MENU_SUBJECTS.mainMenuSubjects(connection)
        elif option == '2':
            MENU_STUDENTS.mainMenuStudents(connection)
        elif option == '3':
<<<<<<< HEAD
            MENU_ACADEMIC_HISTORY.mainMenuAH(connection)
=======
            exitAH = False #Exit Academic History
            while not exitAH:
                option = input('''

                        Academic History Menu

                        1. Insert new Academic History
                        2. Update Final Note
                        3. Query an Academic History's data
                        4. Erase an Academic History
            
                        0. Exit Menu
                        
                        Select an option >>>: ''')
                if option == '1': 
                    ACADEMIC_HISTORY.addSubject(connection)        
                elif option == '2': 
                    #******************
                    ACADEMIC_HISTORY.updateFinalNote(connection)
                    #******************
                elif option == '3':
                    #******************
                    ACADEMIC_HISTORY.queryAcademicHistory(connection)
                    #*******************
                elif option == '4':
                    ACADEMIC_HISTORY.deleteSubject(connection)
                elif option == '0': exitAH == True # exits the academic history table submenu if the input is 0
                else: print('ERROR: Invalid input, try again') # prints out an error message. The submenu iteration continues
>>>>>>> f1b151f3f99ff41cb6257eef06c08dd5757adc1c
        elif option == '4':
            exitClas = False
            while not exitClas:
                option = input('''

                        Classification Menu

                        1. See Classification
                        0. Exit Menu

                        Select an option >>>: ''')
<<<<<<< HEAD
                if option == '1':
                    # **************
                    CLASSIFY.queryClassification()
                    # **************
                elif option == '0':
                    exitClas == True  # exits the classification table submenu if the input is 0
                else:
                    print('ERROR: Invalid input, try again')
        elif option == '5':  # exits the main menu if the input is 0
            print("\033[0;31mDone!\033[0;m")
=======
                if option == '1': 
                    #**************
                    CLASSIFY.queryClassification()   
                    #**************  
                elif option == '0': exitClas == True # exits the classification table submenu if the input is 0
                else: print('ERROR: Invalid input, try again')
        elif option == 0 : # exits the main menu if the input is 0
            print('Exiting Menu...')
>>>>>>> f1b151f3f99ff41cb6257eef06c08dd5757adc1c
            exitMenu = True
        else:  # prints out an error message. The main menu iteration continues
            error = "ERROR: Invalid option"
