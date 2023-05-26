from typing import Optional

from PySide6.QtWidgets import QMainWindow, QWidget

from src.database.database import Database
from src.ui.accounts_widget import AccountsWidget
from src.ui.addresses_widget import AddressesWidget
from src.ui.clients_widget import ClientsWidget
from src.ui.generated.main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._initialize_widgets()
        self._add_tabs()
        self._ui.main_tabs.setTabOrder
        self._ui.main_tabs.setCurrentWidget(self._accounts_widget)

    def _initialize_widgets(self):
        self._accounts_widget = AccountsWidget(self._ui.main_tabs)
        self._addresses_widget = AddressesWidget(self._ui.main_tabs)
        self._clients_widget = ClientsWidget(self._ui.main_tabs)

    def _add_tabs(self):
        self._ui.main_tabs.addTab(self._accounts_widget, "Accounts")
        self._ui.main_tabs.addTab(self._addresses_widget, "Addresses")
        self._ui.main_tabs.addTab(self._clients_widget, "Clients")

    def load_database(self, database: Database):
        self._clients_widget._load_database(database)
        self._addresses_widget._load_database(database)
