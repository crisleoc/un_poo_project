from .main_view import *
from ..classes import classification as CLASSiFY
from .. import mails as EMAIL
from .. import config_app as CONFIG


class ClassificationView(MainView):

    _connection = None
    _classifyObj = CLASSiFY.classification()

    def __init__(self, connection):
        super(ClassificationView, self).__init__(connection)
        self._connection = connection
        self.ui.sendMailStudent.hide()
        self.showDialog(self.reloadClassifyData, [])
        self.ui.refreshClassify.clicked.connect(
            lambda: self.showDialog(self.reloadClassifyData, []))
        self.ui.searchClassifyStudent.clicked.connect(lambda: self.showDialog(
            self.fillClassifyTable, [self._classifyObj.selectClassificationByID(self._connection, self.getSearchClassifyId())]))
        self.ui.sendMailStudent.clicked.connect(
            lambda: self.showDialog(self.sendMail, []))
        self.ui.lineEdit_searchClassifyS.textChanged.connect(
            self.ui.sendMailStudent.hide)

    def sendMail(self):
        studentId = int(self.ui.lineEdit_searchClassifyS.text())
        email = EMAIL.get_email(self._connection, studentId)
        msg = EMAIL.sendEmail(email, CONFIG.bodyMail(
            self._classifyObj.selectClassificationByID(self._connection, studentId)))
        return msg

    def getSearchClassifyId(self):
        try:
            id = int(self.ui.lineEdit_searchClassifyS.text())
            self.ui.sendMailStudent.show()
            return id
        except ValueError:
            self.showErrorDialog("ID must be a number")

    def reloadClassifyData(self):
        self._classifyObj.getStudentInfo(self._connection)
        self._classifyObj.UpdateClassification(self._connection)
        self._classifyObj.GetCreditsAmount(self._connection)
        self.fillClassifyTable(
            self._classifyObj.selectAllClassification(self._connection, 'average'))

    def fillClassifyTable(self, data):
        self.ui.searchTableClassify.setRowCount(0)
        rows = data
        self.ui.searchTableClassify.setRowCount(len(rows))
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                self.ui.searchTableClassify.setItem(
                    i, j, QTableWidgetItem(str(rows[i][j])))
        self.ui.searchTableClassify.resizeColumnsToContents()
        self.ui.searchTableClassify.resizeRowsToContents()
