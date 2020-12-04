from PyQt5.QtGui import QPixmap

from .Rook import Rook
from .Bishop import Bishop


# Creation of the class Queen from where the classes BQueen and WQueen will inherit
# This class inherits at the same time from the classes Rook and Bishop
class Queen(Rook, Bishop):
    def __init__(self, game, x, y):
        Rook.__init__(self, game, x, y)

    def possible_movements(self):
        # The queen movements is a combination of the rook movements and the bishop movements so if we
        # sum all the possible positions from both pieces we obtain the possible positions for the queen
        positions = Rook.possible_movements(self) + Bishop.possible_movements(self)

        return positions


# Creation of the class WQueen (the parameters that change are the image, the name and the color)
class WQueen(Queen):
    def __init__(self, game, x, y):
        Queen.__init__(self, game, x, y)
        self.image = QPixmap("./img/wQ")
        self.name = "wQ"
        self.color = "w"


# Creation of the class BQueen (the parameters that change are the same than WQueen)
class BQueen(Queen):
    def __init__(self, game, x, y):
        Queen.__init__(self, game, x, y)
        self.image = QPixmap("./img/bQ")
        self.name = "bQ"
        self.color = "b"
