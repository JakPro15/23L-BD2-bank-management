from PySide6.QtWidgets import QMainWindow

from src.ui.generated.main_window import Ui_MainWindow
from src.ui.menu_widget import MenuWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        new = MenuWidget()
        self._ui.main_stack.addWidget(new)
        self._ui.main_stack.setCurrentWidget(new)
