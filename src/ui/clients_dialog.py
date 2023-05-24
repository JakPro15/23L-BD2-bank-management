from typing import Optional

from PySide6.QtWidgets import QDialog, QWidget

from src.ui.generated.dialogs.client_dialog import Ui_ClientDialog


class ClientsDialog(QDialog):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_ClientDialog()
        self._ui.setupUi(self)
