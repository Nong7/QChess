from PyQt5.QtGui import QPixmap

from .Piece import Piece
from .Blank import Blank


# Creation of the class Knight from where the classes BKnight and WKnight will inherit
# This class inherits at the same time from the class Piece
class Knight(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)

    def possible_movements(self):
        # Creation of a list to append all the possible positions
        positions = []

        # The if statements check all the possible positions a knight can cover
        # If the position checked is in the board and is a blank square the position is appended
        # If the position checked is in the board and is an enemy piece the position is appended as well
        if (self.coords[0] - 2) >= 0 and (self.coords[1] - 1) >= 0 \
                and (self.game.pieces[self.coords[0] - 2][self.coords[1] - 1].color != self.color or
                     isinstance(self.game.pieces[self.coords[0] - 2][self.coords[1] - 1], Blank)):
            positions.append((self.coords[0] - 2, self.coords[1] - 1))

        if (self.coords[0] - 2) >= 0 and (self.coords[1] + 1) <= 7 \
                and (self.game.pieces[self.coords[0] - 2][self.coords[1] + 1].color != self.color or
                     isinstance(self.game.pieces[self.coords[0] - 2][self.coords[1] + 1], Blank)):
            positions.append((self.coords[0] - 2, self.coords[1] + 1))

        if (self.coords[0] - 1) >= 0 and (self.coords[1] - 2) >= 0 \
                and (self.game.pieces[self.coords[0] - 1][self.coords[1] - 2].color != self.color or
                     isinstance(self.game.pieces[self.coords[0] - 1][self.coords[1] - 2], Blank)):
            positions.append((self.coords[0] - 1, self.coords[1] - 2))

        if (self.coords[0] - 1) >= 0 and (self.coords[1] + 2) <= 7 \
                and (self.game.pieces[self.coords[0] - 1][self.coords[1] + 2].color != self.color or
                     isinstance(self.game.pieces[self.coords[0] - 1][self.coords[1] + 2], Blank)):
            positions.append((self.coords[0] - 1, self.coords[1] + 2))

        if (self.coords[0] + 2) <= 7 and (self.coords[1] + 1) <= 7 \
                and (self.game.pieces[self.coords[0] + 2][self.coords[1] + 1].color != self.color or
                     isinstance(self.game.pieces[self.coords[0] + 2][self.coords[1] + 1], Blank)):
            positions.append((self.coords[0] + 2, self.coords[1] + 1))

        if (self.coords[0] + 2) <= 7 and (self.coords[1] - 1) >= 0 \
                and (self.game.pieces[self.coords[0] + 2][self.coords[1] - 1].color != self.color or
                     isinstance(self.game.pieces[self.coords[0] + 2][self.coords[1] - 1], Blank)):
            positions.append((self.coords[0] + 2, self.coords[1] - 1))

        if (self.coords[0] + 1) <= 7 and (self.coords[1] + 2) <= 7 \
                and (self.game.pieces[self.coords[0] + 1][self.coords[1] + 2].color != self.color or
                     isinstance(self.game.pieces[self.coords[0] + 1][self.coords[1] + 2], Blank)):
            positions.append((self.coords[0] + 1, self.coords[1] + 2))

        if (self.coords[0] + 1) <= 7 and (self.coords[1] - 2) >= 0 \
                and (self.game.pieces[self.coords[0] + 1][self.coords[1] - 2].color != self.color or
                     isinstance(self.game.pieces[self.coords[0] + 1][self.coords[1] - 2], Blank)):
            positions.append((self.coords[0] + 1, self.coords[1] - 2))

        return positions

# Creation of the class WKnight (the parameters that change are the image, the name and the color)
class WKnight(Knight):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/wN")
        self.name = "wN"
        self.color = "w"


# Creation of the class BKnight (the parameters that change are the same than WKnight)
class BKnight(Knight):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/bN")
        self.name = "bN"
        self.color = "b"
