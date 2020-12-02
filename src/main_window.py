from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMenu, \
                            QMenuBar, QAction, QApplication
from PyQt5.QtGui import QFont, QDesktopServices
from PyQt5.QtCore import Qt, QUrl, QFileInfo
from .game_widget import GameWidget


class MainWindow(QMainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)

        self.app = app
        self.setWindowTitle("QChess")
        self.setMinimumSize(400, 450)
        w = QWidget()

        # Main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignHCenter)
        w.setLayout(self.main_layout)
        self.setCentralWidget(w)
        font = QFont("Arial")
        font.setPointSize(10)
        self.setFont(font)

        self.turn_label = QLabel("White's turn")
        self.turn_label.setAlignment(Qt.AlignCenter)
        self.turn_label.setMaximumHeight(15)
        self.main_layout.addWidget(self.turn_label)

        self.game_widget = GameWidget(self)
        self.main_layout.addWidget(self.game_widget)

        # Creation of the menu bar and insertion of the different actions that it has
        self.menu_bar = self.menuBar()

        self.configuration_menu = self.menu_bar.addMenu("Configuration")

        # Configuration action
        self.restart_action = QAction("Restart game", self)
        self.restart_action.triggered.connect(lambda: self.game_widget.reset_board())
        self.configuration_menu.addAction(self.restart_action)

        self.manual = QAction("Game Manual", self)
        self.configuration_menu.addAction(self.manual)

        self.guia = QUrl.fromLocalFile(QFileInfo("./src/guide.pdf").absoluteFilePath())
        self.manual.triggered.connect(lambda: QDesktopServices.openUrl(self.guia))

        self.exit_action = QAction("Exit App", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.triggered.connect(lambda: QApplication.quit())
        self.configuration_menu.addAction(self.exit_action)

        self.show()

    def update_turn_label(self, text: str):
        self.turn_label.setText(text)
