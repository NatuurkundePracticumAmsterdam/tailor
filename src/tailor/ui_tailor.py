# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tailor.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 700)
        self.actionAdd_column = QAction(MainWindow)
        self.actionAdd_column.setObjectName(u"actionAdd_column")
        self.actionAdd_calculated_column = QAction(MainWindow)
        self.actionAdd_calculated_column.setObjectName(u"actionAdd_calculated_column")
        self.actionAdd_row = QAction(MainWindow)
        self.actionAdd_row.setObjectName(u"actionAdd_row")
        self.actionRemove_column = QAction(MainWindow)
        self.actionRemove_column.setObjectName(u"actionRemove_column")
        self.actionRemove_row = QAction(MainWindow)
        self.actionRemove_row.setObjectName(u"actionRemove_row")
        self.actionImport_CSV = QAction(MainWindow)
        self.actionImport_CSV.setObjectName(u"actionImport_CSV")
        self.actionExport_CSV = QAction(MainWindow)
        self.actionExport_CSV.setObjectName(u"actionExport_CSV")
        self.actionExport_Graph_to_PDF = QAction(MainWindow)
        self.actionExport_Graph_to_PDF.setObjectName(u"actionExport_Graph_to_PDF")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExport_Graph_to_PNG = QAction(MainWindow)
        self.actionExport_Graph_to_PNG.setObjectName(u"actionExport_Graph_to_PNG")
        self.actionType_Strange_Things = QAction(MainWindow)
        self.actionType_Strange_Things.setObjectName(u"actionType_Strange_Things")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout_Tailor = QAction(MainWindow)
        self.actionAbout_Tailor.setObjectName(u"actionAbout_Tailor")
        self.actionImport_CSV_into_project = QAction(MainWindow)
        self.actionImport_CSV_into_project.setObjectName(u"actionImport_CSV_into_project")
        self.actionImport_CSV_Into_Current_Project = QAction(MainWindow)
        self.actionImport_CSV_Into_Current_Project.setObjectName(u"actionImport_CSV_Into_Current_Project")
        self.actionClear_Cell_Contents = QAction(MainWindow)
        self.actionClear_Cell_Contents.setObjectName(u"actionClear_Cell_Contents")
        self.actionClear_Menu = QAction(MainWindow)
        self.actionClear_Menu.setObjectName(u"actionClear_Menu")
        self.actionClear_Menu.setEnabled(False)
        self.actionCheck_for_updates = QAction(MainWindow)
        self.actionCheck_for_updates.setObjectName(u"actionCheck_for_updates")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionAdd_Data_Sheet = QAction(MainWindow)
        self.actionAdd_Data_Sheet.setObjectName(u"actionAdd_Data_Sheet")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMovable(True)

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 37))
        self.menuTable = QMenu(self.menubar)
        self.menuTable.setObjectName(u"menuTable")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOpen_Recent = QMenu(self.menuFile)
        self.menuOpen_Recent.setObjectName(u"menuOpen_Recent")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTable.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuTable.addAction(self.actionAdd_Data_Sheet)
        self.menuTable.addSeparator()
        self.menuTable.addAction(self.actionAdd_column)
        self.menuTable.addAction(self.actionAdd_calculated_column)
        self.menuTable.addAction(self.actionAdd_row)
        self.menuTable.addSeparator()
        self.menuTable.addAction(self.actionRemove_column)
        self.menuTable.addAction(self.actionRemove_row)
        self.menuTable.addSeparator()
        self.menuTable.addAction(self.actionClear_Cell_Contents)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuOpen_Recent.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCheck_for_updates)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_CSV)
        self.menuFile.addAction(self.actionExport_CSV)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_Graph_to_PDF)
        self.menuFile.addAction(self.actionExport_Graph_to_PNG)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuOpen_Recent.addAction(self.actionClear_Menu)
        self.menuHelp.addAction(self.actionAbout_Tailor)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tailor", None))
        self.actionAdd_column.setText(QCoreApplication.translate("MainWindow", u"Add Column", None))
        self.actionAdd_calculated_column.setText(QCoreApplication.translate("MainWindow", u"Add Calculated Column", None))
        self.actionAdd_row.setText(QCoreApplication.translate("MainWindow", u"Add Row", None))
        self.actionRemove_column.setText(QCoreApplication.translate("MainWindow", u"Remove Columns", None))
        self.actionRemove_row.setText(QCoreApplication.translate("MainWindow", u"Remove Rows", None))
        self.actionImport_CSV.setText(QCoreApplication.translate("MainWindow", u"Import CSV", None))
        self.actionExport_CSV.setText(QCoreApplication.translate("MainWindow", u"Export CSV", None))
        self.actionExport_Graph_to_PDF.setText(QCoreApplication.translate("MainWindow", u"Export Graph to PDF", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
        self.actionExport_Graph_to_PNG.setText(QCoreApplication.translate("MainWindow", u"Export Graph to PNG", None))
        self.actionType_Strange_Things.setText(QCoreApplication.translate("MainWindow", u"Type Strange Things", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout_Tailor.setText(QCoreApplication.translate("MainWindow", u"About Tailor", None))
        self.actionImport_CSV_into_project.setText(QCoreApplication.translate("MainWindow", u"Import CSV Into Current Project", None))
        self.actionImport_CSV_Into_Current_Project.setText(QCoreApplication.translate("MainWindow", u"Import CSV Into Current Project", None))
        self.actionClear_Cell_Contents.setText(QCoreApplication.translate("MainWindow", u"Clear Cell Contents", None))
        self.actionClear_Menu.setText(QCoreApplication.translate("MainWindow", u"Clear Menu", None))
        self.actionCheck_for_updates.setText(QCoreApplication.translate("MainWindow", u"Check for updates", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.actionAdd_Data_Sheet.setText(QCoreApplication.translate("MainWindow", u"Add Data Sheet", None))
        self.menuTable.setTitle(QCoreApplication.translate("MainWindow", u"Table", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOpen_Recent.setTitle(QCoreApplication.translate("MainWindow", u"Open Recent", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

