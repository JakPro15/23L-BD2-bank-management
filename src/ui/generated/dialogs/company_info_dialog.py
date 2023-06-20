# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'company_info_dialog.ui'
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
    QFormLayout, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_CompanyInfoDialog(object):
    def setupUi(self, CompanyInfoDialog):
        if not CompanyInfoDialog.objectName():
            CompanyInfoDialog.setObjectName(u"CompanyInfoDialog")
        CompanyInfoDialog.resize(863, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CompanyInfoDialog.sizePolicy().hasHeightForWidth())
        CompanyInfoDialog.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(CompanyInfoDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_section = QFormLayout()
        self.main_section.setObjectName(u"main_section")
        self.main_section.setLabelAlignment(Qt.AlignCenter)
        self.client_id_label = QLabel(CompanyInfoDialog)
        self.client_id_label.setObjectName(u"client_id_label")
        font = QFont()
        font.setBold(True)
        self.client_id_label.setFont(font)

        self.main_section.setWidget(0, QFormLayout.LabelRole, self.client_id_label)

        self.client_id_value = QLabel(CompanyInfoDialog)
        self.client_id_value.setObjectName(u"client_id_value")

        self.main_section.setWidget(0, QFormLayout.FieldRole, self.client_id_value)

        self.address_label = QLabel(CompanyInfoDialog)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setFont(font)

        self.main_section.setWidget(1, QFormLayout.LabelRole, self.address_label)

        self.address_value = QLabel(CompanyInfoDialog)
        self.address_value.setObjectName(u"address_value")

        self.main_section.setWidget(1, QFormLayout.FieldRole, self.address_value)

        self.email_label = QLabel(CompanyInfoDialog)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setFont(font)

        self.main_section.setWidget(2, QFormLayout.LabelRole, self.email_label)

        self.email_value = QLabel(CompanyInfoDialog)
        self.email_value.setObjectName(u"email_value")

        self.main_section.setWidget(2, QFormLayout.FieldRole, self.email_value)

        self.phone_number_label = QLabel(CompanyInfoDialog)
        self.phone_number_label.setObjectName(u"phone_number_label")
        self.phone_number_label.setFont(font)

        self.main_section.setWidget(3, QFormLayout.LabelRole, self.phone_number_label)

        self.phone_number_value = QLabel(CompanyInfoDialog)
        self.phone_number_value.setObjectName(u"phone_number_value")

        self.main_section.setWidget(3, QFormLayout.FieldRole, self.phone_number_value)

        self.name_label = QLabel(CompanyInfoDialog)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setFont(font)

        self.main_section.setWidget(4, QFormLayout.LabelRole, self.name_label)

        self.name_value = QLabel(CompanyInfoDialog)
        self.name_value.setObjectName(u"name_value")

        self.main_section.setWidget(4, QFormLayout.FieldRole, self.name_value)

        self.surname_label = QLabel(CompanyInfoDialog)
        self.surname_label.setObjectName(u"surname_label")
        self.surname_label.setFont(font)

        self.main_section.setWidget(5, QFormLayout.LabelRole, self.surname_label)

        self.nip_value = QLabel(CompanyInfoDialog)
        self.nip_value.setObjectName(u"nip_value")

        self.main_section.setWidget(5, QFormLayout.FieldRole, self.nip_value)

        self.accounts_label = QLabel(CompanyInfoDialog)
        self.accounts_label.setObjectName(u"accounts_label")
        self.accounts_label.setFont(font)

        self.main_section.setWidget(6, QFormLayout.LabelRole, self.accounts_label)

        self.accounts_table = QTableWidget(CompanyInfoDialog)
        if (self.accounts_table.columnCount() < 5):
            self.accounts_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.accounts_table.setObjectName(u"accounts_table")
        self.accounts_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.accounts_table.setAutoScroll(False)
        self.accounts_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.accounts_table.setTabKeyNavigation(False)
        self.accounts_table.setAlternatingRowColors(True)
        self.accounts_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.accounts_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.accounts_table.setSortingEnabled(True)
        self.accounts_table.setColumnCount(5)
        self.accounts_table.horizontalHeader().setVisible(True)
        self.accounts_table.horizontalHeader().setCascadingSectionResizes(False)
        self.accounts_table.horizontalHeader().setDefaultSectionSize(143)
        self.accounts_table.horizontalHeader().setHighlightSections(True)
        self.accounts_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.accounts_table.horizontalHeader().setStretchLastSection(True)
        self.accounts_table.verticalHeader().setVisible(False)

        self.main_section.setWidget(6, QFormLayout.FieldRole, self.accounts_table)


        self.verticalLayout.addLayout(self.main_section)

        self.button_section = QHBoxLayout()
        self.button_section.setObjectName(u"button_section")
        self.button_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.button_section.addItem(self.button_spacer)

        self.back_button = QPushButton(CompanyInfoDialog)
        self.back_button.setObjectName(u"back_button")

        self.button_section.addWidget(self.back_button)


        self.verticalLayout.addLayout(self.button_section)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(CompanyInfoDialog)
        self.back_button.clicked.connect(CompanyInfoDialog.accept)

        QMetaObject.connectSlotsByName(CompanyInfoDialog)
    # setupUi

    def retranslateUi(self, CompanyInfoDialog):
        CompanyInfoDialog.setWindowTitle(QCoreApplication.translate("CompanyInfoDialog", u"Dialog", None))
        self.client_id_label.setText(QCoreApplication.translate("CompanyInfoDialog", u"Client id: ", None))
        self.client_id_value.setText("")
        self.address_label.setText(QCoreApplication.translate("CompanyInfoDialog", u"Address:", None))
        self.address_value.setText("")
        self.email_label.setText(QCoreApplication.translate("CompanyInfoDialog", u"E-mail:", None))
        self.email_value.setText("")
        self.phone_number_label.setText(QCoreApplication.translate("CompanyInfoDialog", u"Phone number:", None))
        self.phone_number_value.setText("")
        self.name_label.setText(QCoreApplication.translate("CompanyInfoDialog", u"Name:", None))
        self.name_value.setText("")
        self.surname_label.setText(QCoreApplication.translate("CompanyInfoDialog", u"NIP:", None))
        self.nip_value.setText("")
        self.accounts_label.setText(QCoreApplication.translate("CompanyInfoDialog", u"Accounts:", None))
        ___qtablewidgetitem = self.accounts_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CompanyInfoDialog", u"Account number", None));
        ___qtablewidgetitem1 = self.accounts_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CompanyInfoDialog", u"Creation date", None));
        ___qtablewidgetitem2 = self.accounts_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CompanyInfoDialog", u"Closing date", None));
        ___qtablewidgetitem3 = self.accounts_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CompanyInfoDialog", u"Transaction limit", None));
        ___qtablewidgetitem4 = self.accounts_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CompanyInfoDialog", u"Account type", None));
        self.back_button.setText(QCoreApplication.translate("CompanyInfoDialog", u"Back...", None))
    # retranslateUi

