from .main_view import *
from ..classes import classification as CLASSiFY


class ClassificationView(MainView):

    _connection = None
    _classifyObj = CLASSiFY.classification()

    def __init__(self, connection):
        super(ClassificationView, self).__init__(connection)
        self._connection = connection
        self.ui.classifyBtn.clicked.connect(lambda: self.showDialog(
            self.fillClassifyTable, [self._classifyObj.selectAllClassification(self._connection,'average')]))

    def fillClassifyTable(self, data):
        self.ui.TABLE.setRowCount(0)
        rows = data
        self.ui.TABLE.setRowCount(len(rows))
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                self.ui.TABLE.setItem(
                    i, j, QTableWidgetItem(str(rows[i][j])))
        self.ui.TABLE.resizeColumnsToContents()
        self.ui.TABLE.resizeRowsToContents()

    