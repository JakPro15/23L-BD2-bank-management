from typing import Optional

from PySide6.QtWidgets import QWidget

from src.ui.generated.accounts_widget import Ui_AccountsWidget


class AccountsWidget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_AccountsWidget()
        self._ui.setupUi(self)
        self.menu_button_clicked = self._ui.menu_button.clicked
