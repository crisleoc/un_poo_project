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
    02. Reload main student data
    03. Reload student classification
    04. Reload credits amount
    05. Return
{br}
Choose an option >>>\t"""


# Returns the string containing the Academic History menu options
def menuAcademicHistory():
    return f"""
ACADEMIC HISTORY MENU
{br}
    01. Add subject qualification
    02. Search subject qualification
    03. Update subject qualification
    04. Delete update qualification
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


# creates the 'student' tuple, used in the insertStudent method.
def readDataUserStudent():
    try:
        id = int(input("Enter the id of the student: "))
    except:
        raise Exception("The id must be a number")
    name = input("Enter the name of the student: ")
    last_name = input("Enter the last_name of the student: ")
    career = input("Enter the career of the student: ")
    born_date = input("Enter the born_date of the student: ")
    entry_date = input("Enter the entry_date of the student: ")
    place_origin = input("Enter the place_origin of the student: ")
    email = input("Enter the email of the student: ")
    try:
        enroll_quantity = int(
            input("Enter the enroll_quantity of the student: "))
    except:
        raise Exception("The enroll_quantity must be a number")
    photograph = input("Enter the photograph of the student: ")
    student = (id, name, last_name, career, born_date, entry_date,
               place_origin, email, enroll_quantity, photograph)
    return student


# creates the 'subject' tuple, used in the insertSubject method.
def readDataUserSubject():
    try:
        code = int(input("Enter the code of the subject: "))
    except:
        raise Exception("The id must be a number: ")
    name = input("Enter name of the subject: ")
    school = input("Enter school of the subject: ")
    department = input("Enter the department of the subject: ")
    try:
        credits = int(input("Enter the number of credits of the subject: "))
    except:
        raise Exception("The credits must be a number: ")
    language = input("Enter the language of the subject: ")
    subject = (code, name, school, department, credits, language)
    return subject
