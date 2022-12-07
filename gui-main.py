import sys
from modules.views.app import *
import modules.connect_db as CONNECT_DB


def main():
    CONNECT_DB.createTables()
    my_connection = CONNECT_DB.connectionToDB()
    app = QApplication(sys.argv)
    MainWidget = AppMain(my_connection)
    MainWidget.show()
    sys.exit([app.exec_(), my_connection.close(), print("Connection closed")])


if __name__ == '__main__':
    main()
