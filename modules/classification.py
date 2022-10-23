def createClassificationTable(connection):
    # recorremos la base de datos con el objeto de conexión
    cursorObj = connection.cursor()
    STUDENT_ID = "student_id INTEGER PRIMARY KEY"
    NAME = "name TEXT"
    LAST_NAME = "lastName TEXT"
    AMOUNT_SUBJECTS = "amountSubjects INTEGER"
    CREDIT_SUM = "creditSum INTEGER"
    AVERAGE = "average INTEGER"
    CREATE_STATEMENT = f"CREATE TABLE IF NOT EXISTS classification({STUDENT_ID},{NAME},{LAST_NAME},{AMOUNT_SUBJECTS},{CREDIT_SUM},{AVERAGE})"
    cursorObj.execute(CREATE_STATEMENT)  # creamos la tabla materias
    connection.commit()  # aseguramos la persistencia guardando la tabla en el disco
