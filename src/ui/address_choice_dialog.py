from typing import Optional

from PySide6.QtWidgets import QDialog, QWidget

from src.ui.addresses_dialog import AddressesDialog
from src.ui.generated.dialogs.address_choice_dialog import (
    Ui_AddressChoiceDialog,
)


class AddressChoiceDialog(QDialog):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_AddressChoiceDialog()
        self._ui.setupUi(self)
        self._address_dialog = AddressesDialog(self)
        self._ui.add_button.clicked.connect(self._try_add_address)

    def _try_add_address(self):
        result = self._address_dialog.exec()
        if result:
            pass

    def _load_database(self):
        pass
