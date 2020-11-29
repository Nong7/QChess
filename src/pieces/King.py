from PyQt5.QtGui import QPixmap

from .Piece import Piece


class WKing(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/wK")
        self.name = "wK"
        self.color = "w"

    def possible_movements(self):
        return [(1, 1)]


class BKing(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/bK")
        self.name = "bK"
        self.color = "b"

    def possible_movements(self):
        return [(1, 1)]
