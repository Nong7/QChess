from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QGridLayout, QSizePolicy
from PyQt5.QtGui import QFont, QPainter, QPen, QColor, QPixmap
from PyQt5.QtCore import Qt, QPoint, QLine
from pprint import pprint

BOARD = [
    ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
    ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
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

    def __repr__(self):
        return f"{self.name}"

    @property
    def image(self):
        return QPixmap(f'./img/{self.name}.png')

    def unselect(self):
        self.is_selected = False
        self.update()

    @property
    def coords(self):
        return self.x, self.y

    def mousePressEvent(self, event):
        QLabel.mousePressEvent(self, event)
        if self.game.turn == self.color:
            if self.name != "--":
                self.game.set_selected_piece(self)
                self.is_selected = True
                self.update()
            else:
                if self.game.selected_piece and self.game.selected_piece != self:
                    self.game.move_pieces(self.coords, self.game.selected_piece.coords)

    def paintEvent(self, event):
        QLabel.paintEvent(self, event)
        x, y = self.width(), self.height()
        qp = QPainter(self)
        if (self.x + self.y) % 2 == 1:
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
        self.pieces = BOARD
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
        for i, row in enumerate(self.pieces):
            for j, cell in enumerate(row):
                # cell: str
                piece = Piece(self, cell, i, j)
                self.pieces[i][j] = piece
                self.main_layout.addWidget(piece, i, j)

    def arrange_pieces(self):
        for i in range(8):
            for j in range(8):
                widget = self.main_layout.itemAtPosition(i, j).widget()
                self.main_layout.removeWidget(widget)
                widget.deleteLater()

        for i, row in enumerate(self.pieces):
            for j, cell in enumerate(row):
                # cell: str
                piece = Piece(self, cell.name, i, j)
                self.pieces[i][j] = piece
                self.main_layout.addWidget(piece, i, j)

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

    def move_pieces(self, coords1: tuple, coords2: tuple):
        self.pieces[coords1[0]][coords1[1]], self.pieces[coords2[0]][coords2[1]] = \
            self.pieces[coords2[0]][coords2[1]], self.pieces[coords1[0]][coords1[1]]

        self.arrange_pieces()
