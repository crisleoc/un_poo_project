from .main_view import *
from ..classes import academic_history as AH


class AHView(MainView):

    _connection = None
    _ahObj = AH.academicHistory()

    def __init__(self, connection):
        super(AHView, self).__init__(connection)
        self._connection = connection
        self.showDialog(self.reloadAHData, [])
        self.ui.searchAHStudent.clicked.connect(lambda: self.showDialog(
            self.fillAHTable, [self._ahObj.queryAcademicHistory(self._connection, self.getSearchAHId())]))
        self.ui.refreshAH.clicked.connect(
            lambda: self.showDialog(self.reloadAHData, []))

    def reloadAHData(self):
        self.fillAHTable(
            self._ahObj.selectAllAcademicHistories(self._connection))

    def getSearchAHId(self):
        try:
            id = int(self.ui.lineEdit_searchAH.text())
            return id
        except ValueError:
            self.showErrorDialog("ID must be a number")

    def fillAHTable(self, data):
        self.ui.searchTableAH.setRowCount(0)
        rows = data
        self.ui.searchTableAH.setRowCount(len(rows))
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                self.ui.searchTableAH.setItem(
                    i, j, QTableWidgetItem(str(rows[i][j])))
        self.ui.searchTableAH.resizeColumnsToContents()
        self.ui.searchTableAH.resizeRowsToContents()
