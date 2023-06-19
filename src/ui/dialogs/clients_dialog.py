from typing import Optional

from PySide6.QtWidgets import QDialog, QWidget

from src.database.database import Database
from src.database.database_errors import DatabaseTransactionError
from src.database.table_types import AddressData, CompanyData, PersonData
from src.ui.generated.dialogs.client_dialog import Ui_ClientDialog


class ClientsDialog(QDialog):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._database = None
        self._ui = Ui_ClientDialog()
        self._ui.setupUi(self)
        self._ui.create_button.clicked.connect(self._try_create_client)

    def _try_create_client(self):
        try:
            new_address = AddressData(
                self._ui.country_line_edit.text(),
                self._ui.city_line_edit.text(),
                self._ui.postcode_line_edit.text(),
                self._ui.street_line_edit.text(),
                self._ui.apartment_line_edit.text(),
            )
            if self._ui.selector_combo_box.currentIndex():
                new_client = CompanyData(
                    None,
                    new_address,
                    self._ui.email_line_edit.text(),
                    self._ui.phone_line_edit.text(),
                    self._ui.company_name_line_edit.text(),
                    self._ui.company_nip_line_edit.text(),
                )
            else:
                new_client = PersonData(
                    None,
                    new_address,
                    self._ui.email_line_edit.text(),
                    self._ui.phone_line_edit.text(),
                    self._ui.person_name_line_edit.text(),
                    self._ui.person_surname_line_edit.text(),
                    self._ui.person_pesel_line_edit.text(),
                    self._ui.person_sex_combo_box.currentText(),
                )

            if self._database:
                new_client.insert(self._database)
                self.done(1)

            else:
                raise DatabaseTransactionError(
                    "Database not loaded by dialog."
                )

        except DatabaseTransactionError as e:
            print(e)

    def _load_database(self, database: Database):
        self._database = database
