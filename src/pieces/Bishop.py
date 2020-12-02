from PyQt5.QtGui import QPixmap

from .Piece import Piece
from .Blank import Blank


# Creation of the class Bishop from where the classes BBishop and WBishop will inherit
# This class inherits at the same time from the class Piece
class Bishop(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)

    def possible_movements(self):
        # Creation of a list where the possible positions will be stored
        positions = []
        i = 1

        # The while loops check all the positions of the diagonals and append to the list the ones
        # that don't go off the board and are blank squares
        # All the ifs check if the last position appended of the diagonal is an enemy piece,
        # in this case this position is appended to the list since it can be eaten
        while (self.coords[0] - i) >= 0 and (self.coords[1] - i) >= 0 \
                and isinstance(self.game.pieces[self.coords[0] - i][self.coords[1] - i], Blank):
            positions.append((self.coords[0] - i, self.coords[1] - i))
            i += 1
        if (self.coords[0] - i) >= 0 and (self.coords[1] - i) >= 0 \
                and self.game.pieces[self.coords[0] - i][self.coords[1] - i].color != self.color:
            positions.append((self.coords[0] - i, self.coords[1] - i))

        i = 1
        while (self.coords[0] + i) <= 7 and (self.coords[1] - i) >= 0 \
                and isinstance(self.game.pieces[self.coords[0] + i][self.coords[1] - i], Blank):
            positions.append((self.coords[0] + i, self.coords[1] - i))
            i += 1
        if (self.coords[0] + i) <= 7 and (self.coords[1] - i) >= 0 \
                and self.game.pieces[self.coords[0] + i][self.coords[1] - i].color != self.color:
            positions.append((self.coords[0] + i, self.coords[1] - i))

        i = 1
        while (self.coords[0] - i) >= 0 and (self.coords[1] + i) <= 7 \
                and isinstance(self.game.pieces[self.coords[0] - i][self.coords[1] + i], Blank):
            positions.append((self.coords[0] - i, self.coords[1] + i))
            i += 1
        if (self.coords[0] - i) >= 0 and (self.coords[1] + i) <= 7 \
                and self.game.pieces[self.coords[0] - i][self.coords[1] + i].color != self.color:
            positions.append((self.coords[0] - i, self.coords[1] + i))

        i = 1
        while (self.coords[0] + i) <= 7 and (self.coords[1] + i) <= 7 \
                and isinstance(self.game.pieces[self.coords[0] + i][self.coords[1] + i], Blank):
            positions.append((self.coords[0] + i, self.coords[1] + i))
            i += 1
        if (self.coords[0] + i) <= 7 and (self.coords[1] + i) <= 7 \
                and self.game.pieces[self.coords[0] + i][self.coords[1] + i].color != self.color:
            positions.append((self.coords[0] + i, self.coords[1] + i))

        return positions


# Creation of the class WBishop (the parameters that change are the image, the name and the color)
class WBishop(Bishop):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/wB")
        self.name = "wB"
        self.color = "w"


# Creation of the class BBishop (the parameters that change are the same than WBishop)
class BBishop(Bishop):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/bB")
        self.name = "bB"
        self.color = "b"
