from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QLabel
from .Piece import Piece
from .Blank import Blank


class WRook(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y, "w")
        self.image = QPixmap("./img/wR")
        self.name = "wR"

    def possible_movements(self):
        position = self.coords
        movements = [(1, 1)]

        return movements


class BRook(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y, "b")
        self.image = QPixmap("./img/bR")
        self.name = "bR"

    def possible_movements(self):
        position = self.coords
        movements = [(1, 1)]

        return movements
