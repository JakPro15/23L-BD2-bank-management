# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MenuWidget(object):
    def setupUi(self, MenuWidget):
        if not MenuWidget.objectName():
            MenuWidget.setObjectName(u"MenuWidget")
        MenuWidget.resize(800, 600)
        MenuWidget.setMinimumSize(QSize(800, 600))
        self.horizontalLayout = QHBoxLayout(MenuWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_spacer = QSpacerItem(301, 22, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.left_spacer)

        self.buttons_section = QVBoxLayout()
        self.buttons_section.setObjectName(u"buttons_section")
        self.top_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.buttons_section.addItem(self.top_spacer)

        self.transactions_button = QPushButton(MenuWidget)
        self.transactions_button.setObjectName(u"transactions_button")
        self.transactions_button.setMinimumSize(QSize(400, 60))

        self.buttons_section.addWidget(self.transactions_button)

        self.clients_button = QPushButton(MenuWidget)
        self.clients_button.setObjectName(u"clients_button")
        self.clients_button.setMinimumSize(QSize(400, 60))

        self.buttons_section.addWidget(self.clients_button)

        self.accounts_button = QPushButton(MenuWidget)
        self.accounts_button.setObjectName(u"accounts_button")
        self.accounts_button.setMinimumSize(QSize(400, 60))

        self.buttons_section.addWidget(self.accounts_button)

        self.quit_button = QPushButton(MenuWidget)
        self.quit_button.setObjectName(u"quit_button")
        self.quit_button.setMinimumSize(QSize(400, 60))

        self.buttons_section.addWidget(self.quit_button)

        self.bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.buttons_section.addItem(self.bottom_spacer)


        self.horizontalLayout.addLayout(self.buttons_section)

        self.right_spacer = QSpacerItem(301, 22, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.right_spacer)


        self.retranslateUi(MenuWidget)

        QMetaObject.connectSlotsByName(MenuWidget)
    # setupUi

    def retranslateUi(self, MenuWidget):
        MenuWidget.setWindowTitle(QCoreApplication.translate("MenuWidget", u"Form", None))
        self.transactions_button.setText(QCoreApplication.translate("MenuWidget", u"Transactions", None))
        self.clients_button.setText(QCoreApplication.translate("MenuWidget", u"Clients", None))
        self.accounts_button.setText(QCoreApplication.translate("MenuWidget", u"Accounts", None))
        self.quit_button.setText(QCoreApplication.translate("MenuWidget", u"Quit", None))
    # retranslateUi

