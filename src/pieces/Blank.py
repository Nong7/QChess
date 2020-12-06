from PyQt5.QtGui import QPixmap

from .Piece import Piece


class Blank(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./images/blank")
        self.name = "blank"
