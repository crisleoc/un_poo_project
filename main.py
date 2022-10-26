from unicodedata import name
import modules.connect_db as CONNECT_DB
import modules.students as STUDENTS
import modules.subjects as SUBJECTS
import modules.classification as CLASSIFY
import modules.academic_history as ACADEMIC_HISTORY
import modules.menu_students as MENU_STUDENTS
import modules.menu_subjects as MENU_SUBJECTS
import modules.main_menu as MAIN_MENU


def main():

    my_connection = CONNECT_DB.connectionToDB()
    MAIN_MENU.mainMenu(my_connection)
    my_connection.close()


if __name__ == "__main__":
    main()
