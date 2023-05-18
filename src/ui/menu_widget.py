from PySide6.QtWidgets import QWidget

from src.ui.generated.menu_widget import Ui_MenuWidget


class MenuWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._ui = Ui_MenuWidget()
        self._ui.setupUi(self)
