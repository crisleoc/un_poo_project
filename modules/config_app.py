import os
from turtle import title


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


br = '='*60


def menuStudents():
    return f"""
{br}
    01. Create student
    02. Search student
    03. Update student
    04. Delete student
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


def printSelectApp(studentData):
    titles = ("Id", "Name", "Last Name", "Career", "Born Date", "Entry Date",
              "Place Origin", "Email", "Enroll Quantity", "Photograph")
    print("\033[0;33m" + br)
    for i in range(len(studentData[0])):
        title = str(titles[i])
        data = str(studentData[0][i])
        string = "|{:<23}||{:>33}|".format(title, data)
        print(string)
        print('-'*60)
    print(br + "\033[0m")


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


def input_option(menu):
    while True:
        clear()
        try:
            data = int(input(menu))
            return data
        except ValueError:
            print("ERROR: Use only numbers")
            continue
