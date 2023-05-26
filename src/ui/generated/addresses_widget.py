# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addresses_widget.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_AddressesWidget(object):
    def setupUi(self, AddressesWidget):
        if not AddressesWidget.objectName():
            AddressesWidget.setObjectName(u"AddressesWidget")
        AddressesWidget.resize(800, 600)
        self.horizontalLayout = QHBoxLayout(AddressesWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addresses_list = QTableWidget(AddressesWidget)
        if (self.addresses_list.columnCount() < 6):
            self.addresses_list.setColumnCount(6)
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
        self.addresses_list.setObjectName(u"addresses_list")
        self.addresses_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.addresses_list.setAutoScroll(False)
        self.addresses_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.addresses_list.setTabKeyNavigation(False)
        self.addresses_list.setAlternatingRowColors(True)
        self.addresses_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.addresses_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.addresses_list.setSortingEnabled(True)
        self.addresses_list.setColumnCount(6)
        self.addresses_list.horizontalHeader().setVisible(True)
        self.addresses_list.horizontalHeader().setCascadingSectionResizes(False)
        self.addresses_list.horizontalHeader().setDefaultSectionSize(143)
        self.addresses_list.horizontalHeader().setHighlightSections(True)
        self.addresses_list.horizontalHeader().setProperty("showSortIndicator", True)
        self.addresses_list.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout.addWidget(self.addresses_list)

        self.options_section = QVBoxLayout()
        self.options_section.setObjectName(u"options_section")
        self.options_label = QLabel(AddressesWidget)
        self.options_label.setObjectName(u"options_label")
        self.options_label.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.options_label.setFont(font)
        self.options_label.setAlignment(Qt.AlignCenter)

        self.options_section.addWidget(self.options_label)

        self.add_address_button = QPushButton(AddressesWidget)
        self.add_address_button.setObjectName(u"add_address_button")

        self.options_section.addWidget(self.add_address_button)

        self.options_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.options_section.addItem(self.options_spacer)


        self.horizontalLayout.addLayout(self.options_section)


        self.retranslateUi(AddressesWidget)

        QMetaObject.connectSlotsByName(AddressesWidget)
    # setupUi

    def retranslateUi(self, AddressesWidget):
        AddressesWidget.setWindowTitle(QCoreApplication.translate("AddressesWidget", u"Form", None))
        ___qtablewidgetitem = self.addresses_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AddressesWidget", u"Country", None));
        ___qtablewidgetitem1 = self.addresses_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AddressesWidget", u"City", None));
        ___qtablewidgetitem2 = self.addresses_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AddressesWidget", u"Postcode", None));
        ___qtablewidgetitem3 = self.addresses_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AddressesWidget", u"Street", None));
        ___qtablewidgetitem4 = self.addresses_list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AddressesWidget", u"House number", None));
        ___qtablewidgetitem5 = self.addresses_list.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AddressesWidget", u"Apartment number", None));
        self.options_label.setText(QCoreApplication.translate("AddressesWidget", u"Options", None))
        self.add_address_button.setText(QCoreApplication.translate("AddressesWidget", u"Add address...", None))
    # retranslateUi

