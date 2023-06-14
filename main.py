import sys
import os

from PySide6.QtWidgets import QApplication  # noqa: E402

from src.database.database import Database  # noqa: E402
from src.ui.main_window import MainWindow  # noqa: E402

if __name__ == "__main__":
    os.system("./mysql.sh start && sleep 2")
    app = QApplication(sys.argv)
    database = Database()
    window = MainWindow()
    window.load_database(database)
    window.show()
    sys.exit(app.exec())
