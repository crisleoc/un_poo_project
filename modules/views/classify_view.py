from .main_view import *
from ..classes import classification as CLASSiFY


class ClassificationView(MainView):

    _connection = None
    _classifyObj = CLASSiFY.classification()

    def __init__(self, connection):
        super(ClassificationView, self).__init__(connection)
        self._connection = connection
        self.ui.label_10.setText("Test classification")
