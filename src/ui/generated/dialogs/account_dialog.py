# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDialog,
    QFormLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_AccountDialog(object):
    def setupUi(self, AccountDialog):
        if not AccountDialog.objectName():
            AccountDialog.setObjectName(u"AccountDialog")
        AccountDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(AccountDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_section = QFormLayout()
        self.main_section.setObjectName(u"main_section")
        self.main_section.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.account_number_label = QLabel(AccountDialog)
        self.account_number_label.setObjectName(u"account_number_label")

        self.main_section.setWidget(0, QFormLayout.LabelRole, self.account_number_label)

        self.type_version_label = QLabel(AccountDialog)
        self.type_version_label.setObjectName(u"type_version_label")

        self.main_section.setWidget(7, QFormLayout.LabelRole, self.type_version_label)

        self.creation_date_label = QLabel(AccountDialog)
        self.creation_date_label.setObjectName(u"creation_date_label")

        self.main_section.setWidget(2, QFormLayout.LabelRole, self.creation_date_label)

        self.type_name_label = QLabel(AccountDialog)
        self.type_name_label.setObjectName(u"type_name_label")

        self.main_section.setWidget(6, QFormLayout.LabelRole, self.type_name_label)

        self.transaction_limit_label = QLabel(AccountDialog)
        self.transaction_limit_label.setObjectName(u"transaction_limit_label")

        self.main_section.setWidget(5, QFormLayout.LabelRole, self.transaction_limit_label)

        self.account_number_edit = QLineEdit(AccountDialog)
        self.account_number_edit.setObjectName(u"account_number_edit")

        self.main_section.setWidget(0, QFormLayout.FieldRole, self.account_number_edit)

        self.transaction_limit_edit = QLineEdit(AccountDialog)
        self.transaction_limit_edit.setObjectName(u"transaction_limit_edit")

        self.main_section.setWidget(5, QFormLayout.FieldRole, self.transaction_limit_edit)

        self.type_name_edit = QLineEdit(AccountDialog)
        self.type_name_edit.setObjectName(u"type_name_edit")

        self.main_section.setWidget(6, QFormLayout.FieldRole, self.type_name_edit)

        self.type_version_edit = QLineEdit(AccountDialog)
        self.type_version_edit.setObjectName(u"type_version_edit")

        self.main_section.setWidget(7, QFormLayout.FieldRole, self.type_version_edit)

        self.creation_date_edit = QDateEdit(AccountDialog)
        self.creation_date_edit.setObjectName(u"creation_date_edit")

        self.main_section.setWidget(2, QFormLayout.FieldRole, self.creation_date_edit)

        self.closing_date_check = QCheckBox(AccountDialog)
        self.closing_date_check.setObjectName(u"closing_date_check")

        self.main_section.setWidget(3, QFormLayout.LabelRole, self.closing_date_check)

        self.closing_date_edit = QDateEdit(AccountDialog)
        self.closing_date_edit.setObjectName(u"closing_date_edit")
        self.closing_date_edit.setEnabled(False)

        self.main_section.setWidget(3, QFormLayout.FieldRole, self.closing_date_edit)


        self.verticalLayout.addLayout(self.main_section)

        self.main_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.main_spacer)

        self.button_section = QHBoxLayout()
        self.button_section.setObjectName(u"button_section")
        self.button_section.setSizeConstraint(QLayout.SetMinimumSize)
        self.button_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.button_section.addItem(self.button_spacer)

        self.create_button = QPushButton(AccountDialog)
        self.create_button.setObjectName(u"create_button")

        self.button_section.addWidget(self.create_button)

        self.cancel_button = QPushButton(AccountDialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.button_section.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.button_section)


        self.retranslateUi(AccountDialog)
        self.closing_date_check.toggled.connect(self.closing_date_edit.setEnabled)
        self.cancel_button.clicked.connect(AccountDialog.reject)

        QMetaObject.connectSlotsByName(AccountDialog)
    # setupUi

    def retranslateUi(self, AccountDialog):
        AccountDialog.setWindowTitle(QCoreApplication.translate("AccountDialog", u"Add account...", None))
        self.account_number_label.setText(QCoreApplication.translate("AccountDialog", u"Account number", None))
        self.type_version_label.setText(QCoreApplication.translate("AccountDialog", u"Account type version", None))
        self.creation_date_label.setText(QCoreApplication.translate("AccountDialog", u"Creation date", None))
        self.type_name_label.setText(QCoreApplication.translate("AccountDialog", u"Account type name", None))
        self.transaction_limit_label.setText(QCoreApplication.translate("AccountDialog", u"Transaction limit", None))
        self.closing_date_check.setText(QCoreApplication.translate("AccountDialog", u"Closing date", None))
        self.create_button.setText(QCoreApplication.translate("AccountDialog", u"Create", None))
        self.cancel_button.setText(QCoreApplication.translate("AccountDialog", u"Cancel", None))
    # retranslateUi

