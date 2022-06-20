# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 353)
        MainWindow.setMinimumSize(QtCore.QSize(320, 353))
        MainWindow.setMaximumSize(QtCore.QSize(320, 353))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/sectorgen_icon_16x16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.genButton = QtWidgets.QPushButton(self.centralwidget)
        self.genButton.setGeometry(QtCore.QRect(100, 270, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.genButton.setFont(font)
        self.genButton.setObjectName("genButton")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(90, 20, 171, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(60, 20, 31, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.logo.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("T5")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.logo.setFont(font)
        self.logo.setObjectName("logo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.hydroLabel = QtWidgets.QLabel(self.centralwidget)
        self.hydroLabel.setGeometry(QtCore.QRect(10, 100, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.hydroLabel.setFont(font)
        self.hydroLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hydroLabel.setObjectName("hydroLabel")
        self.hydroBox = QtWidgets.QComboBox(self.centralwidget)
        self.hydroBox.setGeometry(QtCore.QRect(120, 100, 171, 22))
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.hydroBox.setFont(font)
        self.hydroBox.setMaxVisibleItems(2)
        self.hydroBox.setMaxCount(2)
        self.hydroBox.setObjectName("hydroBox")
        self.stellar_densityBox = QtWidgets.QComboBox(self.centralwidget)
        self.stellar_densityBox.setGeometry(QtCore.QRect(120, 140, 171, 22))
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.stellar_densityBox.setFont(font)
        self.stellar_densityBox.setMaxVisibleItems(8)
        self.stellar_densityBox.setMaxCount(8)
        self.stellar_densityBox.setObjectName("stellar_densityBox")
        self.stellar_densityLabel = QtWidgets.QLabel(self.centralwidget)
        self.stellar_densityLabel.setGeometry(QtCore.QRect(10, 140, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.stellar_densityLabel.setFont(font)
        self.stellar_densityLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stellar_densityLabel.setObjectName("stellar_densityLabel")
        self.super_earth_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.super_earth_checkBox.setGeometry(QtCore.QRect(80, 240, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.super_earth_checkBox.setFont(font)
        self.super_earth_checkBox.setObjectName("super_earth_checkBox")
        self.allegianceBox = QtWidgets.QComboBox(self.centralwidget)
        self.allegianceBox.setGeometry(QtCore.QRect(120, 180, 171, 22))
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.allegianceBox.setFont(font)
        self.allegianceBox.setMaxVisibleItems(8)
        self.allegianceBox.setMaxCount(8)
        self.allegianceBox.setObjectName("allegianceBox")
        self.allegianceLabel = QtWidgets.QLabel(self.centralwidget)
        self.allegianceLabel.setGeometry(QtCore.QRect(40, 180, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.allegianceLabel.setFont(font)
        self.allegianceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.allegianceLabel.setObjectName("allegianceLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 19))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menuMenu.setFont(font)
        self.menuMenu.setObjectName("menuMenu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menuHelp.setFont(font)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGen = QtWidgets.QAction(MainWindow)
        self.actionGen.setObjectName("actionGen")
        self.actionAbout_SectorGen = QtWidgets.QAction(MainWindow)
        self.actionAbout_SectorGen.setObjectName("actionAbout_SectorGen")
        self.actionQuitProg = QtWidgets.QAction(MainWindow)
        self.actionQuitProg.setObjectName("actionQuitProg")
        self.actionKeep = QtWidgets.QAction(MainWindow)
        self.actionKeep.setEnabled(False)
        self.actionKeep.setObjectName("actionKeep")
        self.actionLockworld = QtWidgets.QAction(MainWindow)
        self.actionLockworld.setEnabled(False)
        self.actionLockworld.setObjectName("actionLockworld")
        self.menuMenu.addAction(self.actionQuitProg)
        self.menuHelp.addAction(self.actionAbout_SectorGen)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.hydroBox, self.stellar_densityBox)
        MainWindow.setTabOrder(self.stellar_densityBox, self.allegianceBox)
        MainWindow.setTabOrder(self.allegianceBox, self.super_earth_checkBox)
        MainWindow.setTabOrder(self.super_earth_checkBox, self.genButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SectorGen 0.4.0 (Beta)"))
        self.genButton.setText(_translate("MainWindow", "Generate"))
        self.label_1.setText(_translate("MainWindow", "TRAVELLER"))
        self.logo.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "Sector Generator"))
        self.hydroLabel.setText(_translate("MainWindow", "Hydrographics"))
        self.stellar_densityLabel.setText(_translate("MainWindow", "Stellar Density"))
        self.super_earth_checkBox.setText(_translate("MainWindow", "Chance for Super-Earths"))
        self.allegianceLabel.setText(_translate("MainWindow", "Allegiance"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionGen.setText(_translate("MainWindow", "Generate Sector"))
        self.actionGen.setStatusTip(_translate("MainWindow", "Generate Sector"))
        self.actionGen.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionAbout_SectorGen.setText(_translate("MainWindow", "About SectorGen"))
        self.actionAbout_SectorGen.setStatusTip(_translate("MainWindow", "About SectorGen"))
        self.actionQuitProg.setText(_translate("MainWindow", "Quit"))
        self.actionQuitProg.setStatusTip(_translate("MainWindow", "Quit this program"))
        self.actionQuitProg.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionKeep.setText(_translate("MainWindow", "Keep"))
        self.actionKeep.setIconText(_translate("MainWindow", "Keep"))
        self.actionKeep.setToolTip(_translate("MainWindow", "Keep"))
        self.actionKeep.setStatusTip(_translate("MainWindow", "Keep Traveller"))
        self.actionKeep.setShortcut(_translate("MainWindow", "Ctrl+K"))
        self.actionLockworld.setText(_translate("MainWindow", "Lock World"))
        self.actionLockworld.setStatusTip(_translate("MainWindow", "Lock Homeworld"))
        self.actionLockworld.setShortcut(_translate("MainWindow", "Ctrl+L"))
import chargen_rc
