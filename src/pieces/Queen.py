from PyQt5.QtGui import QPixmap

from .Piece import Piece


class WQueen(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/wQ")
        self.name = "wQ"
        self.color = "w"

    def possible_movements(self):
        return [(1, 1)]


class BQueen(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/bQ")
        self.name = "bQ"
        self.color = "b"

    def possible_movements(self):
        return [(1, 1)]
