from typing import Optional

from PySide6.QtWidgets import QMainWindow, QWidget

from src.ui.accounts_widget import AccountsWidget
from src.ui.clients_widget import ClientsWidget
from src.ui.generated.main_window import Ui_MainWindow
from src.ui.menu_widget import MenuWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._initialize_widgets()
        self._add_widgets_to_stack()
        self._connect_widget_buttons()
        self._ui.main_stack.setCurrentWidget(self._menu_widget)

    def _initialize_widgets(self):
        self._menu_widget = MenuWidget(self._ui.main_stack)
        self._accounts_widget = AccountsWidget(self._ui.main_stack)
        self._clients_widget = ClientsWidget(self._ui.main_stack)

    def _add_widgets_to_stack(self):
        self._ui.main_stack.addWidget(self._menu_widget)
        self._ui.main_stack.addWidget(self._accounts_widget)
        self._ui.main_stack.addWidget(self._clients_widget)

    def _connect_widget_buttons(self):
        self._accounts_widget.menu_button_clicked.connect(
            lambda: self._ui.main_stack.setCurrentWidget(self._menu_widget)
        )
        self._menu_widget.accounts_button_clicked.connect(
            lambda: self._ui.main_stack.setCurrentWidget(self._accounts_widget)
        )
        self._clients_widget.menu_button_clicked.connect(
            lambda: self._ui.main_stack.setCurrentWidget(self._menu_widget)
        )
        self._menu_widget.clients_button_clicked.connect(
            lambda: self._ui.main_stack.setCurrentWidget(self._clients_widget)
        )
