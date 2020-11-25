from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QGridLayout, QSizePolicy
from PyQt5.QtGui import QFont, QPainter, QPen, QColor, QPixmap
from PyQt5.QtCore import Qt, QPoint, QLine


BOARD = [
    ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
    ['wR', 'wN', 'wB', 'wK', 'wQ', 'wB', 'wN', 'wR']
]


class Piece(QLabel):
    def __init__(self, game, name: str, x: int, y: int):
        QLabel.__init__(self)
        self.x, self.y = x, y
        self.game = game
        self.name = name
        self.color = "b" if self.name[0] == "b" else "w"
        self.is_selected = False
        self.setScaledContents(True)

    @property
    def image(self):
        return QPixmap(f'./img/{self.name}.png')

    def unselect(self):
        self.is_selected = False
        self.update()

    def mousePressEvent(self, event):
        QLabel.mousePressEvent(self, event)
        if self.game.turn == self.color:
            if self.name != "--":
                self.is_selected = True
                self.game.set_selected_piece(self)
                self.update()
            else:
                # Todo: move if possible
                pass

    def paintEvent(self, event):
        QLabel.paintEvent(self, event)
        x, y = self.width(), self.height()
        qp = QPainter(self)
        if (self.x + self.y) % 2 == 0:
            qp.fillRect(0, 0, x, y, QColor(200, 200, 200))
        if self.is_selected:
            qp.fillRect(0, 0, x, y, QColor(255, 240, 0))

        qp.drawPixmap(0, 0, x, y, self.image)


class GameWidget(QWidget):
    def __init__(self, window):
        QWidget.__init__(self)

        self.main_window = window

        # Main layout
        self.main_layout = QGridLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)
        self.board = BOARD
        self.pieces = [["" for _ in range(8)] for _ in range(8)]
        self.selected_piece = None
        font = QFont("Arial")
        font.setPointSize(10)
        self.setFont(font)
        self.set_up_pieces()
        self.turn = "w"

    def resizeEvent(self, event):
        QWidget.resizeEvent(self, event)
        # Keeps square aspect ratio
        if self.width() > self.height():
            self.resize(self.height(), self.height())
        else:
            self.resize(self.width(), self.width())

    def set_up_pieces(self):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                a = Piece(self, cell, i, j)
                self.pieces[i][j] = a
                self.main_layout.addWidget(a, i, j)

    def set_selected_piece(self, piece: Piece):
        if self.selected_piece:
            self.selected_piece.unselect()
        self.selected_piece = piece

    def change_turn(self):
        if self.turn == "b":
            self.turn = "w"
            self.main_window.update_turn_label("White's turn")
        else:
            self.turn = "b"
            self.main_window.update_turn_label("Black's turn")
