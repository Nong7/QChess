from PyQt5.QtGui import QPixmap

from .Piece import Piece


class WKnight(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/wN")
        self.name = "wN"
        self.color = "w"

    def possible_movements(self):
        return [(1, 1)]


class BKnight(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/bN")
        self.name = "bN"
        self.color = "b"

    def possible_movements(self):
        return [(1, 1)]
