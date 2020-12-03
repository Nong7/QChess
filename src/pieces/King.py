from PyQt5.QtGui import QPixmap

from .Piece import Piece
from .Queen import Queen


# Creation of the class King from where the classes BKing and WKing will inherit
# This class inherits at the same time from the class Queen
class King(Queen):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)

    def possible_movements(self):
        # Creation of a list to append all the possible positions
        positions = []

        # The king has the same possible directions than the queen so to obtain all his possible movements
        # all we have to do is append the positions that don't move more than one square from the king
        queen_positions = Queen.possible_movements(self)

        for position in queen_positions:
            if (self.coords[0] - 1 <= position[0] <= self.coords[0] + 1) \
                    and (self.coords[1] - 1 <= position[1] <= self.coords[1] + 1):
                positions.append(position)

        return positions


# Creation of the class WKing (the parameters that change are the image, the name and the color)
class WKing(King):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/wK")
        self.name = "wK"
        self.color = "w"


# Creation of the class BKing (the parameters that change are the same than WKing)
class BKing(King):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/bK")
        self.name = "bK"
        self.color = "b"
