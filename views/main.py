import sys
from ui_interface import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.leftMenuContainer.setFixedWidth(53)
        self.ui.centerMenuContainer.hide()
        self.ui.rightMenuContainer.hide()
        self.ui.closeBtn.clicked.connect(self.closeWindow)
        self.ui.minimizeBtn.clicked.connect(self.minimizeWindow)
        self.ui.restoreBtn.clicked.connect(self.resizeWindow)
        self.ui.settingsBtn.clicked.connect(self.toggleSettingsWidget)
        self.ui.pushButton.clicked.connect(self.hideSettingsWidget)
        self.ui.pushButton_5.clicked.connect(self.toggleNotificationsWidget)
        self.ui.pushButton_6.clicked.connect(self.hideNotificationsWidget)
        self.ui.menuBtn.clicked.connect(self.toggleMainMenuWidget)
        self.ui.studentsBtn.clicked.connect(self.changeToStudentsPage)
        self.ui.subjectsBtn.clicked.connect(self.changeToSubjectsPage)
        self.ui.ahBtn.clicked.connect(self.changeToAhPage)
        self.ui.classifyBtn.clicked.connect(self.changeToClassifyPage)
        self.show()

    def changeToStudentsPage(self):
        self.ui.studentsBtn.setStyleSheet(u"background-color: #1f232a;")
        self.ui.subjectsBtn.setStyleSheet(u"background-color: transparent;")
        self.ui.ahBtn.setStyleSheet(u"background-color: transparent;")
        self.ui.classifyBtn.setStyleSheet(u"background-color: transparent;")
        self.ui.stackedWidget_main.setCurrentIndex(0)

    def changeToSubjectsPage(self):
        self.ui.subjectsBtn.setStyleSheet(u"background-color: #1f232a;")
        self.ui.studentsBtn.setStyleSheet(u"background-color: transparent;")
        self.ui.ahBtn.setStyleSheet(u"background-color: transparent;")
        self.ui.classifyBtn.setStyleSheet(u"background-color: transparent;")
        self.ui.stackedWidget_main.setCurrentIndex(1)

    def changeToAhPage(self):
        self.ui.ahBtn.setStyleSheet(u"background-color: #1f232a;")
        self.ui.subjectsBtn.setStyleSheet(u"background-color: transparent;")
        self.ui.studentsBtn.setStyleSheet(u"background-color: transparent;")
        self.ui.classifyBtn.setStyleSheet(u"background-color: transparent;")
        self.ui.stackedWidget_main.setCurrentIndex(2)

    def changeToClassifyPage(self):
        self.ui.classifyBtn.setStyleSheet(u"background-color: #1f232a;")
        self.ui.subjectsBtn.setStyleSheet(u"background-color: transparent;")
        self.ui.studentsBtn.setStyleSheet(u"background-color: transparent;")
        self.ui.ahBtn.setStyleSheet(u"background-color: transparent;")
        self.ui.stackedWidget_main.setCurrentIndex(3)

    def closeWindow(self):
        self.close()

    def minimizeWindow(self):
        self.showMinimized()

    def resizeWindow(self):
        if self.isMaximized():
            # Show normal size app if it is maximized
            self.showNormal()
            # Change icon to maximize
            icon9 = QIcon()
            icon9.addFile(u":/icons/icons/square.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            self.ui.restoreBtn.setIcon(icon9)
            self.ui.restoreBtn.setIconSize(QSize(20, 20))
        else:
            # Show maximized app if it is normal size
            self.showMaximized()
            # Change icon to restore
            icon9 = QIcon()
            icon9.addFile(u":/icons/icons/copy.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            self.ui.restoreBtn.setIcon(icon9)
            self.ui.restoreBtn.setIconSize(QSize(20, 20))

    def toggleSettingsWidget(self):
        centerCont = self.ui.centerMenuContainer
        if centerCont.isHidden():
            self.ui.settingsBtn.setStyleSheet(u"background-color: #2a2f37;")
            centerCont.show()
        else:
            self.ui.settingsBtn.setStyleSheet(
                u"background-color: transparent;")
            centerCont.hide()

    def hideSettingsWidget(self):
        centerCont = self.ui.centerMenuContainer
        leftCont = self.ui.leftMenuContainer
        mainCont = self.ui.mainBodyContainer
        self.animationCent = QPropertyAnimation(centerCont, b"geometry")
        self.animationMain = QPropertyAnimation(mainCont, b"geometry")
        self.animationCent.setDuration(250)  # chose the value that fits you
        self.animationMain.setDuration(250)
        self.animationCent.setStartValue(centerCont.geometry())
        self.animationMain.setStartValue(mainCont.geometry())
        self.animationCent.setEndValue(
            QRect(leftCont.width(), 0, 0, centerCont.height()))
        self.animationMain.setEndValue(
            QRect(leftCont.width(), 0, (mainCont.width()+centerCont.width()), centerCont.height()))
        self.animationCent.start()
        self.animationMain.start()
        if self.animationCent.state() == QPropertyAnimation.Running:
            self.animationCent.finished.connect(centerCont.hide)
            self.ui.settingsBtn.setStyleSheet(
                u"background-color: transparent;")

    def toggleNotificationsWidget(self):
        rightCont = self.ui.rightMenuContainer
        if rightCont.isHidden():
            rightCont.show()
        else:
            rightCont.hide()

    def hideNotificationsWidget(self):
        rightCont = self.ui.rightMenuContainer
        rightCont.hide()

    def toggleMainMenuWidget(self):
        leftCont = self.ui.leftMenuContainer
        if leftCont.width() == 53:
            leftCont.setFixedWidth(162)
        else:
            leftCont.setFixedWidth(53)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
