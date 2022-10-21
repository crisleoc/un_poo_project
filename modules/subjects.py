def createSubjectsTable(connection):
    """Create the subjects table in the database:

    Args:
        connection (object): Connection to sqlite3.
    """

    CURSOR_OBJ = connection.cursor()
    ID = "id INTEGER PRIMARY KEY NOT NULL UNIQUE"
    NAME = "name TEXT NOT NULL UNIQUE"
    SCHOOL = "school TEXT"
    DEPARTMENT = "department TEXT"
    CREDITS = "credits TEXT"
    LANGUAGE = "language TEXT"
    CREATE_STATEMENT = f"""CREATE TABLE IF NOT EXISTS subjects(
        {ID}, {NAME}, {SCHOOL}, {DEPARTMENT}, {CREDITS}, {LANGUAGE}
        )"""
    CURSOR_OBJ.execute(CREATE_STATEMENT)
    connection.commit()


def insertSubject(connection, subject):
    """Insert a subject in the subjects table:

    Args:
        connection (object): Connection to sqlite3.
        subject (tuple): Tuple containing the elements of the Subjects table.

    """
    cursor_obj = connection.cursor()
    create_statement = "INSERT INTO subject VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor_obj.execute(create_statement, subject)
    connection.commit()


def selectAllSubjects(connection):
    """Select all of the subjects in the Subjects table:

    Args:
        connection (object): Connection to sqlite3.

    Returns:
        list<tuple>: List of tuples with the data of the subjects.
    """
    cursor_obj = connection.cursor()
    create_statement = "SELECT * FROM subjects"
    cursor_obj.execute(create_statement)
    return cursor_obj.fetchall()


def updateSubjects(connection, codmat):

    """Updates and changes the Subjects table's data:
    
    Args:
        connection (object): Connection to sqlite3.
        codmat (int): Integer that contains the code of a specific subject that we want to modify.

    """
    cursor_obj = connection.cursor()
    salirMenu = False
    while not salirMenu:
        opc = input('''
        Menú de Opciones
        1. Cambiar Código
        2. Cambiar Nombre
        3. Cambiar Facultad
        4. Cambiar Departamento
        5. Cambiar Créditos
        6. Cambiar Lenguaje
        7. Cambiar Todo

        Seleccionar opción>>>: ''')

        if (opc == 1):
            newID = input("Digite nuevo código de la materia: ")
            create_statement = 'UPDATE subjects SET ID="' + \
                newID+'" WHERE ID ="'+codmat+'"'
            cursor_obj.execute(create_statement)

        elif (opc == 2):
            newNAME = input("Digite nuevo nombre de la materia: ")
            create_statement = 'UPDATE subjects SET NAME="' + \
                newNAME+'" WHERE ID ="'+codmat+'"'
            cursor_obj.execute(create_statement)
        elif (opc == 3):
            newSCHOOL = input("Digite nueva facultad de la materia: ")
            create_statement = 'UPDATE subjects SET SCHOOL="' + \
                newSCHOOL+'" WHERE ID ="'+codmat+'"'
            cursor_obj.execute(create_statement)
        elif (opc == 4):
            newDEPARTMENT = input("Digite nuevo departamento de la materia: ")
            create_statement = 'UPDATE subjects SET DEPARTMENT="' + \
                newDEPARTMENT+'" WHERE ID ="'+codmat+'"'
            cursor_obj.execute(create_statement)
        elif (opc == 5):
            newCREDITS = input(
                "Digite nueva cantidad de créditos de la materia: ")
            create_statement = 'UPDATE subjects SET CREDITS="' + \
                newCREDITS+'" WHERE ID ="'+codmat+'"'
            cursor_obj.execute(create_statement)
        elif (opc == 6):
            newLANGUAGE = input("Digite nuevo código de la materia: ")
            create_statement = 'UPDATE subjects SET LANGUAGE="' + \
                newLANGUAGE+'" WHERE ID ="'+codmat+'"'
            cursor_obj.execute(create_statement)
        elif (opc == 7):
            newID = input("Digite nuevo código de la materia: ")
            newNAME = input("Digite nuevo nombre de la materia: ")
            newSCHOOL = input("Digite nueva facultad de la materia: ")
            newDEPARTMENT = input("Digite nuevo departamento de la materia: ")
            newCREDITS = input(
                "Digite nueva cantidad de créditos de la materia: ")
            newLANGUAGE = input("Digite nuevo código de la materia: ")
            create_statement = 'UPDATE subjects SET ID="' + \
                newID+'", NAME="' + \
                newNAME+'", SCHOOL="' + \
                newSCHOOL+'", DEPARTMENT="' + \
                newDEPARTMENT+'", CREDITS="' + \
                newCREDITS+'", LANGUAGE="' + \
                newLANGUAGE+'" WHERE ID ="'+codmat+'"'
            cursor_obj.execute(create_statement)
    connection.commit()

def consultarTablaMaterias(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM subjects")
    filas = cursorObj.fetchall()
    print("filas es de tipo: ", type(filas))
    print(filas)
    for row in filas:
        codigo = row[0]
        nombre = row[1]
        print("La información de la materia es: ", codigo, nombre)
        print("La información de la lista es: ", row)
    return filas
