from PyQt5.QtGui import QPixmap

from .Piece import Piece


class WBishop(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/wB")
        self.name = "wB"
        self.color = "w"

    def possible_movements(self):
        return [(1, 1)]


class BBishop(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/bB")
        self.name = "bB"
        self.color = "b"

    def possible_movements(self):
        return [(1, 1)]
