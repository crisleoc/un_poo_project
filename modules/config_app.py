from datetime import datetime
import os


def clear():
    # Function that clear the console
    """Clear the console"""
    os.system('cls' if os.name == 'nt' else 'clear')


# User Interface variable that multiplies the character 60 times and assigns the new string to the br variable
br = '='*60


# Returns the string containing the main menu options
def menuMain():
    return f"""
MAIN MENU | SIA SIMULATOR 2022
{br}
    00. Fill database with test data
    01. Subjects
    02. Students
    03. Academic History
    04. Classification
    05. Exit
{br}
Choose an option >>>\t"""


# Returns the string containing the Students menu options
def menuStudents():
    return f"""
STUDENTS MENU
{br}
    01. Create student
    02. Search student
    03. Update student
    04. Delete student
    05. Return
{br}
Choose an option >>>\t"""


def menuClassify():
    return f"""
CLASSIFICATION MENU
{br}
    01. Query student classification
    02. Return
{br}
Choose an option >>>\t"""


# Returns the string containing the Academic History menu options
def menuAcademicHistory():
    return f"""
ACADEMIC HISTORY MENU
{br}
    01. Create new academic history
    02. Search academic history
    03. Update subject qualification
    04. Delete subject
    05. Return
{br}
Choose an option >>>\t"""


# Returns the string containing the Subjects menu options
def menuSubjects():
    return f"""
SUBJECTS MENU
{br}
    01. Create subject
    02. Search subject
    03. Update subject
    04. Delete subject
    05. Return
{br}
Choose an option >>>\t"""


def menuUpdateStudent(studentID):
    return f"""
UPDATE STUDENT \033[0;33m({studentID})\033[0;m
{br}
    01. Modify id
    02. Modify name
    03. Modify lastName
    04. Modify career
    05. Modify bornDate
    06. Modify entryDate
    07. Modify placeOrigin
    08. Modify email
    09. Modify enrollQuantity
    10. Modify photograph
    11. Modify all
    12. Cancel
{br}
Choose an option >>>\t"""


def menuUpdateSubject(subjectCode):
    return f"""
UPDATE SUBJECT \033[0;33m({subjectCode})\033[0;m
{br}
    01. Modify code
    02. Modify name
    03. Modify school
    04. Modify department
    05. Modify credits
    06. Modify language
    07. Modify all
    08. Cancel
{br}
Choose an option >>>\t"""


# Function that receive a long text and print ir with a line break every 50 characters
def printErrorApp(text):
    # "\033[0;31m" allows the string to be printed with red characters
    print("\033[0;31m" + br)
    for i in range(0, len(text), 60):
        print(text[i:i+60])
    print(br + "\033[0m")


def printSuccessApp(text):
    print("\033[0;32m" + br)
    for i in range(0, len(text), 60):
        print(text[i:i+60])
    print(br + "\033[0m")


def printMessageApp(text):
    print("\033[0;33m" + br)
    for i in range(0, len(text), 60):
        print(text[i:i+60])
    print(br + "\033[0m")


def printSelectStudent(studentData):
    titles = ("Id", "Name", "Last Name", "Career", "Born Date", "Entry Date",
              "Place Origin", "Email", "Enroll Quantity", "Photograph")
    print("\033[0;33m" + br)
    # if the studentData isn´t empty, prints all its elements
    if studentData != []:
        for i in range(len(studentData[0])):
            title = str(titles[i])
            data = str(studentData[0][i])
            # Limits the space used by each element in every row of the table
            string = "|{:<23}||{:>33}|".format(title, data)
            print(string)
            print('-'*60)
    else:
        print("No data found")
    print(br + "\033[0m")


def printSelectClassify(classifyData):
    titles = ("Id", "Name", "Last Name", "Amount of subjects",
              "Accumulated credits", "Average")
    print("\033[0;33m" + br)
    if classifyData != []:
        for i in range(len(classifyData[0])):
            title = str(titles[i])
            data = str(classifyData[0][i])
            string = "|{:<23}||{:>33}|".format(title, data)
            print(string)
            print('-'*60)
    else:
        print("No data found, please reload the data.")
    print(br + "\033[0m")
    while True:
        sendEmail = input(
            "Do you want to send an email to the student with the info? (y/n) ")
        if sendEmail == "y":
            return [True, classifyData]
        elif sendEmail == "n":
            return [False, classifyData]


def bodyMail(classifyData):
    titles = ("Id", "Name", "Last Name", "Amount of subjects",
              "Accumulated credits", "Average")
    message = ""
    message += f"{br}\n"
    if classifyData != []:
        for i in range(len(classifyData[0])):
            title = str(titles[i])
            data = str(classifyData[0][i])
            string = "|{:<23}||{:>33}|".format(title, data)
            message += f"{string}\n"
            message += '-'*60 + "\n"
    message += f"{br}\n"
    return message


def printSelectSubject(subjectData):
    titles = ("Code", "Name", "School", "Department", "Credits", "Language")
    print("\033[0;33m" + br)  # prints the br variable in red characters
    if subjectData != []:
        for i in range(len(subjectData[0])):
            title = str(titles[i])
            data = str(subjectData[0][i])
            string = "|{:<23}||{:>33}|".format(title, data)
            print(string)
            print('-'*60)
    else:
        print("No data found")
    print(br + "\033[0m")  # prints the br variable in red characters


def printSelectAH(AHData):
    # Prints all the information of a row in the Academic History if it exists
    titles = ("Subject code", "Student id", "Final note", "Credits")
    if AHData != [] and type(AHData) != str:
        print(f"\033[0;35m({AHData[0][1]})\033[0;33m")
        print(br)
        for i in AHData:
            for j in range(len(i)):
                if j != 1:
                    title = str(titles[j])
                    data = str(i[j])
                    string = "|{:<23}||{:>33}|".format(title, data)
                    print(string)
                    print('-'*60)
                else:
                    continue
            print(br)
    elif AHData == []:
        print("\033[0;33m" + br)
        print("No data found")
    else:
        print("\033[0;33m" + br)
        print(AHData)
    print(br + "\033[0m")


def get_data(text, dataType):
    """This function receives a text and a data type and returns the data

    Args:
        text (str): Text to be printed
        dataType (str): Data type to be validated (int, float, str, date)

    Returns:
        data : Data validated
    """
    if dataType == "int":
        while True:
            try:
                data = int(input(text))
                return data
            except ValueError:
                printErrorApp("Please enter a valid integer")
    elif dataType == "float":
        while True:
            try:
                data = float(input(text))
                return data
            except ValueError:
                printErrorApp("Please enter a valid float")
    elif dataType == "str":
        while True:
            try:
                data = str(input(text))
                return data
            except ValueError:
                printErrorApp("Please enter a valid string")
    elif dataType == "date":
        while True:
            try:
                data = str(input(text))
                date = datetime.strptime(data, "%d-%m-%Y")
                return date
            except ValueError:
                printErrorApp("Please enter a valid date (dd-mm-yyyy)")


# creates the 'student' tuple, used in the insertStudent method.
def readDataUserStudent():
    id = get_data("Enter the student id: ", "int")
    name = get_data("Enter the student name: ", "str")
    last_name = get_data("Enter the student last name: ", "str")
    career = get_data("Enter the student career: ", "str")
    born_date = get_data("Enter the student born date (dd-mm-yyyy): ", "date")
    entry_date = get_data(
        "Enter the student entry date (dd-mm-yyyy): ", "date")
    place_origin = get_data("Enter the student place origin: ", "str")
    email = get_data("Enter the student email: ", "str")
    enroll_quantity = get_data("Enter the student enroll quantity: ", "int")
    photograph = get_data("Enter the student photograph link: ", "str")
    student = (id, name, last_name, career, born_date, entry_date,
               place_origin, email, enroll_quantity, photograph)
    return student


# creates the 'subject' tuple, used in the insertSubject method.
def readDataUserSubject():
    code = get_data("Enter the subject code: ", "int")
    name = get_data("Enter the subject name: ", "str")
    school = get_data("Enter the subject school: ", "str")
    department = get_data("Enter the subject department: ", "str")
    credits = get_data("Enter the subject credits: ", "int")
    language = get_data("Enter the subject language: ", "str")
    subject = (code, name, school, department, credits, language)
    return subject
