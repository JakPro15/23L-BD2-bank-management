from typing import Optional

from PySide6.QtWidgets import QDialog, QTableWidgetItem, QWidget

from src.database.database import Database
from src.database.table_types import AccountData, CompanyData
from src.helpers import set_optional_str
from src.ui.generated.dialogs.company_info_dialog import Ui_CompanyInfoDialog


class CompanyInfoDialog(QDialog):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_CompanyInfoDialog()
        self._ui.setupUi(self)

    def load_database(self, database: Database):
        self._database = database

    def load_company_info(self, company: CompanyData):
        self._ui.client_id_value.setText(str(company.client_id))
        self._ui.address_value.setText(str(company.address))
        self._ui.email_value.setText(company.email)
        self._ui.phone_number_value.setText(company.phone_nr)
        self._ui.name_value.setText(company.name)
        self._ui.nip_value.setText(company.NIP)

        self._reset_table()
        accounts = company.accounts(self._database)
        for acc in accounts:
            self._insert_data(acc)

    def _reset_table(self):
        while self._ui.accounts_table.rowCount() > 0:
            self._ui.accounts_table.removeRow(0)

    def _insert_data(self, account: AccountData):
        new_row = self._ui.accounts_table.rowCount()
        self._ui.accounts_table.insertRow(new_row)
        row_entry = [
            str(account.account_nr),
            str(account.creation_date.toPython()),
            str(
                account.closing_date.toPython()
                if account.closing_date is not None
                else "N/A"
            ),
            set_optional_str(account.transaction_limit),
            str(account.account_type),
        ]
        for id, value in enumerate(row_entry):
            self._ui.accounts_table.setItem(
                new_row, id, QTableWidgetItem(value)
            )
