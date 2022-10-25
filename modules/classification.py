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
def getstudentinfo(connection): #tomamos la información relevante de la tabla students y la pasamos a la tabla clasificación
    cursorObj = connection.cursor()
    joinStatement = "INSERT INTO classification (student_id,name,lastname) SELECT id,name,lastname FROM students WHERE id NOT IN(SELECT student_id FROM classification)"
    cursorObj.execute(joinStatement)
    connection.commit()
def selectClassificationByID(connection, student_id): #permite seleccionar la clasificación de un estudiante mediante su ID
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
def UpdateClassification(connection): #recorre la tabla de academicHistory y cuenta cuantas materias concuerdan con cada ID del estudiante
        cursorObj = connection.cursor()
        SELECT_QUERY_ACAD = "SELECT id FROM academicHistory WHERE id>-1 ORDER BY id ASC"
        SELECT_QUERY_CLAS = "SELECT student_id FROM classification WHERE student_id>-1 ORDER BY student_id ASC"
        SELECT_QUERY_CREDITS = "SELECT credits FROM academicHistory WHERE id>-1 ORDER BY id ASC"
        SELECT_QUERY_SCORE = "SELECT finalNote FROM academicHistory WHERE id >-1 ORDER BY id ASC" #convertimos todas las listas en tuplas para realizar los calculos
        cursorObj.execute(SELECT_QUERY_CLAS)
        CLAStuple=cursorObj.fetchall() #toma las IDs de classification y las convierte en una tupla
        cursorObj.execute(SELECT_QUERY_ACAD)
        ACADtuple=cursorObj.fetchall() #toma las IDs de academicHistory y las convierte en una tupla
        cursorObj.execute(SELECT_QUERY_CREDITS)
        CREDITStuple=cursorObj.fetchall()
        cursorObj.execute(SELECT_QUERY_SCORE)
        SCOREtuple=cursorObj.fetchall()
        for i in range(len(CLAStuple)):
            creditos=0
            materias=0
            promedio=0
            for j in range(len(ACADtuple)):
                if(CLAStuple[i]==ACADtuple[j]):
                    creditos=creditos+CREDITStuple[j][0]
                    materias+=1
                    promedio=promedio+(SCOREtuple[j][0]*CREDITStuple[j][0])
            if(creditos!=0):
                promedio=(promedio/creditos)
            UPDATE_STATEMENT = "UPDATE classification SET creditSum == "+str(creditos)+" WHERE student_id == "+str(CLAStuple[i][0])+""
            cursorObj.execute(UPDATE_STATEMENT)
            UPDATE_STATEMENT2 = "UPDATE classification SET amountSubjects == "+str(materias)+" WHERE student_id == "+str(CLAStuple[i][0])+""
            cursorObj.execute(UPDATE_STATEMENT2)
            UPDATE_STATEMENT3 = "UPDATE classification SET average == "+str(promedio)+" WHERE student_id == "+str(CLAStuple[i][0])+""
            cursorObj.execute(UPDATE_STATEMENT3)
            connection.commit()
        connection.commit()


