from PyQt5.QtGui import QPixmap

from .Piece import Piece


class WRook(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/wR")
        self.name = "wR"
        self.color = "w"

    def possible_movements(self):
        position = self.coords
        movements = [(1, 1)]

        return movements


class BRook(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/bR")
        self.name = "bR"
        self.color = "b"

    def possible_movements(self):
        position = self.coords
        movements = [(1, 1)]

        return movements
