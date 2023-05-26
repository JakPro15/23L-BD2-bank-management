from typing import Optional

from PySide6.QtWidgets import QDialog, QWidget

from src.ui.generated.dialogs.address_dialog import Ui_AddressDialog


class AddressesDialog(QDialog):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_AddressDialog()
        self._ui.setupUi(self)
