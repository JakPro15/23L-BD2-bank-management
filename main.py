import sys

from PySide6.QtWidgets import QApplication

from src.database.database import Database
from src.ui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    database = Database()
    window = MainWindow()
    window.load_database(database)
    window.show()
    sys.exit(app.exec())
