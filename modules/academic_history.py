def createAcademicHistoryTable(con):
    cursorObj = con.cursor()  # Recorremos la base de datos con el objeto cursor
    # Creamos la tabla academicHistory
    cursorObj.execute(
        'CREATE TABLE academicHistory(subjectCode integer, identificationNumber integer, finalNote float, subjectCredits integer )')
    con.commit()  # Aseguramos la persistencia guardando la tabla en el disco


def addSubject(con):

    print('\nWelcome! Fill in the blanks to add a new Subject\n')
    # Pedimos la información de la materia que se va a insertar a la historia acádemica
    subjectCode = input('Enter the subject code: ')
    identificationNumber = input('Enter the identification number: ')
    finalNote = input('Enter the final note: ')
    subjectCredits = input('Enter the subject credits: ')

    cursorObj = con.cursor()  # Recorremos la base de datos con el objeto cursor
    infoSubject = 'INSERT INTO academicHistory VALUES('+subjectCode + \
        ','+identificationNumber+', '+finalNote+', '+subjectCredits+')'
    # Creamos una variable, dentro de la cual está la función INSERT, con la cual agregamos la informacion solicitada a cada campo de la tabla en la base de datos
    print('\nAdded Subject: \n', '\nSubject Code: ', subjectCode, '\nIdentification Number: ',
          identificationNumber, '\nFinal Note: ', finalNote, '\nCredits Completed: ', subjectCredits)
    # Mostramos la informacón en consola de la matria que ha sido agregada a la base de datos
    cursorObj.execute(infoSubject)  # Ejecutamos la función INSERT
    con.commit()  # Aseguramos la persistencia guardando la tabla en el disco


def readAcademicHistory(con):

    print('\nWelcome! Fill in the blanks to see your academic history\n')
    # Pedimos el documento de identidad para el cual realizaremos la consulta de la historia académica
    identification = input('Enter the identification number: ')
    print('\nAcademic History: \n')
    readHistory = "SELECT * FROM academicHistory WHERE identificationNumber = "+identification+""
    # Creamos una variable, dentro de la cual está la función SELECT, con la cual mostraremos la información relacionada al documento de identidad, si este ya se encuentra en la base de datos
    cursorObj = con.cursor()  # Recorremos la base de datos con el objeto cursor

    def useSelect(numberHistory):  # Creamos la función useSelect para usarla como ejecutor de los SELECT, que se pudieran necesitar en la funcion principal readAcademicHistory
        cursorObj.execute(numberHistory)  # Ejecutamos la función SELECT
        rows = cursorObj.fetchall()  # lee los registros en memoria y devuelve una lista
        return rows

    rows = useSelect(readHistory)  # llamamos a la función que ejecuta SELECT
    for r in rows:  # Creamos un ciclo for que recorre la base de datos y nos devuelve los datos solicitados
        subjectCode = r[0]
        finalNote = r[2]
        subjectCredits = r[3]
        print('Subject Code: ', subjectCode)
        print('Final Note: ', finalNote)
        print('Subject Credits: ', subjectCredits)
        print('\n')

    if rows == []:  # Verificamos si rows es una lista vacia, de ser así, el usuario no tiene una historia academica asignada a su numero de identidad
        print('This document does not have an academic history assigned')
