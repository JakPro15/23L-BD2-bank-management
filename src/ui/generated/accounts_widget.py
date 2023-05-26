# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accounts_widget.ui'
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

class Ui_AccountsWidget(object):
    def setupUi(self, AccountsWidget):
        if not AccountsWidget.objectName():
            AccountsWidget.setObjectName(u"AccountsWidget")
        AccountsWidget.resize(800, 600)
        self.horizontalLayout = QHBoxLayout(AccountsWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.account_list = QTableWidget(AccountsWidget)
        if (self.account_list.columnCount() < 4):
            self.account_list.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.account_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.account_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.account_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.account_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.account_list.setObjectName(u"account_list")
        self.account_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.account_list.setAutoScroll(False)
        self.account_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.account_list.setTabKeyNavigation(False)
        self.account_list.setAlternatingRowColors(True)
        self.account_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.account_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.account_list.setSortingEnabled(True)
        self.account_list.setColumnCount(4)
        self.account_list.horizontalHeader().setVisible(True)
        self.account_list.horizontalHeader().setCascadingSectionResizes(False)
        self.account_list.horizontalHeader().setDefaultSectionSize(143)
        self.account_list.horizontalHeader().setHighlightSections(True)
        self.account_list.horizontalHeader().setProperty("showSortIndicator", True)
        self.account_list.horizontalHeader().setStretchLastSection(True)
        self.account_list.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.account_list)

        self.options_section = QVBoxLayout()
        self.options_section.setObjectName(u"options_section")
        self.options_label = QLabel(AccountsWidget)
        self.options_label.setObjectName(u"options_label")
        self.options_label.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.options_label.setFont(font)
        self.options_label.setAlignment(Qt.AlignCenter)

        self.options_section.addWidget(self.options_label)

        self.add_account_button = QPushButton(AccountsWidget)
        self.add_account_button.setObjectName(u"add_account_button")

        self.options_section.addWidget(self.add_account_button)

        self.options_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.options_section.addItem(self.options_spacer)

        self.account_info_button = QPushButton(AccountsWidget)
        self.account_info_button.setObjectName(u"account_info_button")
        self.account_info_button.setEnabled(False)

        self.options_section.addWidget(self.account_info_button)


        self.horizontalLayout.addLayout(self.options_section)


        self.retranslateUi(AccountsWidget)

        QMetaObject.connectSlotsByName(AccountsWidget)
    # setupUi

    def retranslateUi(self, AccountsWidget):
        AccountsWidget.setWindowTitle(QCoreApplication.translate("AccountsWidget", u"Form", None))
        ___qtablewidgetitem = self.account_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AccountsWidget", u"Account number", None));
        ___qtablewidgetitem1 = self.account_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AccountsWidget", u"Creation date", None));
        ___qtablewidgetitem2 = self.account_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AccountsWidget", u"Expiration date", None));
        ___qtablewidgetitem3 = self.account_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AccountsWidget", u"Transaction limit", None));
        self.options_label.setText(QCoreApplication.translate("AccountsWidget", u"Options", None))
        self.add_account_button.setText(QCoreApplication.translate("AccountsWidget", u"Add account...", None))
        self.account_info_button.setText(QCoreApplication.translate("AccountsWidget", u"Detailed account info...", None))
    # retranslateUi

