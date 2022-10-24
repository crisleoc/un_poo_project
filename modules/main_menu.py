import modules.connect_db as CONNECT_DB
import modules.students as STUDENTS
import modules.subjects as SUBJECTS
import modules.classification as CLASSIFY
import modules.academic_history as ACADEMIC_HISTORY


def readDataUserStudent():
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


def readDataUserSubject():
    code = input("Enter code of the subject: ")
    code = code.ljust(12)
    name = input("Enter name of the subject")
    school = input("Enter school of the subject")
    department = input("Enter the department of the subject")
    credits = input("Enter the number of credits of the subject")
    language = input("Enter the language of the subject")
    subject = (code, name, school, department, credits, language)
    return subject


def mainMenu(connection):
    
    exitMenu = False
    while not exitMenu:#Ciclo while not que se ejecuta con el Main Menu, hasta que leave = True
        option = input('''

                        Main Menu

                        1. Subjects
                        2. Students
                        3. Academic History
                        4. Classification
            
                        0. Exit Menu
                        
                        Select an option >>>: ''')
        
        if option == '1':#condicional if con diferentes elif, que brindan al usuario las opciones para utilizar el programa
            exitSubjects = False
            while not exitSubjects:
                option = input('''

                        Subjects Menu

                        1. Insert new subject
                        2. Update a subject's data
                        3. Query a subject's data
            
                        0. Exit Menu
                        
                        Select an option >>>: ''')
                if option == '1': 
                    SUBJECTS.insertSubject(connection, readDataUserSubject())        
                elif option == '2': 
                    codeSubUp = int(input("Enter the code of the subject you want to query: "))
                    SUBJECTS.updateSubjects(connection, codeSubUp)
                elif option == '3':
                    codeSubQuery = int(input("Enter the code of the subject you want to query: "))
                    SUBJECTS.querySubjects(connection, codeSubQuery)
                elif option == '0': exitSubjects == True
                else: print('ERROR: Invalid input, try again')                    
        elif option == '2':
            exitStudents = False
            while not exitStudents:
                option = input('''

                        Students Menu

                        1. Insert new student
                        2. Update a student's data
                        3. Query a student's data
            
                        0. Exit Menu
                        
                        Select an option >>>: ''')
                if option == '1': 
                    STUDENTS.insertStudent(connection, readDataUserStudent())        
                elif option == '2': 
                    #********************
                    STUDENTS.update()
                    #********************
                elif option == '3':
                    #********************
                    STUDENTS.query()
                    #********************
                elif option == '0': exitStudents == True
                else: print('ERROR: Invalid input, try again')         
        elif option == '3':
            exitAH = False #Exit Academic History
            while not exitAH:
                option = input('''

                        Academic History Menu

                        1. Insert new Academic History
                        2. Update Final Note
                        3. Query an Academic History's data
                        4. Erase an Academic History
            
                        0. Exit Menu
                        
                        Select an option >>>: ''')
                if option == '1': 
                    ACADEMIC_HISTORY.addSubject(connection)        
                elif option == '2': 
                    #******************
                    ACADEMIC_HISTORY.updateFinalNote
                    #******************
                elif option == '3':
                    #CAMBIAR NOMBRE DE METODO A QueryAcademicHistory
                    ACADEMIC_HISTORY.readAcademicHistory
                    #********************
                elif option == '4':
                    ACADEMIC_HISTORY.deleteSubject(connection)
                elif option == '0': exitAH == True
                else: print('ERROR: Invalid input, try again')
        elif option == '4':
            exitClas = False
            while not exitClas:
                option = input('''

                        Classification Menu

                        1. See Classification
            
                        0. Exit Menu
                        
                        Select an option >>>: ''')
                if option == '1': 
                    #**************
                    CLASSIFICATION.queryClassification()   
                    #**************  
                elif option == '0': exitClas == True
                else: print('ERROR: Invalid input, try again')
        elif option == 0 : 
            print('Exiting Menu...')
            exitMenu = True
        else:#sentencia else que imprime mesaje de incidencia al escribir una opción invalida
            print('Is not a valid option, please try again!')
    
    
def main():
    my_connection = CONNECT_DB.connectionToDB()
    mainMenu(my_connection)