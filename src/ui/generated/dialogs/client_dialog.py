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
        ClientDialog.resize(400, 450)
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
        self.country_label = QLabel(ClientDialog)
        self.country_label.setObjectName(u"country_label")
        self.country_label.setMinimumSize(QSize(120, 0))
        self.country_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(0, QFormLayout.LabelRole, self.country_label)

        self.city_label = QLabel(ClientDialog)
        self.city_label.setObjectName(u"city_label")
        self.city_label.setMinimumSize(QSize(120, 0))
        self.city_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(1, QFormLayout.LabelRole, self.city_label)

        self.postcode_label = QLabel(ClientDialog)
        self.postcode_label.setObjectName(u"postcode_label")
        self.postcode_label.setMinimumSize(QSize(120, 0))
        self.postcode_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(2, QFormLayout.LabelRole, self.postcode_label)

        self.street_label = QLabel(ClientDialog)
        self.street_label.setObjectName(u"street_label")
        self.street_label.setMinimumSize(QSize(120, 0))
        self.street_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(3, QFormLayout.LabelRole, self.street_label)

        self.house_label = QLabel(ClientDialog)
        self.house_label.setObjectName(u"house_label")
        self.house_label.setMinimumSize(QSize(120, 0))
        self.house_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(4, QFormLayout.LabelRole, self.house_label)

        self.apartment_label = QLabel(ClientDialog)
        self.apartment_label.setObjectName(u"apartment_label")
        self.apartment_label.setMinimumSize(QSize(120, 0))
        self.apartment_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(5, QFormLayout.LabelRole, self.apartment_label)

        self.email_label = QLabel(ClientDialog)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setMinimumSize(QSize(120, 0))
        self.email_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(6, QFormLayout.LabelRole, self.email_label)

        self.email_line_edit = QLineEdit(ClientDialog)
        self.email_line_edit.setObjectName(u"email_line_edit")

        self.main_section.setWidget(6, QFormLayout.FieldRole, self.email_line_edit)

        self.phone_label = QLabel(ClientDialog)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setMinimumSize(QSize(120, 0))
        self.phone_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(7, QFormLayout.LabelRole, self.phone_label)

        self.phone_line_edit = QLineEdit(ClientDialog)
        self.phone_line_edit.setObjectName(u"phone_line_edit")

        self.main_section.setWidget(7, QFormLayout.FieldRole, self.phone_line_edit)

        self.selector_label = QLabel(ClientDialog)
        self.selector_label.setObjectName(u"selector_label")
        self.selector_label.setMinimumSize(QSize(120, 0))
        self.selector_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(8, QFormLayout.LabelRole, self.selector_label)

        self.selector_combo_box = QComboBox(ClientDialog)
        self.selector_combo_box.addItem("")
        self.selector_combo_box.addItem("")
        self.selector_combo_box.setObjectName(u"selector_combo_box")

        self.main_section.setWidget(8, QFormLayout.FieldRole, self.selector_combo_box)

        self.country_line_edit = QLineEdit(ClientDialog)
        self.country_line_edit.setObjectName(u"country_line_edit")

        self.main_section.setWidget(0, QFormLayout.FieldRole, self.country_line_edit)

        self.city_line_edit = QLineEdit(ClientDialog)
        self.city_line_edit.setObjectName(u"city_line_edit")

        self.main_section.setWidget(1, QFormLayout.FieldRole, self.city_line_edit)

        self.postcode_line_edit = QLineEdit(ClientDialog)
        self.postcode_line_edit.setObjectName(u"postcode_line_edit")

        self.main_section.setWidget(2, QFormLayout.FieldRole, self.postcode_line_edit)

        self.street_line_edit = QLineEdit(ClientDialog)
        self.street_line_edit.setObjectName(u"street_line_edit")

        self.main_section.setWidget(3, QFormLayout.FieldRole, self.street_line_edit)

        self.house_line_edit = QLineEdit(ClientDialog)
        self.house_line_edit.setObjectName(u"house_line_edit")

        self.main_section.setWidget(4, QFormLayout.FieldRole, self.house_line_edit)

        self.apartment_line_edit = QLineEdit(ClientDialog)
        self.apartment_line_edit.setObjectName(u"apartment_line_edit")

        self.main_section.setWidget(5, QFormLayout.FieldRole, self.apartment_line_edit)


        self.verticalLayout.addLayout(self.main_section)

        self.additional_data_stack = QStackedWidget(ClientDialog)
        self.additional_data_stack.setObjectName(u"additional_data_stack")
        self.person_page = QWidget()
        self.person_page.setObjectName(u"person_page")
        self.verticalLayout_2 = QVBoxLayout(self.person_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.person_section = QFormLayout()
        self.person_section.setObjectName(u"person_section")
        self.person_section.setLabelAlignment(Qt.AlignCenter)
        self.person_name_label = QLabel(self.person_page)
        self.person_name_label.setObjectName(u"person_name_label")
        self.person_name_label.setMinimumSize(QSize(120, 0))
        self.person_name_label.setAlignment(Qt.AlignCenter)

        self.person_section.setWidget(0, QFormLayout.LabelRole, self.person_name_label)

        self.person_surname_label = QLabel(self.person_page)
        self.person_surname_label.setObjectName(u"person_surname_label")
        self.person_surname_label.setMinimumSize(QSize(120, 0))
        self.person_surname_label.setAlignment(Qt.AlignCenter)

        self.person_section.setWidget(1, QFormLayout.LabelRole, self.person_surname_label)

        self.person_pesel_label = QLabel(self.person_page)
        self.person_pesel_label.setObjectName(u"person_pesel_label")
        self.person_pesel_label.setMinimumSize(QSize(120, 0))
        self.person_pesel_label.setAlignment(Qt.AlignCenter)

        self.person_section.setWidget(2, QFormLayout.LabelRole, self.person_pesel_label)

        self.person_sex_label = QLabel(self.person_page)
        self.person_sex_label.setObjectName(u"person_sex_label")
        self.person_sex_label.setMinimumSize(QSize(120, 0))
        self.person_sex_label.setAlignment(Qt.AlignCenter)

        self.person_section.setWidget(3, QFormLayout.LabelRole, self.person_sex_label)

        self.person_name_line_edit = QLineEdit(self.person_page)
        self.person_name_line_edit.setObjectName(u"person_name_line_edit")

        self.person_section.setWidget(0, QFormLayout.FieldRole, self.person_name_line_edit)

        self.person_surname_line_edit = QLineEdit(self.person_page)
        self.person_surname_line_edit.setObjectName(u"person_surname_line_edit")

        self.person_section.setWidget(1, QFormLayout.FieldRole, self.person_surname_line_edit)

        self.person_pesel_line_edit = QLineEdit(self.person_page)
        self.person_pesel_line_edit.setObjectName(u"person_pesel_line_edit")

        self.person_section.setWidget(2, QFormLayout.FieldRole, self.person_pesel_line_edit)

        self.person_sex_combo_box = QComboBox(self.person_page)
        self.person_sex_combo_box.addItem("")
        self.person_sex_combo_box.addItem("")
        self.person_sex_combo_box.setObjectName(u"person_sex_combo_box")

        self.person_section.setWidget(3, QFormLayout.FieldRole, self.person_sex_combo_box)


        self.verticalLayout_2.addLayout(self.person_section)

        self.additional_data_stack.addWidget(self.person_page)
        self.company_page = QWidget()
        self.company_page.setObjectName(u"company_page")
        self.verticalLayout_3 = QVBoxLayout(self.company_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.company_section = QFormLayout()
        self.company_section.setObjectName(u"company_section")
        self.company_section.setLabelAlignment(Qt.AlignCenter)
        self.company_name_label = QLabel(self.company_page)
        self.company_name_label.setObjectName(u"company_name_label")
        self.company_name_label.setMinimumSize(QSize(120, 0))
        self.company_name_label.setAlignment(Qt.AlignCenter)

        self.company_section.setWidget(0, QFormLayout.LabelRole, self.company_name_label)

        self.company_nip_label = QLabel(self.company_page)
        self.company_nip_label.setObjectName(u"company_nip_label")
        self.company_nip_label.setMinimumSize(QSize(120, 0))
        self.company_nip_label.setAlignment(Qt.AlignCenter)

        self.company_section.setWidget(1, QFormLayout.LabelRole, self.company_nip_label)

        self.company_name_line_edit = QLineEdit(self.company_page)
        self.company_name_line_edit.setObjectName(u"company_name_line_edit")

        self.company_section.setWidget(0, QFormLayout.FieldRole, self.company_name_line_edit)

        self.company_nip_line_edit = QLineEdit(self.company_page)
        self.company_nip_line_edit.setObjectName(u"company_nip_line_edit")

        self.company_section.setWidget(1, QFormLayout.FieldRole, self.company_nip_line_edit)


        self.verticalLayout_3.addLayout(self.company_section)

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
        self.country_label.setText(QCoreApplication.translate("ClientDialog", u"Country", None))
        self.city_label.setText(QCoreApplication.translate("ClientDialog", u"City", None))
        self.postcode_label.setText(QCoreApplication.translate("ClientDialog", u"Postcode", None))
        self.street_label.setText(QCoreApplication.translate("ClientDialog", u"Street", None))
        self.house_label.setText(QCoreApplication.translate("ClientDialog", u"House number", None))
        self.apartment_label.setText(QCoreApplication.translate("ClientDialog", u"Apartment number", None))
        self.email_label.setText(QCoreApplication.translate("ClientDialog", u"E-mail", None))
        self.phone_label.setText(QCoreApplication.translate("ClientDialog", u"Phone number", None))
        self.selector_label.setText(QCoreApplication.translate("ClientDialog", u"Account type", None))
        self.selector_combo_box.setItemText(0, QCoreApplication.translate("ClientDialog", u"Person", None))
        self.selector_combo_box.setItemText(1, QCoreApplication.translate("ClientDialog", u"Company", None))

        self.person_name_label.setText(QCoreApplication.translate("ClientDialog", u"Name", None))
        self.person_surname_label.setText(QCoreApplication.translate("ClientDialog", u"Surname", None))
        self.person_pesel_label.setText(QCoreApplication.translate("ClientDialog", u"PESEL", None))
        self.person_sex_label.setText(QCoreApplication.translate("ClientDialog", u"Sex", None))
        self.person_sex_combo_box.setItemText(0, QCoreApplication.translate("ClientDialog", u"K", None))
        self.person_sex_combo_box.setItemText(1, QCoreApplication.translate("ClientDialog", u"M", None))

        self.company_name_label.setText(QCoreApplication.translate("ClientDialog", u"Name", None))
        self.company_nip_label.setText(QCoreApplication.translate("ClientDialog", u"NIP", None))
        self.create_button.setText(QCoreApplication.translate("ClientDialog", u"Create", None))
        self.cancel_button.setText(QCoreApplication.translate("ClientDialog", u"Cancel", None))
    # retranslateUi

