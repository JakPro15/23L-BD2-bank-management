import datetime as dt
from typing import Optional

from PySide6.QtWidgets import QMessageBox, QTableWidgetItem, QWidget

from src.database.database import Database
from src.database.database_errors import DatabaseTransactionError
from src.database.table_types import AccountData
from src.helpers import set_optional_str
from src.ui.dialogs.account_dialog import AccountDialog
from src.ui.dialogs.confirm_dialog import ConfirmDialog
from src.ui.generated.accounts_widget import Ui_AccountsWidget


class AccountsWidget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_AccountsWidget()
        self._ui.setupUi(self)
        self._account_dialog = AccountDialog(self)
        self._ui.account_list.currentCellChanged.connect(
            self._enable_lower_buttons
        )
        self._ui.add_account_button.clicked.connect(
            self._add_account_procedure
        )
        self._ui.delete_button.clicked.connect(self._delete_procedure)
        self._ui.account_info_button.clicked.connect(
            lambda: print(
                [i for i in self._current_account().clients(self._database)]
            )
        )

    def _add_account_procedure(self):
        self._account_dialog.load_database(self._database)
        result = self._account_dialog.exec()
        if result:
            self._reload_database()

    def _delete_account(self, data: AccountData):
        data.delete(self._database)
        self._reload_database()

    def _current_account(self) -> AccountData:
        idx = self._ui.account_list.currentRow()
        return self._accounts_data[idx]

    def _delete_procedure(self):
        result = ConfirmDialog(self).exec()
        match result:
            case QMessageBox.Cancel:
                print("keep")
            case QMessageBox.Ok:
                data = self._current_account()
                try:
                    self._delete_account(data)
                    print("deleted")
                except DatabaseTransactionError as e:
                    print(e)

    def _load_database(self, database: Database):
        self._database = database
        self._reload_database()

    def _enable_lower_buttons(self):
        self._ui.delete_button.setEnabled(True)
        self._ui.account_info_button.setEnabled(True)

    def _reload_database(self):
        while self._ui.account_list.rowCount() > 0:
            self._ui.account_list.removeRow(0)
        self._accounts_data = AccountData.load_all(self._database)
        for data in self._accounts_data:
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
            str(data.account_type),
        ]
        for id, value in enumerate(row_entry):
            self._ui.account_list.setItem(new_row, id, QTableWidgetItem(value))
