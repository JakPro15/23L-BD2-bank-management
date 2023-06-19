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
        self._ui.people_table.currentCellChanged.connect(
            self._enable_lower_buttons
        )
        self._ui.account_info_button.clicked.connect(self._show_info_dialog)

    def _enable_lower_buttons(self):
        self._ui.account_info_button.setEnabled(True)
        self._ui.delete_button.setEnabled(True)

    def _disable_lower_buttons(self):
        self._ui.account_info_button.setEnabled(False)
        self._ui.delete_button.setEnabled(False)

    def _show_info_dialog(self):
        idx = self._ui.people_table.currentRow()

        if self._ui.table_stack.currentIndex():
            data = self._companies_data[idx]
        else:
            data = self._people_data[idx]
        print(data)

    def _add_client_procedure(self):
        self._client_dialog._load_database(self._database)
        result = self._client_dialog.exec()
        if result:
            self._reload_database()

    def _load_database(self, database: Database):
        self._database = database
        self._reload_database()

    def _reload_database(self):
        while self._ui.people_table.rowCount() > 0:
            self._ui.people_table.removeRow(0)
        while self._ui.companies_table.rowCount() > 0:
            self._ui.companies_table.removeRow(0)

        self._people_data = PersonData.load_all(self._database)
        self._companies_data = CompanyData.load_all(self._database)

        for data in self._people_data:
            self.insert_person_data(data)
        for data in self._companies_data:
            self.insert_company_data(data)

    def insert_person_data(self, data: PersonData):
        new_row = self._ui.people_table.rowCount()
        self._ui.people_table.insertRow(new_row)
        row_entry = [
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
