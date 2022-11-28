from .main_view import *
from ..classes import academic_history as AH


class AHView(MainView):

    _connection = None
    _ahObj = AH.academicHistory()

    def __init__(self, connection):
        super(AHView, self).__init__(connection)
        self._connection = connection
        self.ui.label_9.setText("Test Academic History")
