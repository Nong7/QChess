from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QLabel
from .Piece import Piece


class Blank(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/blank")
        self.name = "blank"
