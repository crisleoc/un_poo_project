from .students_view import *
from .subjects_view import *
from .ah_view import *
from .classify_view import *


class AppMain(StudentsView, SubjectsView, AHView, ClassificationView):
    def __init__(self, connection):
        super(AppMain, self).__init__(connection)
