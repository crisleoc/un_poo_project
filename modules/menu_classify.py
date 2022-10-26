from . import config_app as CONFIG
from . import classification as CLASSIFY
from . import mails as EMAIL


def mainMenuClassify(connection):
    """Function to show the main menu of classification:

    Args:
        connection (object): Connection to sqlite3.
    """
    exitMenuClassify = False
    error = None
    success = None
    select = None
    sendEmail = None
    while not exitMenuClassify:
        CONFIG.clear()
        if error:
            CONFIG.printErrorApp(error)
        error = None
        if success:
            CONFIG.printSuccessApp(success)
        success = None
        if select != None:
            sendEmail = CONFIG.printSelectClassify(select)
        select = None
        if sendEmail != None:
            if sendEmail[0]:
                msg = None
                try:
                    email = EMAIL.get_email(connection, sendEmail[1][0][0])
                    msg = EMAIL.sendEmail(email, CONFIG.bodyMail(sendEmail[1]))
                    CONFIG.printSuccessApp(str(msg))
                except Exception as e:
                    msg = e
                    CONFIG.printErrorApp(f"ERROR: {msg}")
        sendEmail = None
        CLASSIFY_MENU = CONFIG.menuClassify()
        option = input(CLASSIFY_MENU)
        if option == '1':
            try:
                studentID = int(input("Enter the student id: "))
                select = CLASSIFY.selectClassificationByID(
                    connection, studentID)
                success = "01. SUCCESS: Execution finished without errors."
            except Exception as e:
                error = "01. ERROR: " + str(e)
        elif option == '2':
            try:
                CLASSIFY.getStudentInfo(connection)
                success = "02. SUCCESS: Data reload successfully"
            except Exception as e:
                error = "02. ERROR: " + str(e)
        elif option == '3':
            try:
                CLASSIFY.UpdateClassification(connection)
                success = "03. SUCCESS: Classification reloaded successfully"
            except Exception as e:
                error = "03. ERROR: " + str(e)
        elif option == '4':
            try:
                CLASSIFY.GetCreditsAmount(connection)
                success = "04. SUCCESS: Credits amount reloaded successfully"
            except Exception as e:
                error = "04. ERROR: " + str(e)
        elif option == '5':
            print("\033[0;31mOperation canceled!\033[0;m")
            exitMenuClassify = True
        else:
            error = "ERROR: Invalid option"
