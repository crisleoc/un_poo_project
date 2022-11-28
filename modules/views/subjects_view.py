from .main_view import *
from ..classes import subjects as SUBJECTS


class SubjectsView(MainView):

    _connection = None
    _subjectObj = SUBJECTS.subject()

    def __init__(self, connection):
        super(SubjectsView, self).__init__(connection)
        self._connection = connection
        self.ui.label_8.setText("Test Subjects")
