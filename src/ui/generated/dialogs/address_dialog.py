# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'address_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_AddressDialog(object):
    def setupUi(self, AddressDialog):
        if not AddressDialog.objectName():
            AddressDialog.setObjectName(u"AddressDialog")
        AddressDialog.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddressDialog.sizePolicy().hasHeightForWidth())
        AddressDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(AddressDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_section = QFormLayout()
        self.main_section.setObjectName(u"main_section")
        self.main_section.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.country_label = QLabel(AddressDialog)
        self.country_label.setObjectName(u"country_label")
        self.country_label.setMinimumSize(QSize(120, 0))
        self.country_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(0, QFormLayout.LabelRole, self.country_label)

        self.city_label = QLabel(AddressDialog)
        self.city_label.setObjectName(u"city_label")
        self.city_label.setMinimumSize(QSize(120, 0))
        self.city_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(1, QFormLayout.LabelRole, self.city_label)

        self.postcode_label = QLabel(AddressDialog)
        self.postcode_label.setObjectName(u"postcode_label")
        self.postcode_label.setMinimumSize(QSize(120, 0))
        self.postcode_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(2, QFormLayout.LabelRole, self.postcode_label)

        self.street_label = QLabel(AddressDialog)
        self.street_label.setObjectName(u"street_label")
        self.street_label.setMinimumSize(QSize(120, 0))
        self.street_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(3, QFormLayout.LabelRole, self.street_label)

        self.house_label = QLabel(AddressDialog)
        self.house_label.setObjectName(u"house_label")
        self.house_label.setMinimumSize(QSize(120, 0))
        self.house_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(4, QFormLayout.LabelRole, self.house_label)

        self.apartment_label = QLabel(AddressDialog)
        self.apartment_label.setObjectName(u"apartment_label")
        self.apartment_label.setMinimumSize(QSize(120, 0))
        self.apartment_label.setAlignment(Qt.AlignCenter)

        self.main_section.setWidget(5, QFormLayout.LabelRole, self.apartment_label)

        self.country_line_edit = QLineEdit(AddressDialog)
        self.country_line_edit.setObjectName(u"country_line_edit")

        self.main_section.setWidget(0, QFormLayout.FieldRole, self.country_line_edit)

        self.city_line_edit = QLineEdit(AddressDialog)
        self.city_line_edit.setObjectName(u"city_line_edit")

        self.main_section.setWidget(1, QFormLayout.FieldRole, self.city_line_edit)

        self.postcode_line_edit = QLineEdit(AddressDialog)
        self.postcode_line_edit.setObjectName(u"postcode_line_edit")

        self.main_section.setWidget(2, QFormLayout.FieldRole, self.postcode_line_edit)

        self.street_line_edit = QLineEdit(AddressDialog)
        self.street_line_edit.setObjectName(u"street_line_edit")

        self.main_section.setWidget(3, QFormLayout.FieldRole, self.street_line_edit)

        self.house_line_edit = QLineEdit(AddressDialog)
        self.house_line_edit.setObjectName(u"house_line_edit")

        self.main_section.setWidget(4, QFormLayout.FieldRole, self.house_line_edit)

        self.apartment_line_edit = QLineEdit(AddressDialog)
        self.apartment_line_edit.setObjectName(u"apartment_line_edit")

        self.main_section.setWidget(5, QFormLayout.FieldRole, self.apartment_line_edit)


        self.verticalLayout.addLayout(self.main_section)

        self.sections_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.sections_spacer)

        self.button_section = QHBoxLayout()
        self.button_section.setObjectName(u"button_section")
        self.button_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.button_section.addItem(self.button_spacer)

        self.create_button = QPushButton(AddressDialog)
        self.create_button.setObjectName(u"create_button")

        self.button_section.addWidget(self.create_button)

        self.cancel_button = QPushButton(AddressDialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.button_section.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.button_section)


        self.retranslateUi(AddressDialog)
        self.cancel_button.clicked.connect(AddressDialog.reject)

        QMetaObject.connectSlotsByName(AddressDialog)
    # setupUi

    def retranslateUi(self, AddressDialog):
        AddressDialog.setWindowTitle(QCoreApplication.translate("AddressDialog", u"Dialog", None))
        self.country_label.setText(QCoreApplication.translate("AddressDialog", u"Country", None))
        self.city_label.setText(QCoreApplication.translate("AddressDialog", u"City", None))
        self.postcode_label.setText(QCoreApplication.translate("AddressDialog", u"Postcode", None))
        self.street_label.setText(QCoreApplication.translate("AddressDialog", u"Street", None))
        self.house_label.setText(QCoreApplication.translate("AddressDialog", u"House number", None))
        self.apartment_label.setText(QCoreApplication.translate("AddressDialog", u"Apartment number", None))
        self.create_button.setText(QCoreApplication.translate("AddressDialog", u"Create", None))
        self.cancel_button.setText(QCoreApplication.translate("AddressDialog", u"Cancel", None))
    # retranslateUi

