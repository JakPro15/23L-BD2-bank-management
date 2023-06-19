from typing import Optional

from PySide6.QtWidgets import QTableWidgetItem, QWidget

from src.database.database import Database
from src.database.table_types import CompanyData, PersonData
from src.helpers import set_optional_str
from src.ui.dialogs.clients_dialog import ClientsDialog
from src.ui.generated.clients_widget import Ui_ClientsWidget


class ClientsWidget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_ClientsWidget()
        self._ui.setupUi(self)
        self._client_dialog = ClientsDialog(self)
        self._ui.add_account_button.clicked.connect(self._add_client_procedure)

    def _add_client_procedure(self):
        result = self._client_dialog.exec()
        if result:
            pass

    def _load_database(self, database: Database):
        people_data = PersonData.load_all(database)
        companies_data = CompanyData.load_all(database)
        for data in people_data:
            self.insert_person_data(data)
        for data in companies_data:
            self.insert_company_data(data)

    def insert_person_data(self, data: PersonData):
        new_row = self._ui.people_table.rowCount()
        self._ui.people_table.insertRow(new_row)
        row_entry = [
            str(data.client_id),
            str(data.address),
            set_optional_str(data.email),
            set_optional_str(data.phone_nr),
            data.first_name,
            data.last_name,
            data.PESEL,
            data.sex,
        ]
        for id, value in enumerate(row_entry):
            self._ui.people_table.setItem(new_row, id, QTableWidgetItem(value))

    def insert_company_data(self, data: CompanyData):
        new_row = self._ui.companies_table.rowCount()
        self._ui.companies_table.insertRow(new_row)
        row_entry = [
            str(data.id),
            str(data.address),
            set_optional_str(data.email),
            set_optional_str(data.phone_nr),
            data.name,
            data.NIP,
        ]
        for id, value in enumerate(row_entry):
            self._ui.companies_table.setItem(
                new_row, id, QTableWidgetItem(value)
            )
