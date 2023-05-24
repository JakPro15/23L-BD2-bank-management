import datetime as dt
from typing import Optional

from PySide6.QtWidgets import QTableWidgetItem, QWidget

from src.ui.generated.accounts_widget import Ui_AccountsWidget


class AccountsWidget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_AccountsWidget()
        self._ui.setupUi(self)
        self.menu_button_clicked = self._ui.menu_button.clicked
        # self.insert_data(12345, dt.date.today(), dt.date.today(), 100000)
        # self.insert_data(
        #     23456,
        #     dt.date.today() - dt.timedelta(days=1),
        #     dt.date.today() + dt.timedelta(days=1),
        #     80000,
        # )

    def insert_data(
        self,
        account_number: int,
        creation_date: dt.date,
        expiration_date: dt.date,
        transaction_limit: int,
    ):
        new_row = self._ui.account_list.rowCount()
        self._ui.account_list.insertRow(new_row)
        self._ui.account_list.setItem(
            new_row, 0, QTableWidgetItem(str(account_number))
        )
        self._ui.account_list.setItem(
            new_row, 1, QTableWidgetItem(creation_date.isoformat())
        )
        self._ui.account_list.setItem(
            new_row, 2, QTableWidgetItem(expiration_date.isoformat())
        )
        self._ui.account_list.setItem(
            new_row, 3, QTableWidgetItem(str(transaction_limit))
        )
