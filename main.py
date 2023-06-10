import sys

from PySide6.QtWidgets import QApplication

from src.database.database import Database
from src.ui.main_window import MainWindow

if __name__ == "__main__":
    # database = Database()
    # from src.database.datatypes import *
    # print(PersonData.load_all(database)[-1])
    # new = PersonData(None, AddressData(None, "polsza", "warsovia", "11-400", "Beans", "5A", None), "abc@gmail", "1234", "ja", "pro", "321", "M")
    # # new = AddressData(None, "polsza", "warsovia", "11-400", "Beans", "5A", None)
    # new.insert(database)
    # print(new.client_id)
    # print(PersonData.load_all(database)[-1])
    # sys.exit(0)
    app = QApplication(sys.argv)
    database = Database()
    window = MainWindow()
    window.load_database(database)
    window.show()
    sys.exit(app.exec())
