from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QLabel
from .Piece import Piece
from .Blank import Blank


class WQueen(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y, "w")
        self.image = QPixmap("./img/wQ")
        self.name = "wQ"

    def possible_movements(self):
        return [(1, 1)]


class BQueen(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y, "b")
        self.image = QPixmap("./img/bQ")
        self.name = "bQ"

    def possible_movements(self):
        return [(1, 1)]
