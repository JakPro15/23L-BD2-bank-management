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
        ClientDialog.resize(400, 300)
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
        self.email_label = QLabel(ClientDialog)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setMinimumSize(QSize(96, 0))
        self.email_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(2, QFormLayout.LabelRole, self.email_label)

        self.email_line_edit = QLineEdit(ClientDialog)
        self.email_line_edit.setObjectName(u"email_line_edit")

        self.main_section.setWidget(2, QFormLayout.FieldRole, self.email_line_edit)

        self.phone_label = QLabel(ClientDialog)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setMinimumSize(QSize(96, 0))
        self.phone_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(3, QFormLayout.LabelRole, self.phone_label)

        self.phone_line_edit = QLineEdit(ClientDialog)
        self.phone_line_edit.setObjectName(u"phone_line_edit")

        self.main_section.setWidget(3, QFormLayout.FieldRole, self.phone_line_edit)

        self.selector_label = QLabel(ClientDialog)
        self.selector_label.setObjectName(u"selector_label")
        self.selector_label.setMinimumSize(QSize(96, 0))
        self.selector_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(4, QFormLayout.LabelRole, self.selector_label)

        self.selector_combo_box = QComboBox(ClientDialog)
        self.selector_combo_box.addItem("")
        self.selector_combo_box.addItem("")
        self.selector_combo_box.setObjectName(u"selector_combo_box")

        self.main_section.setWidget(4, QFormLayout.FieldRole, self.selector_combo_box)

        self.address_section = QHBoxLayout()
        self.address_section.setObjectName(u"address_section")
        self.address_button = QPushButton(ClientDialog)
        self.address_button.setObjectName(u"address_button")

        self.address_section.addWidget(self.address_button)

        self.address_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.address_section.addItem(self.address_spacer)

        self.id_label = QLabel(ClientDialog)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setEnabled(False)

        self.address_section.addWidget(self.id_label)

        self.id_value_label = QLabel(ClientDialog)
        self.id_value_label.setObjectName(u"id_value_label")
        self.id_value_label.setEnabled(False)

        self.address_section.addWidget(self.id_value_label)


        self.main_section.setLayout(1, QFormLayout.FieldRole, self.address_section)

        self.address_label = QLabel(ClientDialog)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setMinimumSize(QSize(96, 0))
        self.address_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(1, QFormLayout.LabelRole, self.address_label)


        self.verticalLayout.addLayout(self.main_section)

        self.additional_data_stack = QStackedWidget(ClientDialog)
        self.additional_data_stack.setObjectName(u"additional_data_stack")
        self.person_page = QWidget()
        self.person_page.setObjectName(u"person_page")
        self.verticalLayout_2 = QVBoxLayout(self.person_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.label = QLabel(self.person_page)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(96, 0))
        self.label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.person_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(96, 0))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.person_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(96, 0))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.person_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(96, 0))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.lineEdit = QLineEdit(self.person_page)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.person_page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.person_page)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.comboBox = QComboBox(self.person_page)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.additional_data_stack.addWidget(self.person_page)
        self.company_page = QWidget()
        self.company_page.setObjectName(u"company_page")
        self.verticalLayout_3 = QVBoxLayout(self.company_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.company_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(96, 0))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.company_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(96, 0))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_4 = QLineEdit(self.company_page)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.company_page)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_5)


        self.verticalLayout_3.addLayout(self.formLayout_2)

        self.additional_data_stack.addWidget(self.company_page)

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
        self.cancel_button.clicked.connect(ClientDialog.reject)
        self.selector_combo_box.currentIndexChanged.connect(self.additional_data_stack.setCurrentIndex)

        self.additional_data_stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ClientDialog)
    # setupUi

    def retranslateUi(self, ClientDialog):
        ClientDialog.setWindowTitle(QCoreApplication.translate("ClientDialog", u"Add client...", None))
        self.email_label.setText(QCoreApplication.translate("ClientDialog", u"E-mail", None))
        self.phone_label.setText(QCoreApplication.translate("ClientDialog", u"Phone number", None))
        self.selector_label.setText(QCoreApplication.translate("ClientDialog", u"Account type", None))
        self.selector_combo_box.setItemText(0, QCoreApplication.translate("ClientDialog", u"Person", None))
        self.selector_combo_box.setItemText(1, QCoreApplication.translate("ClientDialog", u"Company", None))

        self.address_button.setText(QCoreApplication.translate("ClientDialog", u"Choose address...", None))
        self.id_label.setText(QCoreApplication.translate("ClientDialog", u"ID:", None))
        self.id_value_label.setText("")
        self.address_label.setText(QCoreApplication.translate("ClientDialog", u"Address", None))
        self.label.setText(QCoreApplication.translate("ClientDialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("ClientDialog", u"Surname", None))
        self.label_3.setText(QCoreApplication.translate("ClientDialog", u"PESEL", None))
        self.label_4.setText(QCoreApplication.translate("ClientDialog", u"Sex", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("ClientDialog", u"K", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("ClientDialog", u"M", None))

        self.label_5.setText(QCoreApplication.translate("ClientDialog", u"Name", None))
        self.label_6.setText(QCoreApplication.translate("ClientDialog", u"NIP", None))
        self.create_button.setText(QCoreApplication.translate("ClientDialog", u"Create", None))
        self.cancel_button.setText(QCoreApplication.translate("ClientDialog", u"Cancel", None))
    # retranslateUi

