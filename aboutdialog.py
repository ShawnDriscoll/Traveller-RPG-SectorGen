# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(397, 365)
        aboutDialog.setMinimumSize(QtCore.QSize(397, 365))
        aboutDialog.setMaximumSize(QtCore.QSize(397, 365))
        self.aboutOKButton = QtWidgets.QPushButton(aboutDialog)
        self.aboutOKButton.setGeometry(QtCore.QRect(280, 320, 75, 23))
        self.aboutOKButton.setObjectName("aboutOKButton")
        self.textLabel = QtWidgets.QLabel(aboutDialog)
        self.textLabel.setGeometry(QtCore.QRect(40, 20, 321, 261))
        self.textLabel.setTextFormat(QtCore.Qt.RichText)
        self.textLabel.setScaledContents(False)
        self.textLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.textLabel.setWordWrap(True)
        self.textLabel.setOpenExternalLinks(True)
        self.textLabel.setObjectName("textLabel")
        self.line = QtWidgets.QFrame(aboutDialog)
        self.line.setGeometry(QtCore.QRect(37, 210, 321, 20))
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About SectorGen"))
        self.aboutOKButton.setText(_translate("aboutDialog", "OK"))
        self.textLabel.setText(_translate("aboutDialog", "<html><head/><body><p><span style=\" font-weight:600;\">SectorGen for Windows 10</span></p><p>Version: Mongoose Traveller Edition</p><p>Build: 0.2.3 (Beta)</p><p>Produced by Shawn Driscoll. Copyright (C) 2022.</p><p>Visit blog at <a href=\"http://shawndriscoll.blogspot.com\"><span style=\" text-decoration: underline; color:#0000ff;\">shawndriscoll.blogspot.com</span></a><br/>For support, email <a href=\"mailto:shawndriscoll@hotmail.com?subject=SectorGen 0.2.3b\"><span style=\" text-decoration: underline; color:#0000ff;\">shawndriscoll@hotmail.com</span></a></p><p>Qt GUI Toolkit is copyright (C) 2020 The Qt Company Ltd</p><p><br/></p><p>The Traveller game in all forms is owned by Far Future Enterprises. Copyright 1977 - 2022 Far Future Enterprises. Traveller is a registered trademark of Far Future Enterprises.</p></body></html>"))
