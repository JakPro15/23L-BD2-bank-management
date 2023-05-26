from typing import Optional

from PySide6.QtWidgets import QWidget

from src.ui.addresses_dialog import AddressesDialog

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
            pass
