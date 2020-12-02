from src.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon("img/logo.png"))
    window = MainWindow(app)
    app.exec()
