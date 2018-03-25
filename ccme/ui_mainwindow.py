# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/ccmidi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(525, 321)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(7, 7, 325, 112))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.midiChannel = QtGui.QSpinBox(self.widget)
        self.midiChannel.setMaximum(16)
        self.midiChannel.setProperty("value", 1)
        self.midiChannel.setObjectName(_fromUtf8("midiChannel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.midiChannel)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.midiController = QtGui.QSpinBox(self.widget)
        self.midiController.setMinimum(1)
        self.midiController.setMaximum(95)
        self.midiController.setProperty("value", 10)
        self.midiController.setObjectName(_fromUtf8("midiController"))
        self.horizontalLayout_2.addWidget(self.midiController)
        self.controllerName = QtGui.QLabel(self.widget)
        self.controllerName.setObjectName(_fromUtf8("controllerName"))
        self.horizontalLayout_2.addWidget(self.controllerName)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.midiCcValue = QtGui.QSlider(self.widget)
        self.midiCcValue.setMaximum(128)
        self.midiCcValue.setOrientation(QtCore.Qt.Horizontal)
        self.midiCcValue.setObjectName(_fromUtf8("midiCcValue"))
        self.verticalLayout.addWidget(self.midiCcValue)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn0 = QtGui.QPushButton(self.widget)
        self.btn0.setObjectName(_fromUtf8("btn0"))
        self.horizontalLayout.addWidget(self.btn0)
        self.btn64 = QtGui.QPushButton(self.widget)
        self.btn64.setObjectName(_fromUtf8("btn64"))
        self.horizontalLayout.addWidget(self.btn64)
        self.btn128 = QtGui.QPushButton(self.widget)
        self.btn128.setObjectName(_fromUtf8("btn128"))
        self.horizontalLayout.addWidget(self.btn128)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout_Qt = QtGui.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(_fromUtf8("actionAbout_Qt"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.label.setBuddy(self.midiChannel)
        self.label_2.setBuddy(self.midiController)
        self.label_3.setBuddy(self.midiCcValue)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CCMe", None))
        self.label.setText(_translate("MainWindow", "Cha&nnel", None))
        self.label_2.setText(_translate("MainWindow", "&Controller", None))
        self.controllerName.setText(_translate("MainWindow", "Pan", None))
        self.label_3.setText(_translate("MainWindow", "&Value", None))
        self.btn0.setText(_translate("MainWindow", "Set &0", None))
        self.btn0.setShortcut(_translate("MainWindow", "Ctrl+0", None))
        self.btn64.setText(_translate("MainWindow", "Set &64", None))
        self.btn64.setShortcut(_translate("MainWindow", "Ctrl+6", None))
        self.btn128.setText(_translate("MainWindow", "Set &128", None))
        self.btn128.setShortcut(_translate("MainWindow", "Ctrl+1", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help", None))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt", None))
        self.actionQuit.setText(_translate("MainWindow", "&Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))

