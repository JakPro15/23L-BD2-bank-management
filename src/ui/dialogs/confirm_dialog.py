from typing import Optional

from PySide6.QtWidgets import QMessageBox, QWidget


class ConfirmDialog(QMessageBox):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setText("Are you sure?")
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.setDefaultButton(QMessageBox.Cancel)
