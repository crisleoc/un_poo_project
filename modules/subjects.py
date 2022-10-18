def createTableSubjects(connection):
    cursor_obj = connection.cursor()
    codigo = "Código INTEGER PRIMARY KEY NOT NULL UNIQUE"
    nombre = "Nombre TEXT NOT NULL UNIQUE"
    facu = "Dacultad TEXT"
    dep = "Departamento TEXT"
    cred = "Créditos TEXT"
    idioma = "Idioma TEXT"
    create_statement = f"""CREATE TABLE IF NOT EXISTS subjects(
        {codigo}, {nombre}, {facu}, {dep}, {cred}, {idioma}
        )"""
    cursor_obj.execute(create_statement)
    connection.commit()  # Save DB
