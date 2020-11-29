from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QLabel
from .Piece import Piece
from .Blank import Blank


class WKing(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y, "w")
        self.image = QPixmap("./img/wK")
        self.name = "wK"

    def possible_movements(self):
        return [(1, 1)]


class BKing(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y, "b")
        self.image = QPixmap("./img/bK")
        self.name = "bK"

    def possible_movements(self):
        return [(1, 1)]
