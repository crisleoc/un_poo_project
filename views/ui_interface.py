# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'interfaceUuCZkK.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc


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
                                 "#headerContainer {\n"
                                 "	background-color: #2c313c;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit {\n"
                                 "	background-color: transparent;\n"
                                 "	border: none;\n"
                                 "	border-bottom: 2px solid #fff;\n"
                                 "	padding-bottom: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "QTableWidget {\n"
                                 "	background-color: rgb(255, 255, 255, 0.6);\n"
                                 "	color: rgb(0, 0, "
                                 "0);\n"
                                 "	grid-color: #343b47;\n"
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
        self.label_2 = QLabel(self.page_settings)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(62)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

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

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/bell.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon7)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(
            self.pushButton_5, 0, Qt.AlignHCenter)

        self.horizontalLayout_4.addWidget(self.frame_6)

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
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.createStudentBtn = QPushButton(self.frame_9)
        self.createStudentBtn.setObjectName(u"createStudentBtn")
        self.createStudentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/user-plus.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.createStudentBtn.setIcon(icon11)
        self.createStudentBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.createStudentBtn)

        self.searchStudentBtn = QPushButton(self.frame_9)
        self.searchStudentBtn.setObjectName(u"searchStudentBtn")
        self.searchStudentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/search.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.searchStudentBtn.setIcon(icon12)
        self.searchStudentBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.searchStudentBtn)

        self.updateStudentBtn = QPushButton(self.frame_9)
        self.updateStudentBtn.setObjectName(u"updateStudentBtn")
        self.updateStudentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/refresh-ccw.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.updateStudentBtn.setIcon(icon13)
        self.updateStudentBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.updateStudentBtn)

        self.deleteStudentBtn = QPushButton(self.frame_9)
        self.deleteStudentBtn.setObjectName(u"deleteStudentBtn")
        self.deleteStudentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/trash-2.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.deleteStudentBtn.setIcon(icon14)
        self.deleteStudentBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.deleteStudentBtn)

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
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_createStudent)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setLayoutDirection(Qt.RightToLeft)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -294, 337, 680))
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

        self.lineEdit_7 = QLineEdit(self.frame_16)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setAutoFillBackground(False)

        self.verticalLayout_30.addWidget(self.lineEdit_7)

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

        self.lineEdit_8 = QLineEdit(self.frame_17)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setAutoFillBackground(False)

        self.verticalLayout_31.addWidget(self.lineEdit_8)

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

        self.lineEdit_10 = QLineEdit(self.frame_19)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setAutoFillBackground(False)

        self.verticalLayout_33.addWidget(self.lineEdit_10)

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

        self.lineEdit = QLineEdit(self.frame_10)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAutoFillBackground(False)

        self.verticalLayout_24.addWidget(self.lineEdit)

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

        self.dateEdit = QDateEdit(self.frame_11)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout_25.addWidget(self.dateEdit)

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

        self.dateEdit_2 = QDateEdit(self.frame_12)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.verticalLayout_26.addWidget(self.dateEdit_2)

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

        self.lineEdit_9 = QLineEdit(self.frame_18)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setAutoFillBackground(False)

        self.verticalLayout_32.addWidget(self.lineEdit_9)

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

        self.lineEdit_5 = QLineEdit(self.frame_14)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setAutoFillBackground(False)

        self.verticalLayout_28.addWidget(self.lineEdit_5)

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

        self.lineEdit_6 = QLineEdit(self.frame_15)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setAutoFillBackground(False)

        self.verticalLayout_29.addWidget(self.lineEdit_6)

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

        self.lineEdit_4 = QLineEdit(self.frame_13)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setAutoFillBackground(False)

        self.verticalLayout_27.addWidget(self.lineEdit_4)

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
        self.pushButton_2 = QPushButton(self.frame_20)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/delete.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon15)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_20)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/check-square.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon16)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.pushButton_3)

        self.verticalLayout_20.addWidget(
            self.frame_20, 0, Qt.AlignHCenter | Qt.AlignBottom)

        self.stackedWidget_students.addWidget(self.page_createStudent)
        self.page_searchStudent = QWidget()
        self.page_searchStudent.setObjectName(u"page_searchStudent")
        self.verticalLayout_22 = QVBoxLayout(self.page_searchStudent)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.page_searchStudent)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lineEdit_2 = QLineEdit(self.frame_21)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_12.addWidget(self.lineEdit_2)

        self.pushButton_4 = QPushButton(self.frame_21)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setIcon(icon12)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.pushButton_4)

        self.verticalLayout_22.addWidget(self.frame_21)

        self.tableWidget = QTableWidget(self.page_searchStudent)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem12)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setHorizontalScrollMode(
            QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(41)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_22.addWidget(self.tableWidget)

        self.stackedWidget_students.addWidget(self.page_searchStudent)
        self.page_updateStudent = QWidget()
        self.page_updateStudent.setObjectName(u"page_updateStudent")
        self.verticalLayout_23 = QVBoxLayout(self.page_updateStudent)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_6 = QWidget(self.page_updateStudent)
        self.widget_6.setObjectName(u"widget_6")

        self.verticalLayout_23.addWidget(self.widget_6)

        self.stackedWidget_students.addWidget(self.page_updateStudent)
        self.page_deleteStudent = QWidget()
        self.page_deleteStudent.setObjectName(u"page_deleteStudent")
        self.verticalLayout_21 = QVBoxLayout(self.page_deleteStudent)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_7 = QWidget(self.page_deleteStudent)
        self.widget_7.setObjectName(u"widget_7")

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

        self.rightMenuContainer = QWidget(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_10 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.pushButton_6 = QPushButton(self.frame_8)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.pushButton_6, 0, Qt.AlignRight)

        self.verticalLayout_11.addWidget(self.frame_8)

        self.stackedWidget_notifications = QStackedWidget(
            self.rightMenuSubContainer)
        self.stackedWidget_notifications.setObjectName(
            u"stackedWidget_notifications")
        self.page_notifications = QWidget()
        self.page_notifications.setObjectName(u"page_notifications")
        self.verticalLayout_12 = QVBoxLayout(self.page_notifications)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_6 = QLabel(self.page_notifications)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_6)

        self.stackedWidget_notifications.addWidget(self.page_notifications)

        self.verticalLayout_11.addWidget(self.stackedWidget_notifications)

        self.verticalLayout_10.addWidget(self.rightMenuSubContainer)

        self.horizontalLayout_7.addWidget(
            self.rightMenuContainer, 0, Qt.AlignRight)

        self.verticalLayout_9.addWidget(self.mainBodyContent)

        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_settings.setCurrentIndex(0)
        self.stackedWidget_main.setCurrentIndex(0)
        self.stackedWidget_students.setCurrentIndex(1)

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
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Settings", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"SIA Simulator 2022", None))
# if QT_CONFIG(tooltip)
        self.pushButton_5.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Notifications", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_5.setText("")
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
        self.createStudentBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Add student", None))
#endif // QT_CONFIG(tooltip)
        self.createStudentBtn.setText("")
# if QT_CONFIG(tooltip)
        self.searchStudentBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Search student", None))
#endif // QT_CONFIG(tooltip)
        self.searchStudentBtn.setText("")
# if QT_CONFIG(tooltip)
        self.updateStudentBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Update student", None))
#endif // QT_CONFIG(tooltip)
        self.updateStudentBtn.setText("")
# if QT_CONFIG(tooltip)
        self.deleteStudentBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Delete student", None))
#endif // QT_CONFIG(tooltip)
        self.deleteStudentBtn.setText("")
        self.label_18.setText(
            QCoreApplication.translate("MainWindow", u"ID:", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student id", None))
        self.label_19.setText(QCoreApplication.translate(
            "MainWindow", u"Name:", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student name", None))
        self.label_21.setText(QCoreApplication.translate(
            "MainWindow", u"Lastname:", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student lastname", None))
        self.label_12.setText(QCoreApplication.translate(
            "MainWindow", u"Career:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student career", None))
        self.label_13.setText(QCoreApplication.translate(
            "MainWindow", u"Enter the student born date:", None))
        self.label_14.setText(QCoreApplication.translate(
            "MainWindow", u"Enter the student entry date:", None))
        self.label_20.setText(QCoreApplication.translate(
            "MainWindow", u"Place origin:", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student place origin", None))
        self.label_16.setText(QCoreApplication.translate(
            "MainWindow", u"E-mail:", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student email", None))
        self.label_17.setText(QCoreApplication.translate(
            "MainWindow", u"Enroll quantity:", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student's enrollment number", None))
        self.label_15.setText(QCoreApplication.translate(
            "MainWindow", u"Picture URL:", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student picture URL", None))
# if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(
            QCoreApplication.translate("MainWindow", u"Clear all", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText("")
# if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Create student", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Type the student id to search", None))
# if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Search student", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"LastName", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", u"Career", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", u"Born Date", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", u"Entry Date", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate(
            "MainWindow", u"Place origin", None))
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("MainWindow", u"Email", None))
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate(
            "MainWindow", u"Enroll quantity", None))
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate("MainWindow", u"Picture", None))
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate("MainWindow", u"01", None))
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(
            QCoreApplication.translate("MainWindow", u"02", None))
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText(
            QCoreApplication.translate("MainWindow", u"03", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"Subjects", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"Academic History", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"Classification", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Notifications", None))
# if QT_CONFIG(tooltip)
        self.pushButton_6.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Close notificatios", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_6.setText("")
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Notifications", None))
    # retranslateUi
