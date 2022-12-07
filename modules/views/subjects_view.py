from .main_view import *
from ..classes import subjects as SUBJECTS


class SubjectsView(MainView):

    _connection = None
    _subjectObj = SUBJECTS.subject()

    def __init__(self, connection):
        super(SubjectsView, self).__init__(connection)
        self._connection = connection
        self.ui.createSubjectBtnMain.clicked.connect(
            self.changeToCreateSubjectPage)
        self.ui.searchSubjectBtnMain.clicked.connect(
            self.changeToSearchSubjectPage)
        self.ui.updateSubjectBtnMain.clicked.connect(
            self.changeToUpdateSubjectPage)
        self.ui.deleteSubjectBtnMain.clicked.connect(
            self.changeToDeleteSubjectPage)

        self.ui.createSubjectBtn.clicked.connect(lambda: self.showDialog(
            self._subjectObj.insertSubject, [self._connection, self.getTupleSubjectInsert()]))
        self.ui.searchSubjectBtnS.clicked.connect(lambda: self.showDialog(
            self.fillSubjectsTable, [self._subjectObj.selectSubjectByID(self._connection, self.getSearchSubjectCode())]))
        self.ui.searchSubjectBtnU.clicked.connect(
            lambda: self.showDialog(self.getUpdateSubjectCode, []))
        self.ui.updateSubjectBtn.clicked.connect(
            lambda: self.showDialog(self._subjectObj.updateSubjectView, [self._connection, self.getUpdateSubjectCode2(), self.getTupleSubjectUpdate()]))
        self.ui.deleteSubjectBtn.clicked.connect(lambda: self.showDialog(
            self._subjectObj.deleteSubject, [self._connection, self.getDeleteSubCode()]))

    def getDeleteSubCode(self):
        id = self.ui.lineEdit_searchSubjectD.text()
        return id

    def getUpdateSubjectCode2(self):
        try:
            code = int(self.ui.lineEdit_searchSubjectU.text())
            return code
        except Exception as e:
            print(str(e))

    def getUpdateSubjectCode(self):
        try:
            code = int(self.ui.lineEdit_searchSubjectU.text())
            subjectData = self._subjectObj.selectSubjectByID(
                self._connection, code)
            self.fillSubjectUpdateInputs(subjectData[0])
            return code
        except ValueError:
            self.showErrorDialog("ID must be a number")

    def fillSubjectUpdateInputs(self, subjectData):
        self.ui.lineEdit_uSubName.setText(subjectData[1])
        self.ui.lineEdit_uSubSchool.setText(subjectData[2])
        self.ui.lineEdit_uSubDepartment.setText(subjectData[3])
        self.ui.lineEdit_uSubCredits.setText(str(subjectData[4]))
        self.ui.lineEdit_uSubLanguage.setText(subjectData[5])

    def getSearchSubjectCode(self):
        try:
            id = int(self.ui.lineEdit_searchSubjectS.text())
            return id
        except ValueError:
            self.showErrorDialog("ID must be a number")

    def fillSubjectsTable(self, data):
        self.ui.searchTableSubject.setRowCount(0)
        rows = data
        self.ui.searchTableSubject.setRowCount(len(rows))
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                self.ui.searchTableSubject.setItem(
                    i, j, QTableWidgetItem(str(rows[i][j])))
        self.ui.searchTableSubject.resizeColumnsToContents()
        self.ui.searchTableSubject.resizeRowsToContents()

    def getTupleSubjectUpdate(self):
        try:
            name = self.ui.lineEdit_uSubName.text()
            school = self.ui.lineEdit_uSubSchool.text()
            department = self.ui.lineEdit_uSubDepartment.text()
            credits = int(self.ui.lineEdit_uSubCredits.text())
            language = self.ui.lineEdit_uSubLanguage.text()
            return (name, school, department, credits, language)
        except Exception as e:
            print(e)

    def getTupleSubjectInsert(self):
        try:
            code = int(self.ui.lineEdit_cSubCode.text())
            name = self.ui.lineEdit_cSubName.text()
            school = self.ui.lineEdit_cSubSchool.text()
            department = self.ui.lineEdit_cSubDepartment.text()
            credits = int(self.ui.lineEdit_cSubCredits.text())
            language = self.ui.lineEdit_cSubLanguage.text()
            return (code, name, school, department, credits, language)
        except Exception as e:
            print(e)

    def clearSubjectCreateInputs(self):
        self.ui.lineEdit_cSubCode.clear()
        self.ui.lineEdit_cSubName.clear()
        self.ui.lineEdit_cSubSchool.clear()
        self.ui.lineEdit_cSubDepartment.clear()
        self.ui.lineEdit_cSubCredits.clear()
        self.ui.lineEdit_cSubLanguage.clear()

    def clearSubjectUpdateInputs(self):
        self.ui.lineEdit_uSubName.clear()
        self.ui.lineEdit_uSubSchool.clear()
        self.ui.lineEdit_uSubDepartment.clear()
        self.ui.lineEdit_uSubCredits.clear()
        self.ui.lineEdit_cSubLanguage.clear()

    def changeToCreateSubjectPage(self):
        self.ui.createSubjectBtnMain.setStyleSheet(
            u"background-color: #2c313c;")
        self.ui.searchSubjectBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.updateSubjectBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.deleteSubjectBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.clearSubjectCreateInputs()
        self.ui.stackedWidget_subjects.setCurrentIndex(0)

    def changeToSearchSubjectPage(self):
        self.ui.searchSubjectBtnMain.setStyleSheet(
            u"background-color: #2c313c;")
        self.ui.createSubjectBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.updateSubjectBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.deleteSubjectBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.stackedWidget_subjects.setCurrentIndex(1)
        self.ui.lineEdit_searchSubjectS.clear()
        self.ui.lineEdit_searchSubjectS.setFocus()
        subjects = self._subjectObj.selectAllSubjects(self._connection)
        self.fillSubjectsTable(subjects)

    def changeToUpdateSubjectPage(self):
        self.ui.updateSubjectBtnMain.setStyleSheet(
            u"background-color: #2c313c;")
        self.ui.createSubjectBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.searchSubjectBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.deleteSubjectBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.clearSubjectUpdateInputs()
        self.ui.lineEdit_searchSubjectU.setFocus()
        self.ui.stackedWidget_subjects.setCurrentIndex(2)

    def changeToDeleteSubjectPage(self):
        self.ui.deleteSubjectBtnMain.setStyleSheet(
            u"background-color: #2c313c;")
        self.ui.createSubjectBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.searchSubjectBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.updateSubjectBtnMain.setStyleSheet(
            u"background-color: transparent;")
        self.ui.lineEdit_searchSubjectD.setFocus()
        self.ui.stackedWidget_subjects.setCurrentIndex(3)
