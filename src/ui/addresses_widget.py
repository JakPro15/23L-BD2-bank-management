from typing import Optional

from PySide6.QtWidgets import QTableWidgetItem, QWidget

from src.database.database import Database
from src.database.table_types import AddressData
from src.ui.dialogs.addresses_dialog import AddressesDialog

# from src.ui.addresses_dialog import AddressDialog
from src.ui.generated.addresses_widget import Ui_AddressesWidget


class AddressesWidget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_AddressesWidget()
        self._ui.setupUi(self)
        self._address_dialog = AddressesDialog(self)
        self._ui.add_address_button.clicked.connect(
            self._add_address_procedure
        )

    def _add_address_procedure(self):
        result = self._address_dialog.exec()
        if result:
            self.clear_data()
            self._load_database(self._database)

    def clear_data(self):
        while self._ui.addresses_list.rowCount() > 0:
            self._ui.addresses_list.removeRow(0)

    def insert_data(self, data: AddressData):
        new_row = self._ui.addresses_list.rowCount()
        self._ui.addresses_list.insertRow(new_row)
        row_entry = [
            str(0),
            data.country,
            data.city,
            data.post_code,
            data.street,
            data.house_nr,
            data.apartment_nr if data.apartment_nr is not None else "N/A",
        ]
        for id, value in enumerate(row_entry):
            self._ui.addresses_list.setItem(
                new_row, id, QTableWidgetItem(value)
            )

    def _load_database(self, database: Database):
        self._address_dialog._load_database(database)
        self._database = database
        addresses = AddressData.load_all(database)
        for address in addresses:
            self.insert_data(address)
