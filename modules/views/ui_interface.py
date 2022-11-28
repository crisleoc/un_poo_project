# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'interfaceheczLy.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .resources_rc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(952, 582)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(62)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
                                 "	border: none;\n"
                                 "	background-color: transparent;\n"
                                 "	background: transparent;\n"
                                 "	margin: 0;\n"
                                 "	padding: 0;\n"
                                 "	color: #fff;\n"
                                 "	font: 'Segoe UI';\n"
                                 "	font-size: 12px;\n"
                                 "	font-weight: 500;\n"
                                 "}\n"
                                 "\n"
                                 "#centralwidget {\n"
                                 "	background-color: #1f232a;\n"
                                 "}\n"
                                 "\n"
                                 "#leftMenuSubContainer {\n"
                                 "	background-color: #16191d;\n"
                                 "}\n"
                                 "\n"
                                 "#leftMenuSubContainer QPushButton {\n"
                                 "	text-align: left;\n"
                                 "	padding: 5px 10px;\n"
                                 "	border-top-left-radius: 10px;\n"
                                 "	border-bottom-left-radius: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "#centerMenuSubContainer, #rightMenuSubContainer {\n"
                                 "	background-color: #2c313c;\n"
                                 "}\n"
                                 "\n"
                                 "#frame_4, #frame_8, #frame_9 {\n"
                                 "	background-color: #16191d;\n"
                                 "	border-radius: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "#fillDbBtn {\n"
                                 "	background-color: #16191d;\n"
                                 "	border-radius: 10px;\n"
                                 "	padding: 10px 5px;\n"
                                 "}\n"
                                 "\n"
                                 "#fillDbBtn:hover {\n"
                                 "	background-color: #1f232a;\n"
                                 "}\n"
                                 "\n"
                                 "#headerContainer {\n"
                                 "	background-color: #2c313c;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit {\n"
                                 "	background-color: transparent;\n"
                                 "	b"
                                 "order: none;\n"
                                 "	border-bottom: 2px solid #fff;\n"
                                 "	padding-bottom: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "QTableWidget {\n"
                                 "	background-color: rgb(255, 255, 255, 0.6);\n"
                                 "	color: rgb(0, 0, 0);\n"
                                 "	font-size: 11px;\n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::section {\n"
                                 "	background-color: #16191d;\n"
                                 "	border: 1px solid #1f232a;\n"
                                 "	font-size: 11px;\n"
                                 "}\n"
                                 "\n"
                                 "QTableWidget QTableCornerButton::section {\n"
                                 "	background-color: #16191d;\n"
                                 "	border: 1px solid #1f232a;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setStyleSheet(u"font-size: 12px;\n"
                                             "font-weight: 500;")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.menuBtn)

        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.studentsBtn = QPushButton(self.frame_2)
        self.studentsBtn.setObjectName(u"studentsBtn")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(62)
        self.studentsBtn.setFont(font1)
        self.studentsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.studentsBtn.setStyleSheet(u"background-color: #1f232a;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/users.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.studentsBtn.setIcon(icon1)
        self.studentsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.studentsBtn)

        self.subjectsBtn = QPushButton(self.frame_2)
        self.subjectsBtn.setObjectName(u"subjectsBtn")
        self.subjectsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/book-open.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.subjectsBtn.setIcon(icon2)
        self.subjectsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.subjectsBtn)

        self.ahBtn = QPushButton(self.frame_2)
        self.ahBtn.setObjectName(u"ahBtn")
        self.ahBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/file-text.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.ahBtn.setIcon(icon3)
        self.ahBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.ahBtn)

        self.classifyBtn = QPushButton(self.frame_2)
        self.classifyBtn.setObjectName(u"classifyBtn")
        self.classifyBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/info.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.classifyBtn.setIcon(icon4)
        self.classifyBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.classifyBtn)

        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon5)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.settingsBtn)

        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)

        self.verticalLayout.addWidget(
            self.leftMenuSubContainer, 0, Qt.AlignLeft)

        self.horizontalLayout.addWidget(
            self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QWidget(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setStyleSheet(u"font-size: 12px;\n"
                                               "font-weight: 500;")
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_7 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/x-circle.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pushButton, 0, Qt.AlignRight)

        self.verticalLayout_7.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.stackedWidget_settings = QStackedWidget(
            self.centerMenuSubContainer)
        self.stackedWidget_settings.setObjectName(u"stackedWidget_settings")
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_8 = QVBoxLayout(self.page_settings)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_22 = QFrame(self.page_settings)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.fillDbBtn = QPushButton(self.frame_22)
        self.fillDbBtn.setObjectName(u"fillDbBtn")
        self.fillDbBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/database.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.fillDbBtn.setIcon(icon7)
        self.fillDbBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.fillDbBtn, 0, Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.frame_22)

        self.stackedWidget_settings.addWidget(self.page_settings)

        self.verticalLayout_7.addWidget(self.stackedWidget_settings)

        self.verticalLayout_6.addWidget(
            self.centerMenuSubContainer, 0, Qt.AlignLeft)

        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(62)
        self.mainBodyContainer.setFont(font2)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(30, 30))
        self.label_3.setPixmap(QPixmap(u":/images/logo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(99)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"font-size: 14px;\n"
                                   "font-weight: 800;")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/minus.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon8)
        self.minimizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        self.restoreBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/square.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon9)
        self.restoreBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/x.svg", QSize(),
                       QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon10)
        self.closeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeBtn)

        self.horizontalLayout_4.addWidget(self.frame_7, 0, Qt.AlignRight)

        self.verticalLayout_9.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy.setHeightForWidth(
            self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy)
        self.horizontalLayout_7 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mainContentContainer = QWidget(self.mainBodyContent)
        self.mainContentContainer.setObjectName(u"mainContentContainer")
        self.verticalLayout_13 = QVBoxLayout(self.mainContentContainer)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.stackedWidget_main = QStackedWidget(self.mainContentContainer)
        self.stackedWidget_main.setObjectName(u"stackedWidget_main")
        self.page_students = QWidget()
        self.page_students.setObjectName(u"page_students")
        self.verticalLayout_14 = QVBoxLayout(self.page_students)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget = QWidget(self.page_students)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_19 = QVBoxLayout(self.widget)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, 9)
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11, 0, Qt.AlignLeft)

        self.frame_9 = QFrame(self.widget_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QPushButton {\n"
                                   "	padding: 5px;\n"
                                   "	border-radius: 10px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "	background-color: #1f232a\n"
                                   "}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.createStudentBtnMain = QPushButton(self.frame_9)
        self.createStudentBtnMain.setObjectName(u"createStudentBtnMain")
        self.createStudentBtnMain.setCursor(QCursor(Qt.PointingHandCursor))
        self.createStudentBtnMain.setStyleSheet(u"background-color: #2c313c")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/user-plus.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.createStudentBtnMain.setIcon(icon11)
        self.createStudentBtnMain.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.createStudentBtnMain)

        self.searchStudentBtnMain = QPushButton(self.frame_9)
        self.searchStudentBtnMain.setObjectName(u"searchStudentBtnMain")
        self.searchStudentBtnMain.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/search.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.searchStudentBtnMain.setIcon(icon12)
        self.searchStudentBtnMain.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.searchStudentBtnMain)

        self.updateStudentBtnMain = QPushButton(self.frame_9)
        self.updateStudentBtnMain.setObjectName(u"updateStudentBtnMain")
        self.updateStudentBtnMain.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/refresh-ccw.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.updateStudentBtnMain.setIcon(icon13)
        self.updateStudentBtnMain.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.updateStudentBtnMain)

        self.deleteStudentBtnMain = QPushButton(self.frame_9)
        self.deleteStudentBtnMain.setObjectName(u"deleteStudentBtnMain")
        self.deleteStudentBtnMain.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/trash-2.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.deleteStudentBtnMain.setIcon(icon14)
        self.deleteStudentBtnMain.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.deleteStudentBtnMain)

        self.horizontalLayout_9.addWidget(self.frame_9, 0, Qt.AlignRight)

        self.verticalLayout_19.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(
            self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet(u"QFrame QLabel {\n"
                                    "	font-size: 11px;\n"
                                    "}")
        self.verticalLayout_18 = QVBoxLayout(self.widget_3)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_students = QStackedWidget(self.widget_3)
        self.stackedWidget_students.setObjectName(u"stackedWidget_students")
        self.page_createStudent = QWidget()
        self.page_createStudent.setObjectName(u"page_createStudent")
        self.verticalLayout_20 = QVBoxLayout(self.page_createStudent)
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(9, 9, 9, 9)
        self.scrollArea = QScrollArea(self.page_createStudent)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setLayoutDirection(Qt.RightToLeft)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 519, 680))
        self.verticalLayout_34 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.scrollAreaWidgetContents)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_16)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_18 = QLabel(self.frame_16)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_30.addWidget(self.label_18)

        self.lineEdit_cID = QLineEdit(self.frame_16)
        self.lineEdit_cID.setObjectName(u"lineEdit_cID")
        self.lineEdit_cID.setAutoFillBackground(False)

        self.verticalLayout_30.addWidget(self.lineEdit_cID)

        self.verticalLayout_34.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.scrollAreaWidgetContents)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_17)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_19 = QLabel(self.frame_17)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_31.addWidget(self.label_19)

        self.lineEdit_cName = QLineEdit(self.frame_17)
        self.lineEdit_cName.setObjectName(u"lineEdit_cName")
        self.lineEdit_cName.setAutoFillBackground(False)

        self.verticalLayout_31.addWidget(self.lineEdit_cName)

        self.verticalLayout_34.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.scrollAreaWidgetContents)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_19)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_21 = QLabel(self.frame_19)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_33.addWidget(self.label_21)

        self.lineEdit_cLastName = QLineEdit(self.frame_19)
        self.lineEdit_cLastName.setObjectName(u"lineEdit_cLastName")
        self.lineEdit_cLastName.setAutoFillBackground(False)

        self.verticalLayout_33.addWidget(self.lineEdit_cLastName)

        self.verticalLayout_34.addWidget(self.frame_19)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_24.addWidget(self.label_12)

        self.lineEdit_cCareer = QLineEdit(self.frame_10)
        self.lineEdit_cCareer.setObjectName(u"lineEdit_cCareer")
        self.lineEdit_cCareer.setAutoFillBackground(False)

        self.verticalLayout_24.addWidget(self.lineEdit_cCareer)

        self.verticalLayout_34.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_11)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_13 = QLabel(self.frame_11)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_25.addWidget(self.label_13)

        self.dateEdit_cBornD = QDateEdit(self.frame_11)
        self.dateEdit_cBornD.setObjectName(u"dateEdit_cBornD")

        self.verticalLayout_25.addWidget(self.dateEdit_cBornD)

        self.verticalLayout_34.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_12)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_14 = QLabel(self.frame_12)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_26.addWidget(self.label_14)

        self.dateEdit_cEntryD = QDateEdit(self.frame_12)
        self.dateEdit_cEntryD.setObjectName(u"dateEdit_cEntryD")

        self.verticalLayout_26.addWidget(self.dateEdit_cEntryD)

        self.verticalLayout_34.addWidget(self.frame_12)

        self.frame_18 = QFrame(self.scrollAreaWidgetContents)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_18)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_20 = QLabel(self.frame_18)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_32.addWidget(self.label_20)

        self.lineEdit_cOrigin = QLineEdit(self.frame_18)
        self.lineEdit_cOrigin.setObjectName(u"lineEdit_cOrigin")
        self.lineEdit_cOrigin.setAutoFillBackground(False)

        self.verticalLayout_32.addWidget(self.lineEdit_cOrigin)

        self.verticalLayout_34.addWidget(self.frame_18)

        self.frame_14 = QFrame(self.scrollAreaWidgetContents)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_14)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_28.addWidget(self.label_16)

        self.lineEdit_cEmail = QLineEdit(self.frame_14)
        self.lineEdit_cEmail.setObjectName(u"lineEdit_cEmail")
        self.lineEdit_cEmail.setAutoFillBackground(False)

        self.verticalLayout_28.addWidget(self.lineEdit_cEmail)

        self.verticalLayout_34.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_15)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_17 = QLabel(self.frame_15)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_29.addWidget(self.label_17)

        self.lineEdit_cEnroll = QLineEdit(self.frame_15)
        self.lineEdit_cEnroll.setObjectName(u"lineEdit_cEnroll")
        self.lineEdit_cEnroll.setAutoFillBackground(False)

        self.verticalLayout_29.addWidget(self.lineEdit_cEnroll)

        self.verticalLayout_34.addWidget(self.frame_15)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_13)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_27.addWidget(self.label_15)

        self.lineEdit_cPURL = QLineEdit(self.frame_13)
        self.lineEdit_cPURL.setObjectName(u"lineEdit_cPURL")
        self.lineEdit_cPURL.setAutoFillBackground(False)

        self.verticalLayout_27.addWidget(self.lineEdit_cPURL)

        self.verticalLayout_34.addWidget(self.frame_13)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_20.addWidget(self.scrollArea)

        self.frame_20 = QFrame(self.page_createStudent)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_11.setSpacing(30)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.createStudentBtn = QPushButton(self.frame_20)
        self.createStudentBtn.setObjectName(u"createStudentBtn")
        self.createStudentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/check-square.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.createStudentBtn.setIcon(icon15)
        self.createStudentBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.createStudentBtn)

        self.verticalLayout_20.addWidget(
            self.frame_20, 0, Qt.AlignHCenter | Qt.AlignBottom)

        self.stackedWidget_students.addWidget(self.page_createStudent)
        self.page_searchStudent = QWidget()
        self.page_searchStudent.setObjectName(u"page_searchStudent")
        self.verticalLayout_22 = QVBoxLayout(self.page_searchStudent)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(9, 9, 9, 9)
        self.frame_21 = QFrame(self.page_searchStudent)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lineEdit_searchStudentS = QLineEdit(self.frame_21)
        self.lineEdit_searchStudentS.setObjectName(u"lineEdit_searchStudentS")

        self.horizontalLayout_12.addWidget(self.lineEdit_searchStudentS)

        self.searchStudentBtnS = QPushButton(self.frame_21)
        self.searchStudentBtnS.setObjectName(u"searchStudentBtnS")
        self.searchStudentBtnS.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchStudentBtnS.setIcon(icon12)
        self.searchStudentBtnS.setIconSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.searchStudentBtnS)

        self.verticalLayout_22.addWidget(self.frame_21)

        self.searchTableStudents = QTableWidget(self.page_searchStudent)
        if (self.searchTableStudents.columnCount() < 10):
            self.searchTableStudents.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.searchTableStudents.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.searchTableStudents.setHorizontalHeaderItem(
            1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.searchTableStudents.setHorizontalHeaderItem(
            2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.searchTableStudents.setHorizontalHeaderItem(
            3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.searchTableStudents.setHorizontalHeaderItem(
            4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.searchTableStudents.setHorizontalHeaderItem(
            5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.searchTableStudents.setHorizontalHeaderItem(
            6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.searchTableStudents.setHorizontalHeaderItem(
            7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.searchTableStudents.setHorizontalHeaderItem(
            8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.searchTableStudents.setHorizontalHeaderItem(
            9, __qtablewidgetitem9)
        self.searchTableStudents.setObjectName(u"searchTableStudents")
        self.searchTableStudents.setStyleSheet(u"")
        self.searchTableStudents.setAlternatingRowColors(False)
        self.searchTableStudents.setHorizontalScrollMode(
            QAbstractItemView.ScrollPerPixel)
        self.searchTableStudents.setCornerButtonEnabled(False)
        self.searchTableStudents.horizontalHeader().setMinimumSectionSize(41)
        self.searchTableStudents.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_22.addWidget(self.searchTableStudents)

        self.stackedWidget_students.addWidget(self.page_searchStudent)
        self.page_updateStudent = QWidget()
        self.page_updateStudent.setObjectName(u"page_updateStudent")
        self.verticalLayout_23 = QVBoxLayout(self.page_updateStudent)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_6 = QWidget(self.page_updateStudent)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_57 = QVBoxLayout(self.widget_6)
        self.verticalLayout_57.setSpacing(10)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.widget_6)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lineEdit_searchStudentU = QLineEdit(self.frame_23)
        self.lineEdit_searchStudentU.setObjectName(u"lineEdit_searchStudentU")

        self.horizontalLayout_15.addWidget(self.lineEdit_searchStudentU)

        self.searchStudentBtnU = QPushButton(self.frame_23)
        self.searchStudentBtnU.setObjectName(u"searchStudentBtnU")
        self.searchStudentBtnU.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchStudentBtnU.setIcon(icon12)
        self.searchStudentBtnU.setIconSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.searchStudentBtnU)

        self.verticalLayout_57.addWidget(self.frame_23)

        self.scrollArea_2 = QScrollArea(self.widget_6)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setLayoutDirection(Qt.RightToLeft)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(
            u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 519, 609))
        self.verticalLayout_35 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_35)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_33 = QLabel(self.frame_35)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_48.addWidget(self.label_33)

        self.lineEdit_uName = QLineEdit(self.frame_35)
        self.lineEdit_uName.setObjectName(u"lineEdit_uName")
        self.lineEdit_uName.setAutoFillBackground(False)

        self.verticalLayout_48.addWidget(self.lineEdit_uName)

        self.verticalLayout_35.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_36)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_34 = QLabel(self.frame_36)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_49.addWidget(self.label_34)

        self.lineEdit_uLastName = QLineEdit(self.frame_36)
        self.lineEdit_uLastName.setObjectName(u"lineEdit_uLastName")
        self.lineEdit_uLastName.setAutoFillBackground(False)

        self.verticalLayout_49.addWidget(self.lineEdit_uLastName)

        self.verticalLayout_35.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_37)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_35 = QLabel(self.frame_37)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_50.addWidget(self.label_35)

        self.lineEdit_uCareer = QLineEdit(self.frame_37)
        self.lineEdit_uCareer.setObjectName(u"lineEdit_uCareer")
        self.lineEdit_uCareer.setAutoFillBackground(False)

        self.verticalLayout_50.addWidget(self.lineEdit_uCareer)

        self.verticalLayout_35.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_38)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_36 = QLabel(self.frame_38)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_51.addWidget(self.label_36)

        self.dateEdit_uBornD = QDateEdit(self.frame_38)
        self.dateEdit_uBornD.setObjectName(u"dateEdit_uBornD")

        self.verticalLayout_51.addWidget(self.dateEdit_uBornD)

        self.verticalLayout_35.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_39)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_37 = QLabel(self.frame_39)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_52.addWidget(self.label_37)

        self.dateEdit_uEntryD = QDateEdit(self.frame_39)
        self.dateEdit_uEntryD.setObjectName(u"dateEdit_uEntryD")

        self.verticalLayout_52.addWidget(self.dateEdit_uEntryD)

        self.verticalLayout_35.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_40)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_38 = QLabel(self.frame_40)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_53.addWidget(self.label_38)

        self.lineEdit_uOrigin = QLineEdit(self.frame_40)
        self.lineEdit_uOrigin.setObjectName(u"lineEdit_uOrigin")
        self.lineEdit_uOrigin.setAutoFillBackground(False)

        self.verticalLayout_53.addWidget(self.lineEdit_uOrigin)

        self.verticalLayout_35.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_41)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.label_39 = QLabel(self.frame_41)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_54.addWidget(self.label_39)

        self.lineEdit_uEmail = QLineEdit(self.frame_41)
        self.lineEdit_uEmail.setObjectName(u"lineEdit_uEmail")
        self.lineEdit_uEmail.setAutoFillBackground(False)

        self.verticalLayout_54.addWidget(self.lineEdit_uEmail)

        self.verticalLayout_35.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_42)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_40 = QLabel(self.frame_42)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_55.addWidget(self.label_40)

        self.lineEdit_uEnroll = QLineEdit(self.frame_42)
        self.lineEdit_uEnroll.setObjectName(u"lineEdit_uEnroll")
        self.lineEdit_uEnroll.setAutoFillBackground(False)

        self.verticalLayout_55.addWidget(self.lineEdit_uEnroll)

        self.verticalLayout_35.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_43)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_41 = QLabel(self.frame_43)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_56.addWidget(self.label_41)

        self.lineEdit_uPURL = QLineEdit(self.frame_43)
        self.lineEdit_uPURL.setObjectName(u"lineEdit_uPURL")
        self.lineEdit_uPURL.setAutoFillBackground(False)

        self.verticalLayout_56.addWidget(self.lineEdit_uPURL)

        self.verticalLayout_35.addWidget(self.frame_43)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_57.addWidget(self.scrollArea_2)

        self.frame_44 = QFrame(self.widget_6)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_44)
        self.verticalLayout_47.setSpacing(30)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.updateStudentBtn = QPushButton(self.frame_44)
        self.updateStudentBtn.setObjectName(u"updateStudentBtn")
        self.updateStudentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateStudentBtn.setIcon(icon13)
        self.updateStudentBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_47.addWidget(self.updateStudentBtn)

        self.verticalLayout_57.addWidget(
            self.frame_44, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.verticalLayout_23.addWidget(self.widget_6)

        self.stackedWidget_students.addWidget(self.page_updateStudent)
        self.page_deleteStudent = QWidget()
        self.page_deleteStudent.setObjectName(u"page_deleteStudent")
        self.verticalLayout_21 = QVBoxLayout(self.page_deleteStudent)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_7 = QWidget(self.page_deleteStudent)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_59 = QVBoxLayout(self.widget_7)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.widget_7)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lineEdit_searchStudentD = QLineEdit(self.frame_34)
        self.lineEdit_searchStudentD.setObjectName(u"lineEdit_searchStudentD")

        self.horizontalLayout_16.addWidget(self.lineEdit_searchStudentD)

        self.deleteStudentBtn = QPushButton(self.frame_34)
        self.deleteStudentBtn.setObjectName(u"deleteStudentBtn")
        self.deleteStudentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/trash.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.deleteStudentBtn.setIcon(icon16)
        self.deleteStudentBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.deleteStudentBtn)

        self.verticalLayout_59.addWidget(self.frame_34, 0, Qt.AlignTop)

        self.verticalLayout_21.addWidget(self.widget_7)

        self.stackedWidget_students.addWidget(self.page_deleteStudent)

        self.verticalLayout_18.addWidget(self.stackedWidget_students)

        self.verticalLayout_19.addWidget(self.widget_3)

        self.verticalLayout_14.addWidget(self.widget)

        self.stackedWidget_main.addWidget(self.page_students)
        self.page_subjects = QWidget()
        self.page_subjects.setObjectName(u"page_subjects")
        self.verticalLayout_15 = QVBoxLayout(self.page_subjects)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_8 = QLabel(self.page_subjects)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_8)

        self.stackedWidget_main.addWidget(self.page_subjects)
        self.page_ah = QWidget()
        self.page_ah.setObjectName(u"page_ah")
        self.verticalLayout_16 = QVBoxLayout(self.page_ah)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_9 = QLabel(self.page_ah)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_9)

        self.stackedWidget_main.addWidget(self.page_ah)
        self.page_classify = QWidget()
        self.page_classify.setObjectName(u"page_classify")
        self.verticalLayout_17 = QVBoxLayout(self.page_classify)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_10 = QLabel(self.page_classify)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_10)

        self.stackedWidget_main.addWidget(self.page_classify)

        self.verticalLayout_13.addWidget(self.stackedWidget_main)

        self.horizontalLayout_7.addWidget(self.mainContentContainer)

        self.verticalLayout_9.addWidget(self.mainBodyContent)

        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_settings.setCurrentIndex(0)
        self.stackedWidget_main.setCurrentIndex(0)
        self.stackedWidget_students.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
# if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
# if QT_CONFIG(tooltip)
        self.studentsBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go to subjects", None))
#endif // QT_CONFIG(tooltip)
        self.studentsBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Students", None))
# if QT_CONFIG(tooltip)
        self.subjectsBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go to students", None))
#endif // QT_CONFIG(tooltip)
        self.subjectsBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Subjects", None))
# if QT_CONFIG(tooltip)
        self.ahBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go to academic history", None))
#endif // QT_CONFIG(tooltip)
        self.ahBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Academic History", None))
# if QT_CONFIG(tooltip)
        self.classifyBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go to classification", None))
#endif // QT_CONFIG(tooltip)
        self.classifyBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Classification", None))
# if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go to settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Settings Menu", None))
# if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Close Settings", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
        self.fillDbBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Fill DB", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"SIA Simulator 2022", None))
# if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Minimize window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
# if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Restore window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
# if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Close window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_11.setText(QCoreApplication.translate(
            "MainWindow", u"Students", None))
# if QT_CONFIG(tooltip)
        self.createStudentBtnMain.setToolTip(
            QCoreApplication.translate("MainWindow", u"Add student", None))
#endif // QT_CONFIG(tooltip)
        self.createStudentBtnMain.setText("")
# if QT_CONFIG(tooltip)
        self.searchStudentBtnMain.setToolTip(
            QCoreApplication.translate("MainWindow", u"Search student", None))
#endif // QT_CONFIG(tooltip)
        self.searchStudentBtnMain.setText("")
# if QT_CONFIG(tooltip)
        self.updateStudentBtnMain.setToolTip(
            QCoreApplication.translate("MainWindow", u"Update student", None))
#endif // QT_CONFIG(tooltip)
        self.updateStudentBtnMain.setText("")
# if QT_CONFIG(tooltip)
        self.deleteStudentBtnMain.setToolTip(
            QCoreApplication.translate("MainWindow", u"Delete student", None))
#endif // QT_CONFIG(tooltip)
        self.deleteStudentBtnMain.setText("")
        self.label_18.setText(
            QCoreApplication.translate("MainWindow", u"ID:", None))
        self.lineEdit_cID.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student id", None))
        self.label_19.setText(QCoreApplication.translate(
            "MainWindow", u"Name:", None))
        self.lineEdit_cName.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student name", None))
        self.label_21.setText(QCoreApplication.translate(
            "MainWindow", u"Lastname:", None))
        self.lineEdit_cLastName.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student lastname", None))
        self.label_12.setText(QCoreApplication.translate(
            "MainWindow", u"Career:", None))
        self.lineEdit_cCareer.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student career", None))
        self.label_13.setText(QCoreApplication.translate(
            "MainWindow", u"Enter the student born date (yyyy-mm--dd):", None))
        self.dateEdit_cBornD.setDisplayFormat(
            QCoreApplication.translate("MainWindow", u"dd-MM-yyyy", None))
        self.label_14.setText(QCoreApplication.translate(
            "MainWindow", u"Enter the student entry date (yyyy-mm--dd):", None))
        self.dateEdit_cEntryD.setDisplayFormat(
            QCoreApplication.translate("MainWindow", u"dd-MM-yyyy", None))
        self.label_20.setText(QCoreApplication.translate(
            "MainWindow", u"Place origin:", None))
        self.lineEdit_cOrigin.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student place origin", None))
        self.label_16.setText(QCoreApplication.translate(
            "MainWindow", u"E-mail:", None))
        self.lineEdit_cEmail.setText("")
        self.lineEdit_cEmail.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student email", None))
        self.label_17.setText(QCoreApplication.translate(
            "MainWindow", u"Enroll quantity:", None))
        self.lineEdit_cEnroll.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student's enrollment number", None))
        self.label_15.setText(QCoreApplication.translate(
            "MainWindow", u"Picture URL:", None))
        self.lineEdit_cPURL.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student picture URL", None))
# if QT_CONFIG(tooltip)
        self.createStudentBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Create student", None))
#endif // QT_CONFIG(tooltip)
        self.createStudentBtn.setText("")
        self.lineEdit_searchStudentS.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student id to search", None))
# if QT_CONFIG(tooltip)
        self.searchStudentBtnS.setToolTip(
            QCoreApplication.translate("MainWindow", u"Search student", None))
#endif // QT_CONFIG(tooltip)
        self.searchStudentBtnS.setText("")
        ___qtablewidgetitem = self.searchTableStudents.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem1 = self.searchTableStudents.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem2 = self.searchTableStudents.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"LastName", None))
        ___qtablewidgetitem3 = self.searchTableStudents.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", u"Career", None))
        ___qtablewidgetitem4 = self.searchTableStudents.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", u"Born Date", None))
        ___qtablewidgetitem5 = self.searchTableStudents.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", u"Entry Date", None))
        ___qtablewidgetitem6 = self.searchTableStudents.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate(
            "MainWindow", u"Place origin", None))
        ___qtablewidgetitem7 = self.searchTableStudents.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("MainWindow", u"Email", None))
        ___qtablewidgetitem8 = self.searchTableStudents.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate(
            "MainWindow", u"Enroll quantity", None))
        ___qtablewidgetitem9 = self.searchTableStudents.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate("MainWindow", u"Picture", None))
        self.lineEdit_searchStudentU.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student id to update", None))
# if QT_CONFIG(tooltip)
        self.searchStudentBtnU.setToolTip(
            QCoreApplication.translate("MainWindow", u"Search student", None))
#endif // QT_CONFIG(tooltip)
        self.searchStudentBtnU.setText("")
        self.label_33.setText(QCoreApplication.translate(
            "MainWindow", u"Name:", None))
        self.lineEdit_uName.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the new student name", None))
        self.label_34.setText(QCoreApplication.translate(
            "MainWindow", u"Lastname:", None))
        self.lineEdit_uLastName.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the new student lastname", None))
        self.label_35.setText(QCoreApplication.translate(
            "MainWindow", u"Career:", None))
        self.lineEdit_uCareer.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the new student career", None))
        self.label_36.setText(QCoreApplication.translate(
            "MainWindow", u"Enter the new student born date (yyyy-mm--dd):", None))
        self.dateEdit_uBornD.setDisplayFormat(
            QCoreApplication.translate("MainWindow", u"dd-MM-yyyy", None))
        self.label_37.setText(QCoreApplication.translate(
            "MainWindow", u"Enter the new student entry date (yyyy-mm--dd):", None))
        self.dateEdit_uEntryD.setDisplayFormat(
            QCoreApplication.translate("MainWindow", u"dd-MM-yyyy", None))
        self.label_38.setText(QCoreApplication.translate(
            "MainWindow", u"Place origin:", None))
        self.lineEdit_uOrigin.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the new student place origin", None))
        self.label_39.setText(QCoreApplication.translate(
            "MainWindow", u"E-mail:", None))
        self.lineEdit_uEmail.setText("")
        self.lineEdit_uEmail.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the new student email", None))
        self.label_40.setText(QCoreApplication.translate(
            "MainWindow", u"Enroll quantity:", None))
        self.lineEdit_uEnroll.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the new student's enrollment number", None))
        self.label_41.setText(QCoreApplication.translate(
            "MainWindow", u"Picture URL:", None))
        self.lineEdit_uPURL.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the new student picture URL", None))
# if QT_CONFIG(tooltip)
        self.updateStudentBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Update student", None))
#endif // QT_CONFIG(tooltip)
        self.updateStudentBtn.setText("")
        self.lineEdit_searchStudentD.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student id to delete", None))
# if QT_CONFIG(tooltip)
        self.deleteStudentBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Delete student", None))
#endif // QT_CONFIG(tooltip)
        self.deleteStudentBtn.setText("")
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"Subjects", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"Academic History", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"Classification", None))
    # retranslateUi
