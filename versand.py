# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'versand.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        mainWindow.setEnabled(True)
        mainWindow.resize(1268, 783)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(30, 30))
        mainWindow.setMaximumSize(QtCore.QSize(1268, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 177, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 177, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 177, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        mainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        mainWindow.setFont(font)
        mainWindow.setMouseTracking(False)
        mainWindow.setTabletTracking(True)
        mainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        mainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        mainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../PDF_Reader_1/foto/pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        mainWindow.setAutoFillBackground(True)
        mainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        mainWindow.setAnimated(True)
        mainWindow.setDocumentMode(False)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        mainWindow.setDockNestingEnabled(False)
        mainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName("centralwidget")
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setEnabled(True)
        self.text.setGeometry(QtCore.QRect(270, 90, 991, 621))
        self.text.setMinimumSize(QtCore.QSize(991, 0))
        self.text.setMaximumSize(QtCore.QSize(991, 621))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.text.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.text.setFont(font)
        self.text.setMouseTracking(True)
        self.text.setTabletTracking(True)
        self.text.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.text.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.text.setAcceptDrops(True)
        self.text.setAutoFillBackground(True)
        self.text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.text.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.text.setUndoRedoEnabled(True)
        self.text.setObjectName("text")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(1230, 230, 21, 191))
        self.verticalScrollBar_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(200, 300, 16, 160))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(20, 10, 93, 61))
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(140, 10, 93, 61))
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(270, 10, 121, 61))
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(420, 10, 93, 61))
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(560, 10, 93, 61))
        self.btn5.setObjectName("btn5")
        self.list = QtWidgets.QListWidget(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(10, 90, 256, 621))
        self.list.setMinimumSize(QtCore.QSize(256, 0))
        self.list.setMaximumSize(QtCore.QSize(256, 621))
        self.list.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.list.setObjectName("list")
        item = QtWidgets.QListWidgetItem()
        self.list.addItem(item)
        self.verticalScrollBar_2.raise_()
        self.verticalScrollBar.raise_()
        self.btn1.raise_()
        self.btn2.raise_()
        self.btn3.raise_()
        self.btn4.raise_()
        self.btn5.raise_()
        self.list.raise_()
        self.text.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setTabletTracking(True)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1268, 29))
        self.menuBar.setObjectName("menuBar")
        self.menuDatei = QtWidgets.QMenu(self.menuBar)
        self.menuDatei.setObjectName("menuDatei")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHilfe = QtWidgets.QMenu(self.menuBar)
        self.menuHilfe.setObjectName("menuHilfe")
        mainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(mainWindow)
        self.toolBar.setObjectName("toolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_ffnen = QtWidgets.QAction(mainWindow)
        self.action_ffnen.setObjectName("action_ffnen")
        self.actionSpeichern_als = QtWidgets.QAction(mainWindow)
        self.actionSpeichern_als.setObjectName("actionSpeichern_als")
        self.actionBeenden = QtWidgets.QAction(mainWindow)
        self.actionBeenden.setObjectName("actionBeenden")
        self.actionSellect_All = QtWidgets.QAction(mainWindow)
        self.actionSellect_All.setObjectName("actionSellect_All")
        self.actionCopy = QtWidgets.QAction(mainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionAuschneiden = QtWidgets.QAction(mainWindow)
        self.actionAuschneiden.setObjectName("actionAuschneiden")
        self.actionEinf_gen = QtWidgets.QAction(mainWindow)
        self.actionEinf_gen.setObjectName("actionEinf_gen")
        self.actionL_schen = QtWidgets.QAction(mainWindow)
        self.actionL_schen.setObjectName("actionL_schen")
        self.actionVersion = QtWidgets.QAction(mainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.menuDatei.addAction(self.action_ffnen)
        self.menuDatei.addAction(self.actionSpeichern_als)
        self.menuDatei.addAction(self.actionBeenden)
        self.menuEdit.addAction(self.actionSellect_All)
        self.menuEdit.addAction(self.actionL_schen)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionAuschneiden)
        self.menuEdit.addAction(self.actionEinf_gen)
        self.menuHilfe.addAction(self.actionVersion)
        self.menuBar.addAction(self.menuDatei.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHilfe.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.btn1, self.btn2)
        mainWindow.setTabOrder(self.btn2, self.btn3)
        mainWindow.setTabOrder(self.btn3, self.btn4)
        mainWindow.setTabOrder(self.btn4, self.btn5)
        mainWindow.setTabOrder(self.btn5, self.list)
        mainWindow.setTabOrder(self.list, self.text)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Versand Aplikation"))
        self.text.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Text Feld</span></p></body></html>"))
        self.btn1.setText(_translate("mainWindow", "Öffnen"))
        self.btn2.setText(_translate("mainWindow", "Speichern"))
        self.btn3.setText(_translate("mainWindow", "Unterschreiben"))
        self.btn4.setText(_translate("mainWindow", "Drcuken"))
        self.btn5.setText(_translate("mainWindow", "Teilen"))
        __sortingEnabled = self.list.isSortingEnabled()
        self.list.setSortingEnabled(False)
        item = self.list.item(0)
        item.setText(_translate("mainWindow", "List"))
        self.list.setSortingEnabled(__sortingEnabled)
        self.menuDatei.setTitle(_translate("mainWindow", "Datei"))
        self.menuEdit.setTitle(_translate("mainWindow", "Edit"))
        self.menuHilfe.setTitle(_translate("mainWindow", "Hilfe"))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar"))
        self.action_ffnen.setText(_translate("mainWindow", "Öffnen"))
        self.actionSpeichern_als.setText(_translate("mainWindow", "Speichern als"))
        self.actionBeenden.setText(_translate("mainWindow", "Beenden"))
        self.actionSellect_All.setText(_translate("mainWindow", "Sellect All"))
        self.actionCopy.setText(_translate("mainWindow", "Kopie"))
        self.actionAuschneiden.setText(_translate("mainWindow", "Auschneiden"))
        self.actionEinf_gen.setText(_translate("mainWindow", "Einfügen"))
        self.actionL_schen.setText(_translate("mainWindow", "Löschen"))
        self.actionVersion.setText(_translate("mainWindow", "Version"))
