import datetime as dt
from typing import Optional

from PySide6.QtWidgets import QTableWidgetItem, QWidget

from src.database.database import Database
from src.database.table_types import AccountData
from src.helpers import set_optional_str
from src.ui.generated.accounts_widget import Ui_AccountsWidget


class AccountsWidget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_AccountsWidget()
        self._ui.setupUi(self)

    def _load_database(self, database: Database):
        accounts_data = AccountData.load_all(database)
        for data in accounts_data:
            self.insert_data(data)

    def insert_data(self, data: AccountData):
        new_row = self._ui.account_list.rowCount()
        self._ui.account_list.insertRow(new_row)
        row_entry = [
            str(data.account_nr),
            str(data.creation_date.toPython()),
            str(
                data.closing_date.toPython()
                if data.closing_date is not None
                else "N/A"
            ),
            set_optional_str(data.transaction_limit),
        ]
        for id, value in enumerate(row_entry):
            self._ui.account_list.setItem(new_row, id, QTableWidgetItem(value))
