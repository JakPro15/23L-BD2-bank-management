from typing import Optional

from PySide6.QtWidgets import QDialog, QWidget

from src.ui.generated.dialogs.address_dialog import Ui_AddressDialog


class AddressesDialog(QDialog):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_AddressDialog()
        self._ui.setupUi(self)
        self._ui.create_button.clicked.connect(self._try_create_address)

    def _try_create_address(self):
        self.done(1)
