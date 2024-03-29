from typing import Optional

from PySide6.QtWidgets import QMessageBox, QTableWidgetItem, QWidget

from src.database.database import Database
from src.database.database_errors import DatabaseTransactionError
from src.database.table_types import ClientData, CompanyData, PersonData
from src.helpers import set_optional_str
from src.ui.dialogs.clients_dialog import ClientsDialog
from src.ui.dialogs.company_info_dialog import CompanyInfoDialog
from src.ui.dialogs.confirm_dialog import ConfirmDialog
from src.ui.dialogs.person_info_dialog import PersonInfoDialog
from src.ui.generated.clients_widget import Ui_ClientsWidget


class ClientsWidget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_ClientsWidget()
        self._ui.setupUi(self)
        self._client_dialog = ClientsDialog(self)
        self._person_info_dialog = PersonInfoDialog(self)
        self._company_info_dialog = CompanyInfoDialog(self)
        self._ui.add_account_button.clicked.connect(self._add_client_procedure)
        self._ui.people_table.currentCellChanged.connect(
            self._enable_lower_buttons
        )
        self._ui.companies_table.currentCellChanged.connect(
            self._enable_lower_buttons
        )
        self._ui.account_info_button.clicked.connect(self._show_info_dialog)
        self._ui.delete_button.clicked.connect(self._delete_procedure)

    def _delete_client(self, data: ClientData):
        data.delete(self._database)
        self._reload_database()

    def _delete_procedure(self):
        result = ConfirmDialog(self).exec()

        match result:
            case QMessageBox.Cancel:
                print("keep")
            case QMessageBox.Ok:
                data = self._current_client()
                try:
                    self._delete_client(data)
                    print("deleted")
                except DatabaseTransactionError as e:
                    print(e)

    def _current_client(self) -> ClientData:
        if self._ui.table_stack.currentIndex():
            idx = self._ui.companies_table.currentRow()
            return self._companies_data[idx]
        else:
            idx = self._ui.people_table.currentRow()
            return self._people_data[idx]

    def _enable_lower_buttons(self):
        self._ui.account_info_button.setEnabled(True)
        self._ui.delete_button.setEnabled(True)

    def _disable_lower_buttons(self):
        self._ui.account_info_button.setEnabled(False)
        self._ui.delete_button.setEnabled(False)

    def _show_info_dialog(self):
        data = self._current_client()
        if self._ui.account_type_combo.currentIndex():
            self._company_info_dialog.load_company_info(data)
            self._company_info_dialog.exec()
        else:
            self._person_info_dialog.load_person_info(data)
            self._person_info_dialog.exec()

    def _add_client_procedure(self):
        self._client_dialog._load_database(self._database)
        result = self._client_dialog.exec()
        if result:
            self._reload_database()

    def _load_database(self, database: Database):
        self._database = database
        self._person_info_dialog.load_database(self._database)
        self._company_info_dialog.load_database(self._database)
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
