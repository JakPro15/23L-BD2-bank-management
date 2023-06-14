from typing import Optional

from PySide6.QtWidgets import QDialog, QWidget

from src.database.database import Database
from src.database.database_errors import DatabaseTransactionError
from src.database.table_types import AddressData
from src.ui.generated.dialogs.address_dialog import Ui_AddressDialog


class AddressesDialog(QDialog):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_AddressDialog()
        self._ui.setupUi(self)
        self._ui.create_button.clicked.connect(self._try_create_address)

    def _try_create_address(self):
        new_address = AddressData(
            None,
            self._ui.country_line_edit.text(),
            self._ui.city_line_edit.text(),
            self._ui.postcode_line_edit.text(),
            self._ui.street_line_edit.text(),
            self._ui.house_line_edit.text(),
            self._ui.apartment_line_edit.text(),
        )
        try:
            self._database.add_address(new_address)
            self.done(1)
        except DatabaseTransactionError as e:
            print(e)

    def _load_database(self, database: Database):
        self._database = database
