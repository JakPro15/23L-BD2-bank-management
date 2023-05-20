from typing import Optional

from PySide6.QtWidgets import QMainWindow, QWidget

from src.ui.accounts_widget import AccountsWidget
from src.ui.generated.main_window import Ui_MainWindow
from src.ui.menu_widget import MenuWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._menu_widget = MenuWidget(self)
        self._accounts_widget = AccountsWidget(self)
        self._ui.main_stack.addWidget(self._menu_widget)
        self._ui.main_stack.addWidget(self._accounts_widget)
        self._accounts_widget.menu_button_clicked.connect(
            lambda: self._ui.main_stack.setCurrentWidget(self._menu_widget)
        )
        self._menu_widget.accounts_button_clicked.connect(
            lambda: self._ui.main_stack.setCurrentWidget(self._accounts_widget)
        )
        self._ui.main_stack.setCurrentWidget(self._menu_widget)
