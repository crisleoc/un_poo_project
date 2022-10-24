from unicodedata import name
import modules.connect_db as CONNECT_DB
import modules.students as STUDENTS
import modules.subjects as SUBJECTS
import modules.classification as CLASSIFY
import modules.academic_history as ACADEMIC_HISTORY
def main():

    my_connection = CONNECT_DB.connectionToDB()
    STUDENTS.createStudentTable(my_connection)
    SUBJECTS.createSubjectsTable(my_connection)
    CLASSIFY.createClassificationTable(my_connection)
    ACADEMIC_HISTORY.createAcademicHistoryTable(my_connection)
    #ACADEMIC_HISTORY.addSubject(my_connection)
    CLASSIFY.GetSubjectAmount(my_connection)
    #STUDENTS.insertStudent(my_connection, STUDENTS.readDataUserStudent())
    #SUBJECTS.insertSubject(my_connection,SUBJECTS.readDataUserSubject())
    #CLASSIFY.getstudentinfo(my_connection)
    # people = STUDENTS.selectAllStudents(my_connection)
    # print(people)
    # person = STUDENTS.selectStudentByID(my_connection, 1234)
    # print(person)


if __name__ == "__main__":
    main()
