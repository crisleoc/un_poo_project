def createClassificationTable(connection):
    # recorremos la base de datos con el objeto de conexión
    cursorObj = connection.cursor()
    STUDENT_ID = "student_id INTEGER"
    NAME = "name TEXT"
    LAST_NAME = "lastName TEXT"
    AMOUNT_SUBJECTS = "amountSubjects INTEGER"
    CREDIT_SUM = "creditSum INTEGER"
    AVERAGE = "average INTEGER"
    CREATE_STATEMENT = f"CREATE TABLE IF NOT EXISTS classification({STUDENT_ID},{NAME},{LAST_NAME},{AMOUNT_SUBJECTS},{CREDIT_SUM},{AVERAGE})"
    cursorObj.execute(CREATE_STATEMENT)  # creamos la tabla materias
    connection.commit()  # aseguramos la persistencia guardando la tabla en el disco


# tomamos la información relevante de la tabla students y la pasamos a la tabla clasificación
def getStudentInfo(connection):
    """Get the student information from the students table and insert it into the classification table.

    Args:
        connection (Object): Connection to sqlite3.
    """
    cursorObj = connection.cursor()
    joinStatement = "INSERT INTO classification (student_id, name, lastname) SELECT id, name, lastname FROM students WHERE id NOT IN (SELECT student_id FROM classification)"
    cursorObj.execute(joinStatement)
    connection.commit()


# permite seleccionar la clasificación de un estudiante mediante su ID
def selectClassificationByID(connection, student_id):
    """Select a classification by the student id in the database:

    Args:
        connection (object): Connection to sqlite3.
        student_id (int): Id of the student.
    Returns:
        list<tuple>: List of tuples with the data of the students that contains the id.
    """
    CURSOR_OBJ = connection.cursor()
    SELECT_STATEMENT = "SELECT * FROM Classification WHERE student_id = ?"
    CURSOR_OBJ.execute(SELECT_STATEMENT, (student_id,))
    return CURSOR_OBJ.fetchall()


# recorre la tabla de academicHistory y cuenta cuantas materias concuerdan con cada ID del estudiante
def UpdateClassification(connection):
    """Update the classification table with the amount of subjects and the sum of credits of the students.

    Args:
        connection (object): Connection to sqlite3.
    """
    cursorObj = connection.cursor()
    SELECT_QUERY_ACAD = "SELECT id FROM academicHistory WHERE id>-1 ORDER BY id ASC"
    SELECT_QUERY_CLAS = "SELECT student_id FROM classification WHERE student_id>-1 ORDER BY student_id ASC"
    SELECT_QUERY_CREDITS = "SELECT credits FROM academicHistory WHERE id>-1 ORDER BY id ASC"
    SELECT_QUERY_SCORE = "SELECT finalNote FROM academicHistory WHERE id >-1 ORDER BY id ASC"
    cursorObj.execute(SELECT_QUERY_CLAS)
    # toma las IDs de classification y las convierte en una tupla
    CLAStuple = cursorObj.fetchall()
    cursorObj.execute(SELECT_QUERY_ACAD)
    # toma las IDs de academicHistory y las convierte en una tupla
    ACADtuple = cursorObj.fetchall()
    cursorObj.execute(SELECT_QUERY_CREDITS)
    CREDITStuple = cursorObj.fetchall()
    cursorObj.execute(SELECT_QUERY_SCORE)
    SCOREtuple = cursorObj.fetchall()
    for i in range(len(CLAStuple)):
        creditos = 0
        materias = 0
        promedio = 0
        for j in range(len(ACADtuple)):
            if(CLAStuple[i] == ACADtuple[j]):
                creditos = creditos+CREDITStuple[j][0]
                materias += 1
                promedio = promedio+(SCOREtuple[j][0]*CREDITStuple[j][0])
        if(creditos != 0):
            promedio = round((promedio/creditos), 1)
        UPDATE_STATEMENT = "UPDATE classification SET creditSum == " + \
            str(creditos)+" WHERE student_id == "+str(CLAStuple[i][0])+""
        cursorObj.execute(UPDATE_STATEMENT)
        UPDATE_STATEMENT2 = "UPDATE classification SET amountSubjects == " + \
            str(materias)+" WHERE student_id == "+str(CLAStuple[i][0])+""
        cursorObj.execute(UPDATE_STATEMENT2)
        UPDATE_STATEMENT3 = "UPDATE classification SET average == " + \
            str(promedio)+" WHERE student_id == "+str(CLAStuple[i][0])+""
        cursorObj.execute(UPDATE_STATEMENT3)
        connection.commit()
    connection.commit()


# recorre la tabla de academicHistory y cuenta cuantas materias concuerdan con cada ID del estudiante
def GetCreditsAmount(connection):
    """Get the amount of credits of the students."""
    cursorObj = connection.cursor()
    SELECT_QUERY_ACAD = "SELECT id FROM academicHistory WHERE id>-1 ORDER BY id ASC"
    SELECT_QUERY_CLAS = "SELECT student_id FROM classification WHERE student_id>-1 ORDER BY student_id ASC"
    SELECT_QUERY_CREDITS = "SELECT credits FROM academicHistory WHERE id>-1 ORDER BY id ASC"
    SELECT_QUERY_SCORE = "SELECT finalNote FROM academicHistory WHERE id >-1 ORDER BY id ASC"
    cursorObj.execute(SELECT_QUERY_CLAS)
    # toma las IDs de classification y las convierte en una tupla
    CLAStuple = cursorObj.fetchall()
    cursorObj.execute(SELECT_QUERY_ACAD)
    # toma las IDs de academicHistory y las convierte en una tupla
    ACADtuple = cursorObj.fetchall()
    cursorObj.execute(SELECT_QUERY_CREDITS)
    CREDITStuple = cursorObj.fetchall()
    cursorObj.execute(SELECT_QUERY_SCORE)
    SCOREtuple = cursorObj.fetchall()
    for i in range(len(CLAStuple)):
        creditos = 0
        materias = 0
        promedio = 0
        for j in range(len(ACADtuple)):
            if(CLAStuple[i] == ACADtuple[j]):
                creditos = creditos+CREDITStuple[j][0]
                materias += 1
                promedio = promedio+(SCOREtuple[j][0]*CREDITStuple[j][0])
        if(creditos != 0):
            promedio = round((promedio/creditos), 1)
        UPDATE_STATEMENT = "UPDATE classification SET creditSum == " + \
            str(creditos)+" WHERE student_id == "+str(CLAStuple[i][0])+""
        cursorObj.execute(UPDATE_STATEMENT)
        UPDATE_STATEMENT2 = "UPDATE classification SET amountSubjects == " + \
            str(materias)+" WHERE student_id == "+str(CLAStuple[i][0])+""
        cursorObj.execute(UPDATE_STATEMENT2)
        UPDATE_STATEMENT3 = "UPDATE classification SET average == " + \
            str(promedio)+" WHERE student_id == "+str(CLAStuple[i][0])+""
        cursorObj.execute(UPDATE_STATEMENT3)
        connection.commit()
    connection.commit()
