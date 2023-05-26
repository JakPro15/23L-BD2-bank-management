from typing import Optional

from PySide6.QtWidgets import QDialog, QWidget

from src.ui.dialogs.address_choice_dialog import AddressChoiceDialog
from src.ui.generated.dialogs.client_dialog import Ui_ClientDialog


class ClientsDialog(QDialog):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_ClientDialog()
        self._ui.setupUi(self)
        self._address_choice_dialog = AddressChoiceDialog(self)
        self._ui.create_button.clicked.connect(self._try_create_client)
        self._ui.address_button.clicked.connect(self._try_choose_address)

    def _try_create_client(self):
        self.done(1)

    def _try_choose_address(self):
        result = self._address_choice_dialog.exec()
        if result:
            pass
