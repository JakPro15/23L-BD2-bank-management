from typing import Optional

from PySide6.QtWidgets import QDialog, QWidget

from src.database.database import Database
from src.database.database_errors import DatabaseTransactionError
from src.database.table_types import AccountData, AccountTypeData
from src.ui.generated.dialogs.account_dialog import Ui_AccountDialog


class AccountDialog(QDialog):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_AccountDialog()
        self._ui.setupUi(self)
        self._ui.create_button.clicked.connect(self._try_create_account)

    def load_database(self, database: Database):
        self._database = database

    def _try_create_account(self):
        try:
            new_type = AccountTypeData(
                self._ui.type_name_edit.text(),
                int(self._ui.type_version_edit.text()),
            )
            transaction_limit = self._ui.transaction_limit_edit.text()
            if not transaction_limit:
                transaction_limit = None
            else:
                transaction_limit = float(transaction_limit)
            new_account = AccountData(
                None,
                self._ui.account_number_edit.text(),
                self._ui.creation_date_edit.date(),
                self._ui.closing_date_edit.date()
                if self._ui.closing_date_check.isChecked()
                else None,
                transaction_limit,
                new_type,
            )
            new_account.insert(self._database)
            self.done(1)

        except DatabaseTransactionError as e:
            print(e)
