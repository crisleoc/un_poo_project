from .main_view import *
from ..classes import students as STUDENTS


class StudentsView(MainView):

    _connection = None
    _studentObj = STUDENTS.student()

    def __init__(self, connection):
        super(StudentsView, self).__init__(connection)
        self._connection = connection
        self.ui.createStudentBtnMain.clicked.connect(
            self.changeToCreateStudentPage)
        self.ui.searchStudentBtnMain.clicked.connect(
            self.changeToSearchStudentPage)
        self.ui.updateStudentBtnMain.clicked.connect(
            self.changeToUpdateStudentPage)
        self.ui.deleteStudentBtnMain.clicked.connect(
            self.changeToDeleteStudentPage)

        self.ui.createStudentBtn.clicked.connect(lambda: self.showDialog(
            self._studentObj.insertStudent, [self._connection, self.getTupleStudentInsert()]))
        self.ui.deleteStudentBtn.clicked.connect(lambda: self.showDialog(
            self._studentObj.deleteStudent, [self._connection, self.getDeleteId()]))
        self.ui.searchStudentBtnS.clicked.connect(lambda: self.showDialog(
            self.fillStudentsTable, [self._studentObj.selectStudentByID(self._connection, self.getSearchStudentId())]))
        self.ui.searchStudentBtnU.clicked.connect(
            lambda: self.showDialog(self.getUpdateStudentId, []))
        self.ui.updateStudentBtn.clicked.connect(
            lambda: self.showDialog(self._studentObj.updateStudentView, [self._connection, self.getUpdateStudentId2(), self.getTupleStudentUpdate()]))

    def getUpdateStudentId2(self):
        try:
            id = int(self.ui.lineEdit_searchStudentU.text())
            return id
        except Exception as e:
            print(str(e))

    def getUpdateStudentId(self):
        try:
            id = int(self.ui.lineEdit_searchStudentU.text())
            studentData = self._studentObj.selectStudentByID(
                self._connection, id)
            self.fillUpdatePlaceHolders(studentData[0])
            return id
        except ValueError:
            self.showErrorDialog("ID must be a number")

    def fillUpdatePlaceHolders(self, studentData):
        self.ui.lineEdit_uName.setText(studentData[1])
        self.ui.lineEdit_uLastName.setText(studentData[2])
        self.ui.lineEdit_uCareer.setText(studentData[3])
        self.ui.dateEdit_uBornD.setDate(
            QDate.fromString(studentData[4], "dd-MM-yyyy"))
        self.ui.dateEdit_uEntryD.setDate(
            QDate.fromString(studentData[5], "dd-MM-yyyy"))
        self.ui.lineEdit_uOrigin.setText(studentData[6])
        self.ui.lineEdit_uEmail.setText(studentData[7])
        self.ui.lineEdit_uEnroll.setText(str(studentData[8]))
        self.ui.lineEdit_uPURL.setText(studentData[9])

    def clearUpdateInputs(self):
        self.ui.lineEdit_uName.clear()
        self.ui.lineEdit_uLastName.clear()
        self.ui.lineEdit_uCareer.clear()
        self.ui.lineEdit_uOrigin.clear()
        self.ui.lineEdit_uEmail.clear()
        self.ui.lineEdit_uEnroll.clear()
        self.ui.lineEdit_uPURL.clear()

    def getSearchStudentId(self):
        try:
            id = int(self.ui.lineEdit_searchStudentS.text())
            return id
        except ValueError:
            self.showErrorDialog("ID must be a number")

    def getDeleteId(self):
        id = self.ui.lineEdit_searchStudentD.text()
        return id

    def fillStudentsTable(self, data):
        self.ui.searchTableStudents.setRowCount(0)
        rows = data
        self.ui.searchTableStudents.setRowCount(len(rows))
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                self.ui.searchTableStudents.setItem(
                    i, j, QTableWidgetItem(str(rows[i][j])))
        self.ui.searchTableStudents.resizeColumnsToContents()
        self.ui.searchTableStudents.resizeRowsToContents()

    def getTupleStudentUpdate(self):
        try:
            name = self.ui.lineEdit_uName.text()
            lastName = self.ui.lineEdit_uLastName.text()
            career = self.ui.lineEdit_uCareer.text()
            bornDate = self.ui.dateEdit_uBornD.date().toString("dd-MM-yyyy")
            entryDate = self.ui.dateEdit_uEntryD.date().toString("dd-MM-yyyy")
            origin = self.ui.lineEdit_uOrigin.text()
            email = self.ui.lineEdit_uEmail.text()
            enrollment = int(self.ui.lineEdit_uEnroll.text())
            pictureURL = self.ui.lineEdit_uPURL.text()
            return (name, lastName, career, bornDate, entryDate, origin, email, enrollment, pictureURL)
        except Exception as e:
            print(str(e))

    def getTupleStudentInsert(self):
        try:
            id = int(self.ui.lineEdit_cID.text())
            name = self.ui.lineEdit_cName.text()
            lastName = self.ui.lineEdit_cLastName.text()
            career = self.ui.lineEdit_cCareer.text()
            bornDate = self.ui.dateEdit_cBornD.date().toString("dd-MM-yyyy")
            entryDate = self.ui.dateEdit_cEntryD.date().toString("dd-MM-yyyy")
            placeOrigin = self.ui.lineEdit_cOrigin.text()
            email = self.ui.lineEdit_cEmail.text()
            enrollQ = int(self.ui.lineEdit_cEnroll.text())
            pic = self.ui.lineEdit_cPURL.text()
            return (id, name, lastName, career, bornDate, entryDate, placeOrigin, email, enrollQ, pic)
        except Exception as e:
            print(str(e))

    def clearInsertInputs(self):
        self.ui.lineEdit_cID.clear()
        self.ui.lineEdit_cName.clear()
        self.ui.lineEdit_cLastName.clear()
        self.ui.lineEdit_cCareer.clear()
        self.ui.lineEdit_cOrigin.clear()
        self.ui.lineEdit_cEmail.clear()
        self.ui.lineEdit_cEnroll.clear()
        self.ui.lineEdit_cPURL.clear()

    def changeToCreateStudentPage(self):
        self.ui.createStudentBtnMain.setStyleSheet(
            u"background-color: #2c313c;")
        self.ui.searchStudentBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.updateStudentBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.deleteStudentBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.stackedWidget_students.setCurrentIndex(0)
        self.clearInsertInputs()

    def changeToSearchStudentPage(self):
        self.ui.searchStudentBtnMain.setStyleSheet(
            u"background-color: #2c313c;")
        self.ui.createStudentBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.updateStudentBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.deleteStudentBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.stackedWidget_students.setCurrentIndex(1)
        self.ui.lineEdit_searchStudentS.clear()
        self.ui.lineEdit_searchStudentS.setFocus()
        students = self._studentObj.selectAllStudents(self._connection)
        self.fillStudentsTable(students)

    def changeToUpdateStudentPage(self):
        self.ui.updateStudentBtnMain.setStyleSheet(
            u"background-color: #2c313c;")
        self.ui.createStudentBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.searchStudentBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.deleteStudentBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.stackedWidget_students.setCurrentIndex(2)
        self.ui.stackedWidget_main.setCurrentIndex(0)
        self.ui.lineEdit_searchStudentU.clear()
        self.ui.lineEdit_searchStudentU.setFocus()
        self.clearUpdateInputs()

    def changeToDeleteStudentPage(self):
        self.ui.deleteStudentBtnMain.setStyleSheet(
            u"background-color: #2c313c;")
        self.ui.createStudentBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.searchStudentBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.updateStudentBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.stackedWidget_students.setCurrentIndex(3)
        self.ui.lineEdit_searchStudentD.clear()
