from typing import Optional

from PySide6.QtWidgets import QWidget

from src.ui.clients_dialog import ClientsDialog
from src.ui.generated.clients_widget import Ui_ClientsWidget


class ClientsWidget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_ClientsWidget()
        self._ui.setupUi(self)
        self._client_dialog = ClientsDialog(self)
        self._ui.add_account_button.clicked.connect(self._add_client_procedure)

    def _add_client_procedure(self):
        result = self._client_dialog.exec()
        if result:
            pass

    # def insert_data(
    #     self,
    #     account_number: int,
    #     creation_date: dt.date,
    #     expiration_date: dt.date,
    #     transaction_limit: int,
    # ):
    #     pass
    # new_row = self._ui.account_list.rowCount()
    # self._ui.account_list.insertRow(new_row)
    # self._ui.account_list.setItem(
    #     new_row, 0, QTableWidgetItem(str(account_number))
    # )
    # self._ui.account_list.setItem(
    #     new_row, 1, QTableWidgetItem(creation_date.isoformat())
    # )
    # self._ui.account_list.setItem(
    #     new_row, 2, QTableWidgetItem(expiration_date.isoformat())
    # )
    # self._ui.account_list.setItem(
    #     new_row, 3, QTableWidgetItem(str(transaction_limit))
    # )
