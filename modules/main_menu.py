import modules.connect_db as CONNECT_DB
import modules.students as STUDENTS
import modules.subjects as SUBJECTS
import modules.classification as CLASSIFY
import modules.academic_history as ACADEMIC_HISTORY


def readDataUserStudent(): #creates the 'student' tuple, used in the insertStudent method.
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


def readDataUserSubject(): #creates the 'subject' tuple, used in the insertSubject method.
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
    while not exitMenu: #an infinite while not iteration. Prints out the main menu options, every option is a table that the user can modify.
        option = input('''

                        Main Menu

                        1. Subjects
                        2. Students
                        3. Academic History
                        4. Classification
            
                        0. Exit Menu
                        
                        Select an option >>>: ''')
        
        if option == '1': #starts another infinite iteration for each option; prints a submenu that allows the calling of the methods of the tables
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
                elif option == '0': exitSubjects == True # exits the subjects table submenu if the input is 0
                else: print('ERROR: Invalid input, try again') # exception handling, asks again for a valid option                  
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
                    CLASSIFY.getstudentinfo(connection)        
                elif option == '2': 
                    #********************
                    studentID=int(input('''
                    
                    Insert the ID of the student you want to update: '''
                    
                    ))
                    STUDENTS.updateStudent(connection,studentID)
                    #********************
                elif option == '3':
                    #********************
                    studentID=int(input('''
                    
                    Insert the ID of the student you want to query: '''
                    
                    ))
                    print(STUDENTS.selectStudentByID(connection,studentID))
                    #********************
                elif option == '0': exitStudents == True # exits the students table submenu if the input is 0
                else: print('ERROR: Invalid input, try again') # prints out an error message. The submenu iteration continues        
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
                    CLASSIFY.UpdateClassification(connection)      
                elif option == '2': 
                    #******************
                    ACADEMIC_HISTORY.updateFinalNote
                    CLASSIFY.UpdateClassification(connection)
                    #******************
                elif option == '3':
                    #CAMBIAR NOMBRE DE METODO A QueryAcademicHistory
                    ACADEMIC_HISTORY.readAcademicHistory
                    #********************
                elif option == '4':
                    ACADEMIC_HISTORY.deleteSubject(connection)
                elif option == '0': exitAH == True # exits the academic history table submenu if the input is 0
                else: print('ERROR: Invalid input, try again') # prints out an error message. The submenu iteration continues
        elif option == '4':
            exitClas = False
            while not exitClas:
                option = input('''

                        Classification Menu

                        1. See Classification
            
                        0. Exit Menu
                        
                        Select an option >>>: ''')
                if option == '1': 
                    student_id=int(input('''
                        
                        Insert the ID of the student you want to see the clasification of:
                        
                         '''))
                    #**************
                    print(CLASSIFY.selectClassificationByID(connection,student_id))   
                    #**************  
                elif option == '0': exitClas == True # exits the classification table submenu if the input is 0
                else: print('ERROR: Invalid input, try again')
        elif option == 0 : # exits the main menu if the input is 0
            print('Exiting Menu...')
            exitMenu = True
        else:# prints out an error message. The main menu iteration continues
            print('Is not a valid option, please try again!')
    
    
def main():
    my_connection = CONNECT_DB.connectionToDB()
    mainMenu(my_connection)