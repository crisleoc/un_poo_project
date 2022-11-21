from . import config_app as CONFIG
from .classes import classification as CLASSIFY
from . import mails as EMAIL


def mainMenuClassify(connection):
    """Function to show the main menu of classification:

    Args:
        connection (object): Connection to sqlite3.
    """
    # Create the object classification
    objectClassify = CLASSIFY.classification()

    exitMenuClassify = False
    error = None
    success = None
    select = None
    sendEmail = None
    while not exitMenuClassify:
        try:
            objectClassify.getStudentInfo(connection)
            objectClassify.UpdateClassification(connection)
            objectClassify.GetCreditsAmount(connection)
            success = "SUCCESS: Classification module reloaded successfully."
        except Exception as e:
            error = "ERROR: " + str(e)

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
                select = objectClassify.selectClassificationByID(
                    connection, studentID)
                success = "01. SUCCESS: Execution finished without errors."
            except Exception as e:
                error = "01. ERROR: " + str(e)
        elif option == '2':
            print("\033[0;31mOperation canceled!\033[0;m")
            exitMenuClassify = True
        else:
            error = "ERROR: Invalid option"
