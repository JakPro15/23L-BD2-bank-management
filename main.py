import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from src.ui.main_window import Ui_MainWindow
from src.ui.menu_widget import Ui_MenuWidget


class MainMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._ui = Ui_MenuWidget()
        self._ui.setupUi(self)


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        new = MainMenu()
        self._ui.main_stack.addWidget(new)
        self._ui.main_stack.setCurrentWidget(new)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
