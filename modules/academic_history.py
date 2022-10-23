def createAcademicHistoryTable(connection):
    cursorObj = connection.cursor()#Recorremos la base de datos con el objeto cursorObj
    cursorObj.execute('''CREATE TABLE academicHistory(
                                    subjectCode integer PRIMARY KEY,
                                    identificationNumber integer,
                                    finalNote float,
                                    subjectCredits integer )''')#Creamos la tabla academicHistory
    connection.commit()#Aseguramos la persistencia guardando la tabla en el disco

def addSubject(connection):#La función addSubjec añade materias a la tabla academicHistory   

    print ('\n\nWelcome! Enter the information to add a new subject\n')#Solicitamos la información de la materia que se va a insertar a la historia acádemica
    subjectCode = input('Enter the subject code: ') 
    identificationNumber = input('Enter the identification number: ')
    finalNote = input('Enter the final note: ')
    subjectCredits = input('Enter the subject credits: ')

    cursorObj = connection.cursor()#Recorremos la base de datos con el objeto cursorObj
    infoSubject = 'INSERT INTO academicHistory VALUES('+subjectCode+','+identificationNumber+', '+finalNote+', '+subjectCredits+')'
    #Asignamos a la variable infoSubject la función INSERT, y relacionamos la información solicitada con el campo correspondiente de la tabla academicHistory
    cursorObj.execute(infoSubject)#Insertamos la información en la tabla academicHistory
    connection.commit()#Aseguramos la persistencia guardando la tabla en el disco
    print ('\nSubject was successfully added!')
    
def readAcademicHistory(connection):#La función readAcademicHistory hace la consulta de informacion a la tabla academicHistory 
    
    print ('\n\nWelcome! Enter the information to see your academic history\n')#Solicitamos la información del usuario para realizar la consulta correcta
    identification = input('Enter the identification number: ')
    readHistory = "SELECT * FROM academicHistory WHERE identificationNumber = "+identification+""
    #Asignamos a la variable readHistory la función SELECT, y relacionamos la información solicitada con el campo correspondiente de la tabla
    cursorObj = connection.cursor()#Recorremos la base de datos con el objeto cursorObj
   
    def useSelect(numberHistory):#La función useSelect ejecuta el SELECT
        cursorObj.execute(numberHistory)#Consultamos la informacion en la tabla academicHistory
        rows = cursorObj.fetchall()#Lee los registros en memoria y devuelve una lista
        return rows 

    rows = useSelect(readHistory)#Llamamos a la función que ejecuta el SELECT
    
    for r in rows:#El ciclo for recorre la base de datos y nos devuelve la información solicitada a traves de los correspondientes indices
        subjectCode = r[0]
        finalNote = r[2]
        subjectCredits = r[3]
        print ('\nAcademic History: ')
        print ('\nSubject Code: ', subjectCode)
        print ('Final Note: ', finalNote)
        print ('Subject Credits: ', subjectCredits)

    if rows == []:#El condicional if verifica que la lista esté vacia, e imprime mensaje de incidencia por el documento ingresado
        print ('\nThis document does not have an academic history assigned!')

def deleteSubject(connection):#La función deleteSubject elimina una materia en la tabla academicHistory

    print ('\n\nwelcome! Enter the information to remove a subject\n')#Solicitamos la información del usuario para realizar la eliminación correcta
    code = input('Enter the subject code: ')
    identification = input('Enter the identification number: ')
    deleteHistory = "DELETE FROM academicHistory Where identificationNumber == "+identification+" AND subjectCode == "+code+""
    #Asignamos a la variable deleteHistory la función DELETE, y relacionamos la información solicitada con el campo correspondiente de la tabla
    readHistory = "SELECT * FROM academicHistory WHERE identificationNumber == "+identification+" AND subjectCode == "+code+""
    #Asignamos a la variable readHistory la función SELECT, y relacionamos la información solicitada con el campo correspondiente de la tabla
    cursorObj = connection.cursor()#Recorremos la base de datos con el objeto cursorObj

    def modificateHistory(numberHistory):#La función modificateHistory ejecuta el DELETE
        cursorObj.execute(numberHistory)#Eliminamos la información en la tabla academicHistory
        connection.commit()#Aseguramos la persistencia guardando la tabla en el disco

    def checkDelete(numberHistory):#La función checkDelete ejecuta el SELECT
        cursorObj.execute(numberHistory)#Consultamos la información en la tabla academicHistory
        rows = cursorObj.fetchall()#Lee los registros en memoria y devuelve una lista
        return rows

    rows = checkDelete(readHistory)#Llamamos a la función que ejecuta el DELETE
    
    for r in rows:#El ciclo for recorre la base de datos y nos devuelve la información de la materia eliminada
        subjectCode = r[0]
        finalNote = r[2]
        subjectCredits = r[3]
        print ('\nSubject Code: ', subjectCode)
        print ('Final Note: ', finalNote)
        print ('Subject Credits: ', subjectCredits)
        
    if rows == []:#El condicional if verifica que la lista esté vacia, e imprime mensaje de incidencia con el documento ingresado
        print ('\nThe data entered is incorrect, please check and try again!')
    else:
        print ('\n<- This subject was successfully deleted!')
        
    modificateHistory(deleteHistory)#Llamamos a la función que ejecuta el SELECT

def updateFinalNote(connection):#La función updateFinalNote actualiza la nota final de una materia en la tabla academicHistory

    print ('\n\nWelcome! Enter the information to update the final note\n')#Solicitamos la información del usuario para realizar la actualización correcta
    code = input('Enter the subject code: ')
    identification = input('Enter the identification number: ')
    readHistory = "SELECT * FROM academicHistory WHERE identificationNumber == "+identification+" AND subjectCode == "+code+""
    #Asignamos a la variable readHistory la función SELECT, y relacionamos la información solicitada con el campo correspondiente de la tabla
    cursorObj = connection.cursor()#Recorremos la base de datos con el objeto cursorObj
        
    def readNew(numberHistory):#La función readNew ejecuta el Select
        cursorObj.execute(numberHistory)#Consultamos la información en la tabla academicHistory
        rows = cursorObj.fetchall()#Lee los registros en memoria y devuelve una lista
        return rows

    rows = readNew(readHistory)#Llamamos a la función que ejecuta el SELECT

    for r in rows:#El ciclo for recorre la base de datos y nos devuelve los elementos solicitados
            subjectCode = r[0]
            finalNote = r[2]
            subjectCredits = r[3]
            
    if rows == []:#El condicional if verifica que la lista esté vacia, e imprime mensaje de incidencia por el documento ingresado
        print ('\nThe data entered is incorrect, please check and try again!')
    
    else:
        
        newNote = input('Enter the new final note: ')#Solicitamos la nueva nota al usuario para realizar la actualización correcta
        updateHistory = "UPDATE academicHistory SET finalNote == "+newNote+" WHERE identificationNumber == "+identification+" AND subjectCode == "+code+""
        #Asignamos a la variable updateHistory la función UPDATE, y relacionamos la información solicitada con el campo correspondiente de la tabla
        cursorObj = connection.cursor()#Recorremos la base de datos con el objeto cursorObj

        def refreshNote(chooseHistory):#La función refreshNote ejecuta el UPDATE
            cursorObj.execute(chooseHistory)#Actualizamos la información en la table academicHistory
            connection.commit()#Aseguramos la persistencia guardando la tabla en el disco

        refreshNote(updateHistory)#Llamamos a la función que ejecuta el UPDATE
        rows = readNew(readHistory)#Llamamos a la función que ejecuta el SELECT con la nota ya actualizada
        
        for r in rows:#El ciclo for recorre la base de datos y nos devuelve la información de la materia con la nota actualizada
            subjectCode = r[0]
            finalNote = r[2]
            subjectCredits = r[3]
            print ('\nSubject Code: ', subjectCode)
            print ('New final Note: ', finalNote)
            print ('Subject Credits: ', subjectCredits)
            print ('\n<- This subject was successfully updated!')

def close_db(connection):#La funcion close_db cierra la base de datos academicHistory
    connection.close()

def eraseAcademicHistoryTable(connection):#La funcion eraseAcademicHistoryTable elimina la tabla academicHistory

    cursorObj = connection.cursor()#Recorremos la base de datos con el objeto cursorObj
    cursorObj.execute('DROP TABLE academicHistory')#Eliminamos la tabla academicHistory
    connection.commit()#Aseguramos la persistencia guardando el cambio en el disco

def menu():#La función menu utiliza las funciones del programa y crea una interfaz para navegar a través de este mismo

    my_connection = connectionToDB()#Variable my_connection asignada a la conexión con la base de datos
    leave = False
    while not leave:#Ciclo while not que se ejecuta con el Main Menu, hasta que leave = True
        mainMenu = input('''

                        Main Menu

                        0. createAcademicHistoryTable
                        1. addSubject
                        2. readAcademicHistory
                        3. deleteSubject
                        4. updateFinalNote
                        5. close_db
                        6. exit
                        7. eraseAcademicHistoryTable
                        
                        select an option >>>: ''')
        
        if mainMenu == '0':#condicional if con diferentes elif, que brindan al usuario las opciones para utilizar el programa
            createAcademicHistoryTable(my_connection)
            print('\n\nTable "academicHistory" created successfully')
        elif mainMenu == '1':
            addSubject (my_connection)
        elif mainMenu == '2':
            readAcademicHistory (my_connection)
        elif mainMenu == '3':
            deleteSubject(my_connection)
        elif mainMenu == '4':
            updateFinalNote(my_connection)
        elif mainMenu == '5':
            close_db(my_connection)
            print ('\n\nThe database "academicHistory" has been closed!')
        elif mainMenu == '6':
            leave = True
            print('\n\nProgram closed, see you soon!')
        elif mainMenu == '7':
            eraseAcademicHistoryTable(my_connection)
            print('\n\nThe database "academicHistory" has been dropped!')
        else:#sentencia else que imprime mesaje de incidencia al escribir una opción invalida
            print('\n\nIs not a valid option, please try again!')