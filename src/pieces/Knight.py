from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QLabel
from .Piece import Piece
from .Blank import Blank


class WKnight(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y, "w")
        self.image = QPixmap("./img/wN")
        self.name = "wN"

    def possible_movements(self):
        return [(1, 1)]


class BKnight(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y, "b")
        self.image = QPixmap("./img/bN")
        self.name = "bN"

    def possible_movements(self):
        return [(1, 1)]
