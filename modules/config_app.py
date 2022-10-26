import os


def clear():
    # Function that clear the console
    """_summary_: Clear the console
    """
    os.system('cls' if os.name == 'nt' else 'clear')


br = '='*60


def menuMain():
    return f"""
MAIN MENU
{br}
    01. Subjects
    02. Students
    03. Academic History
    04. Classification
    05. Exit
{br}
Choose an option >>>\t"""


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
    if studentData != []:
        for i in range(len(studentData[0])):
            title = str(titles[i])
            data = str(studentData[0][i])
            string = "|{:<23}||{:>33}|".format(title, data)
            print(string)
            print('-'*60)
    else:
        print("No data found")
    print(br + "\033[0m")


def printSelectSubject(subjectData):
    titles = ("Code", "Name", "School", "Department", "Credits", "Language")
    print("\033[0;33m" + br)
    if subjectData != []:
        for i in range(len(subjectData[0])):
            title = str(titles[i])
            data = str(subjectData[0][i])
            string = "|{:<23}||{:>33}|".format(title, data)
            print(string)
            print('-'*60)
    else:
        print("No data found")
    print(br + "\033[0m")


def printSelectAH(AHData):
    titles = ("Subject code", "Student id", "Final note", "Credits")
    print("\033[0;33m" + br)
    if AHData != [] and type(AHData) != str:
        for i in AHData:
            for j in range(len(i)):
                title = str(titles[j])
                data = str(i[j])
                string = "|{:<23}||{:>33}|".format(title, data)
                print(string)
                print('-'*60)
            print(br)
    elif AHData == []:
        print("No data found")
    else:
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
