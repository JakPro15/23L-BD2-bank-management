import sys
from typing import Optional

from PySide6.QtWidgets import QWidget

from src.ui.generated.menu_widget import Ui_MenuWidget


class MenuWidget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_MenuWidget()
        self._ui.setupUi(self)
        self._ui.quit_button.clicked.connect(lambda: sys.exit(0))
        self.accounts_button_clicked = self._ui.accounts_button.clicked
