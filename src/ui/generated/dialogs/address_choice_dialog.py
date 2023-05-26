# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'address_choice_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDialog,
    QHBoxLayout, QHeaderView, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_AddressChoiceDialog(object):
    def setupUi(self, AddressChoiceDialog):
        if not AddressChoiceDialog.objectName():
            AddressChoiceDialog.setObjectName(u"AddressChoiceDialog")
        AddressChoiceDialog.resize(600, 600)
        self.verticalLayout = QVBoxLayout(AddressChoiceDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addresses_list = QTableWidget(AddressChoiceDialog)
        if (self.addresses_list.columnCount() < 7):
            self.addresses_list.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.addresses_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.addresses_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.addresses_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.addresses_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.addresses_list.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.addresses_list.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.addresses_list.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.addresses_list.setObjectName(u"addresses_list")
        self.addresses_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.addresses_list.setAutoScroll(False)
        self.addresses_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.addresses_list.setTabKeyNavigation(False)
        self.addresses_list.setAlternatingRowColors(True)
        self.addresses_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.addresses_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.addresses_list.setSortingEnabled(True)
        self.addresses_list.setColumnCount(7)
        self.addresses_list.horizontalHeader().setVisible(True)
        self.addresses_list.horizontalHeader().setCascadingSectionResizes(False)
        self.addresses_list.horizontalHeader().setDefaultSectionSize(143)
        self.addresses_list.horizontalHeader().setHighlightSections(True)
        self.addresses_list.horizontalHeader().setProperty("showSortIndicator", True)
        self.addresses_list.horizontalHeader().setStretchLastSection(True)
        self.addresses_list.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.addresses_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_button = QPushButton(AddressChoiceDialog)
        self.add_button.setObjectName(u"add_button")

        self.horizontalLayout.addWidget(self.add_button)

        self.button_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.button_spacer)

        self.select_button = QPushButton(AddressChoiceDialog)
        self.select_button.setObjectName(u"select_button")

        self.horizontalLayout.addWidget(self.select_button)

        self.cancel_button = QPushButton(AddressChoiceDialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AddressChoiceDialog)
        self.cancel_button.clicked.connect(AddressChoiceDialog.reject)

        QMetaObject.connectSlotsByName(AddressChoiceDialog)
    # setupUi

    def retranslateUi(self, AddressChoiceDialog):
        AddressChoiceDialog.setWindowTitle(QCoreApplication.translate("AddressChoiceDialog", u"Choose address...", None))
        ___qtablewidgetitem = self.addresses_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AddressChoiceDialog", u"ID", None));
        ___qtablewidgetitem1 = self.addresses_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AddressChoiceDialog", u"Country", None));
        ___qtablewidgetitem2 = self.addresses_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AddressChoiceDialog", u"City", None));
        ___qtablewidgetitem3 = self.addresses_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AddressChoiceDialog", u"Postcode", None));
        ___qtablewidgetitem4 = self.addresses_list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AddressChoiceDialog", u"Street", None));
        ___qtablewidgetitem5 = self.addresses_list.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AddressChoiceDialog", u"House number", None));
        ___qtablewidgetitem6 = self.addresses_list.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AddressChoiceDialog", u"Apartment number", None));
        self.add_button.setText(QCoreApplication.translate("AddressChoiceDialog", u"Add address...", None))
        self.select_button.setText(QCoreApplication.translate("AddressChoiceDialog", u"Select", None))
        self.cancel_button.setText(QCoreApplication.translate("AddressChoiceDialog", u"Cancel", None))
    # retranslateUi

