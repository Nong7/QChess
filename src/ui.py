from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMenu, \
                            QMenuBar, QAction, QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from .game_widget import GameWidget


class MainWindow(QMainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)

        self.app = app
        self.setWindowTitle("QChess")
        self.setMinimumSize(400, 400)
        w = QWidget()

        # Main layout
        self.main_layout = QVBoxLayout()
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
        self.aspect_menu = self.menu_bar.addMenu("Aspect")
        self.change_color = self.aspect_menu.addMenu("Change Color")

        # Configuration action
        self.exit_action = QAction("Exit App", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.triggered.connect(lambda: QApplication.quit())
        self.configuration_menu.addAction(self.exit_action)

        self.manual = QAction("Game Manual", self)
        self.configuration_menu.addAction(self.manual)

        # Change Color Action
        self.classic_color = QtWidgets.QAction("Classic")
        self.change_color.addAction(self.classic_color)

        self.brown_color = QtWidgets.QAction("Brown")
        self.change_color.addAction(self.brown_color)

        self.show()

    def update_turn_label(self, text: str):
        self.turn_label.setText(text)
