import modules.students as students


def readDataUser():
    id = input("Enter the id of the student: ")
    id = id.ljust(12)  # Fix to the left 12 positions
    name = input("Enter the name of the student: ")
    last_name = input("Enter the last_name of the student: ")
    career = input("Enter the career of the student: ")
    born_date = input("Enter the born_date of the student: ")
    entry_date = input("Enter the entry_date of the student: ")
    place_origin = input("Enter the place_origin of the student: ")
    email = input("Enter the email of the student: ")
    enrol_quantity = input("Enter the enrol_quantity of the student: ")
    photograph = input("Enter the photograph of the student: ")
    student = (id, name, last_name, career, born_date, entry_date,
               place_origin, email, enrol_quantity, photograph)
    return student


def main():
    my_connection = students.connectionToDB()
    students.createTableStudent(my_connection)
    # readDataUser()


if __name__ == "__main__":
    main()
