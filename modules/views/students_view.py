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
            self._studentObj.insertStudent, [self._connection, self.getTupleStudent()]))

    def getTupleStudent(self):
        try:
            id = int(self.ui.lineEdit_cID.text())
            name = self.ui.lineEdit_cName.text()
            lastName = self.ui.lineEdit_cLastName.text()
            career = self.ui.lineEdit_cCareer.text()
            bornDateTuple = self.ui.dateEdit_cBornD.date().getDate()
            bornDate = f"{bornDateTuple[2]}-{bornDateTuple[1]}-{bornDateTuple[0]}"
            entryDateTuple = self.ui.dateEdit_cEntryD.date().getDate()
            entryDate = f"{entryDateTuple[2]}-{entryDateTuple[1]}-{entryDateTuple[0]}"
            placeOrigin = self.ui.lineEdit_cOrigin.text()
            email = self.ui.lineEdit_cEmail.text()
            enrollQ = int(self.ui.lineEdit_cEnroll.text())
            pic = self.ui.lineEdit_cPURL.text()
            return (id, name, lastName, career, bornDate, entryDate, placeOrigin, email, enrollQ, pic)
        except Exception as e:
            print(str(e))

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
