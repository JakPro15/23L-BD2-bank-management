# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_ClientDialog(object):
    def setupUi(self, ClientDialog):
        if not ClientDialog.objectName():
            ClientDialog.setObjectName(u"ClientDialog")
        ClientDialog.resize(474, 513)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ClientDialog.sizePolicy().hasHeightForWidth())
        ClientDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(ClientDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_section = QFormLayout()
        self.main_section.setObjectName(u"main_section")
        self.main_section.setLabelAlignment(Qt.AlignCenter)
        self.address_label = QLabel(ClientDialog)
        self.address_label.setObjectName(u"address_label")

        self.main_section.setWidget(0, QFormLayout.LabelRole, self.address_label)

        self.address_line_edit = QLineEdit(ClientDialog)
        self.address_line_edit.setObjectName(u"address_line_edit")

        self.main_section.setWidget(0, QFormLayout.FieldRole, self.address_line_edit)

        self.email_line_edit = QLineEdit(ClientDialog)
        self.email_line_edit.setObjectName(u"email_line_edit")

        self.main_section.setWidget(1, QFormLayout.FieldRole, self.email_line_edit)

        self.phone_line_edit = QLineEdit(ClientDialog)
        self.phone_line_edit.setObjectName(u"phone_line_edit")

        self.main_section.setWidget(2, QFormLayout.FieldRole, self.phone_line_edit)

        self.selector_combo_box = QComboBox(ClientDialog)
        self.selector_combo_box.setObjectName(u"selector_combo_box")

        self.main_section.setWidget(3, QFormLayout.FieldRole, self.selector_combo_box)

        self.email_label = QLabel(ClientDialog)
        self.email_label.setObjectName(u"email_label")

        self.main_section.setWidget(1, QFormLayout.LabelRole, self.email_label)

        self.phone_label = QLabel(ClientDialog)
        self.phone_label.setObjectName(u"phone_label")

        self.main_section.setWidget(2, QFormLayout.LabelRole, self.phone_label)

        self.selector_label = QLabel(ClientDialog)
        self.selector_label.setObjectName(u"selector_label")

        self.main_section.setWidget(3, QFormLayout.LabelRole, self.selector_label)


        self.verticalLayout.addLayout(self.main_section)

        self.additional_data_stack = QStackedWidget(ClientDialog)
        self.additional_data_stack.setObjectName(u"additional_data_stack")

        self.verticalLayout.addWidget(self.additional_data_stack)

        self.button_section = QHBoxLayout()
        self.button_section.setObjectName(u"button_section")
        self.button_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.button_section.addItem(self.button_spacer)

        self.create_button = QPushButton(ClientDialog)
        self.create_button.setObjectName(u"create_button")

        self.button_section.addWidget(self.create_button)

        self.cancel_button = QPushButton(ClientDialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.button_section.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.button_section)


        self.retranslateUi(ClientDialog)

        QMetaObject.connectSlotsByName(ClientDialog)
    # setupUi

    def retranslateUi(self, ClientDialog):
        ClientDialog.setWindowTitle(QCoreApplication.translate("ClientDialog", u"Dialog", None))
        self.address_label.setText(QCoreApplication.translate("ClientDialog", u"Address", None))
        self.email_label.setText(QCoreApplication.translate("ClientDialog", u"E-mail", None))
        self.phone_label.setText(QCoreApplication.translate("ClientDialog", u"Phone number", None))
        self.selector_label.setText(QCoreApplication.translate("ClientDialog", u"Account type", None))
        self.create_button.setText(QCoreApplication.translate("ClientDialog", u"Create", None))
        self.cancel_button.setText(QCoreApplication.translate("ClientDialog", u"Cancel", None))
    # retranslateUi

