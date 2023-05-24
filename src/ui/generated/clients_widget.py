# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clients_widget.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_ClientsWidget(object):
    def setupUi(self, ClientsWidget):
        if not ClientsWidget.objectName():
            ClientsWidget.setObjectName(u"ClientsWidget")
        ClientsWidget.resize(800, 600)
        self.horizontalLayout = QHBoxLayout(ClientsWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.table_stack = QStackedWidget(ClientsWidget)
        self.table_stack.setObjectName(u"table_stack")
        self.people_page = QWidget()
        self.people_page.setObjectName(u"people_page")
        self.verticalLayout = QVBoxLayout(self.people_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.people_table = QTableWidget(self.people_page)
        if (self.people_table.columnCount() < 7):
            self.people_table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.people_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.people_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.people_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.people_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.people_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.people_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.people_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.people_table.setObjectName(u"people_table")
        self.people_table.setAutoScroll(False)
        self.people_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.people_table.setTabKeyNavigation(False)
        self.people_table.setAlternatingRowColors(True)
        self.people_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.people_table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.people_table)

        self.table_stack.addWidget(self.people_page)
        self.companies_page = QWidget()
        self.companies_page.setObjectName(u"companies_page")
        self.verticalLayout_2 = QVBoxLayout(self.companies_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.companies_table = QTableWidget(self.companies_page)
        if (self.companies_table.columnCount() < 5):
            self.companies_table.setColumnCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.companies_table.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.companies_table.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.companies_table.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.companies_table.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.companies_table.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        self.companies_table.setObjectName(u"companies_table")
        self.companies_table.setAutoScroll(False)
        self.companies_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.companies_table.setTabKeyNavigation(False)
        self.companies_table.setAlternatingRowColors(True)
        self.companies_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.companies_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.companies_table.setSortingEnabled(True)
        self.companies_table.horizontalHeader().setDefaultSectionSize(110)
        self.companies_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.companies_table)

        self.table_stack.addWidget(self.companies_page)

        self.horizontalLayout.addWidget(self.table_stack)

        self.options_section = QVBoxLayout()
        self.options_section.setObjectName(u"options_section")
        self.account_type_label = QLabel(ClientsWidget)
        self.account_type_label.setObjectName(u"account_type_label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.account_type_label.setFont(font)
        self.account_type_label.setAlignment(Qt.AlignCenter)

        self.options_section.addWidget(self.account_type_label)

        self.account_type_combo = QComboBox(ClientsWidget)
        self.account_type_combo.addItem("")
        self.account_type_combo.addItem("")
        self.account_type_combo.setObjectName(u"account_type_combo")

        self.options_section.addWidget(self.account_type_combo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.options_section.addItem(self.verticalSpacer)

        self.options_label = QLabel(ClientsWidget)
        self.options_label.setObjectName(u"options_label")
        self.options_label.setMinimumSize(QSize(200, 0))
        self.options_label.setFont(font)
        self.options_label.setAlignment(Qt.AlignCenter)

        self.options_section.addWidget(self.options_label)

        self.add_account_button = QPushButton(ClientsWidget)
        self.add_account_button.setObjectName(u"add_account_button")

        self.options_section.addWidget(self.add_account_button)

        self.options_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.options_section.addItem(self.options_spacer)

        self.account_info_button = QPushButton(ClientsWidget)
        self.account_info_button.setObjectName(u"account_info_button")
        self.account_info_button.setEnabled(False)

        self.options_section.addWidget(self.account_info_button)

        self.menu_button = QPushButton(ClientsWidget)
        self.menu_button.setObjectName(u"menu_button")

        self.options_section.addWidget(self.menu_button)


        self.horizontalLayout.addLayout(self.options_section)


        self.retranslateUi(ClientsWidget)
        self.account_type_combo.currentIndexChanged.connect(self.table_stack.setCurrentIndex)

        self.table_stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ClientsWidget)
    # setupUi

    def retranslateUi(self, ClientsWidget):
        ClientsWidget.setWindowTitle(QCoreApplication.translate("ClientsWidget", u"Form", None))
        ___qtablewidgetitem = self.people_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ClientsWidget", u"Address", None));
        ___qtablewidgetitem1 = self.people_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ClientsWidget", u"E-mail", None));
        ___qtablewidgetitem2 = self.people_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ClientsWidget", u"Phone number", None));
        ___qtablewidgetitem3 = self.people_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ClientsWidget", u"Name", None));
        ___qtablewidgetitem4 = self.people_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ClientsWidget", u"Surname", None));
        ___qtablewidgetitem5 = self.people_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ClientsWidget", u"PESEL", None));
        ___qtablewidgetitem6 = self.people_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ClientsWidget", u"Sex", None));
        ___qtablewidgetitem7 = self.companies_table.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ClientsWidget", u"Address", None));
        ___qtablewidgetitem8 = self.companies_table.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ClientsWidget", u"E-mail", None));
        ___qtablewidgetitem9 = self.companies_table.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ClientsWidget", u"Phone number", None));
        ___qtablewidgetitem10 = self.companies_table.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("ClientsWidget", u"Name", None));
        ___qtablewidgetitem11 = self.companies_table.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("ClientsWidget", u"NIP", None));
        self.account_type_label.setText(QCoreApplication.translate("ClientsWidget", u"Account type", None))
        self.account_type_combo.setItemText(0, QCoreApplication.translate("ClientsWidget", u"Person", None))
        self.account_type_combo.setItemText(1, QCoreApplication.translate("ClientsWidget", u"Company", None))

        self.options_label.setText(QCoreApplication.translate("ClientsWidget", u"Options", None))
        self.add_account_button.setText(QCoreApplication.translate("ClientsWidget", u"Add client...", None))
        self.account_info_button.setText(QCoreApplication.translate("ClientsWidget", u"Detailed client info...", None))
        self.menu_button.setText(QCoreApplication.translate("ClientsWidget", u"Back to main menu", None))
    # retranslateUi

