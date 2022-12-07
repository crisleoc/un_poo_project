import modules.connect_db as CONNECT_DB
import modules.main_menu as MAIN_MENU


def main():
    CONNECT_DB.createTables()
    my_connection = CONNECT_DB.connectionToDB()
    MAIN_MENU.mainMenu(my_connection)
    my_connection.close()


if __name__ == "__main__":
    main()
