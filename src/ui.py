from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMenu, \
                            QMenuBar
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

        self.show()

    def update_turn_label(self, text: str):
        self.turn_label.setText(text)
