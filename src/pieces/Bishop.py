from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QLabel
from .Piece import Piece
from .Blank import Blank


class WBishop(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y, "w")
        self.image = QPixmap("./img/wB")
        self.name = "wB"

    def possible_movements(self):
        return [(1, 1)]


class BBishop(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y, "b")
        self.image = QPixmap("./img/bB")
        self.name = "bB"

    def possible_movements(self):
        return [(1, 1)]