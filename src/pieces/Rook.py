from PyQt5.QtGui import QPixmap

from .Piece import Piece
from .Blank import Blank


# Creation of the class Rook from where the classes BRook and WRook will inherit
# This class inherits at the same time from the class Piece
class Rook(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)

    def possible_movements(self):
        # Creation of a list to append all the possible positions
        positions = []
        i = 1

        # The while loops check all the positions of the columns and rows containing the rook and append
        # to the list the ones that don't go off the board and are blank squares
        # All the ifs check if the last position appended of the while is an enemy piece,
        # in this case this position is appended to the list since it can be eaten
        while (self.coords[0] - i) >= 0 and isinstance(self.game.pieces[self.coords[0] - i][self.coords[1]], Blank):
            positions.append((self.coords[0] - i, self.coords[1]))
            i += 1
        if (self.coords[0] - i) >= 0 and self.game.pieces[self.coords[0] - i][self.coords[1]].color != self.color:
            positions.append((self.coords[0] - i, self.coords[1]))

        i = 1
        while (self.coords[0] + i) <= 7 and isinstance(self.game.pieces[self.coords[0] + i][self.coords[1]], Blank):
            positions.append((self.coords[0] + i, self.coords[1]))
            i += 1
        if (self.coords[0] + i) <= 7 and self.game.pieces[self.coords[0] + i][self.coords[1]].color != self.color:
            positions.append((self.coords[0] + i, self.coords[1]))

        i = 1
        while (self.coords[1] - i) >= 0 and isinstance(self.game.pieces[self.coords[0]][self.coords[1] - i], Blank):
            positions.append((self.coords[0], self.coords[1] - i))
            i += 1
        if (self.coords[1] - i) >= 0 and self.game.pieces[self.coords[0]][self.coords[1] - i].color != self.color:
            positions.append((self.coords[0], self.coords[1] - i))

        i = 1
        while (self.coords[1] + i) <= 7 and isinstance(self.game.pieces[self.coords[0]][self.coords[1] + i], Blank):
            positions.append((self.coords[0], self.coords[1] + i))
            i += 1
        if (self.coords[1] + i) <= 7 and self.game.pieces[self.coords[0]][self.coords[1] + i].color != self.color:
            positions.append((self.coords[0], self.coords[1] + i))

        return positions


# Creation of the class WRook (the parameters that change are the image, the name and the color)
class WRook(Rook):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/wR")
        self.name = "wR"
        self.color = "w"


# Creation of the class BRook (the parameters that change are the same than WRook)
class BRook(Rook):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/bR")
        self.name = "bR"
        self.color = "b"
