from typing import Optional

from PySide6.QtWidgets import QDialog, QTableWidgetItem, QWidget

from src.database.database import Database
from src.database.table_types import AccountData, PersonData
from src.helpers import set_optional_str
from src.ui.generated.dialogs.person_info_dialog import Ui_PersonInfoDialog


class PersonInfoDialog(QDialog):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_PersonInfoDialog()
        self._ui.setupUi(self)

    def load_database(self, database: Database):
        self._database = database

    def load_person_info(self, person: PersonData):
        self._ui.client_id_value.setText(str(person.client_id))
        self._ui.address_value.setText(str(person.address))
        self._ui.email_value.setText(person.email)
        self._ui.phone_number_value.setText(person.phone_nr)
        self._ui.name_value.setText(person.first_name)
        self._ui.surname_value.setText(person.last_name)
        self._ui.pesel_value.setText(person.PESEL)
        self._ui.sex_value.setText(person.sex)

        self._reset_table()
        accounts = person.accounts(self._database)
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
