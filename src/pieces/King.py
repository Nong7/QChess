from PyQt5.QtGui import QPixmap

from .Piece import Piece
from .Blank import Blank


# Creation of the class King from where the classes BKing and WKing will inherit
# This class inherits at the same time from the class Piece
class King(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)

    def possible_movements(self):
        # Creation of a list to append all the possible positions
        positions = []
        i = 1

        # The if statements check all the squares that surround the king to see if they go off the
        # board and if they are a blank space, if those two conditions are correct the position is appended
        # In the case that the first condition isn't met if the squares that surround
        # the king are enemy pieces its position is appended
        if (self.coords[0] - i) >= 0 and (self.coords[1] - i) >= 0 \
                and (isinstance(self.game.pieces[self.coords[0] - i][self.coords[1] - i], Blank) \
                     or self.game.pieces[self.coords[0] - i][self.coords[1] - i].color != self.color):
            positions.append((self.coords[0] - i, self.coords[1] - i))

        if (self.coords[0] + i) <= 7 and (self.coords[1] - i) >= 0 \
                and (isinstance(self.game.pieces[self.coords[0] + i][self.coords[1] - i], Blank) \
                     or self.game.pieces[self.coords[0] + i][self.coords[1] - i].color != self.color):
            positions.append((self.coords[0] + i, self.coords[1] - i))

        if (self.coords[0] - i) >= 0 and (self.coords[1] + i) <= 7 \
                and (isinstance(self.game.pieces[self.coords[0] - i][self.coords[1] + i], Blank) \
                     or self.game.pieces[self.coords[0] - i][self.coords[1] + i].color != self.color):
            positions.append((self.coords[0] - i, self.coords[1] + i))

        if (self.coords[0] + i) <= 7 and (self.coords[1] + i) <= 7 \
                and (isinstance(self.game.pieces[self.coords[0] + i][self.coords[1] + i], Blank) \
                     or self.game.pieces[self.coords[0] + i][self.coords[1] + i].color != self.color):
            positions.append((self.coords[0] + i, self.coords[1] + i))

        if (self.coords[0] - i) >= 0 and (isinstance(self.game.pieces[self.coords[0] - i][self.coords[1]], Blank) \
                                          or self.game.pieces[self.coords[0] - i][self.coords[1]].color != self.color):
            positions.append((self.coords[0] - i, self.coords[1]))

        if (self.coords[0] + i) <= 7 and (isinstance(self.game.pieces[self.coords[0] + i][self.coords[1]], Blank) \
                                          or self.game.pieces[self.coords[0] + i][self.coords[1]].color != self.color):
            positions.append((self.coords[0] + i, self.coords[1]))

        if (self.coords[1] - i) >= 0 and (isinstance(self.game.pieces[self.coords[0]][self.coords[1] - i], Blank) \
                                          or self.game.pieces[self.coords[0]][self.coords[1] - i].color != self.color):
            positions.append((self.coords[0], self.coords[1] - i))

        if (self.coords[1] + i) <= 7 and (isinstance(self.game.pieces[self.coords[0]][self.coords[1] + i], Blank) \
                                          or self.game.pieces[self.coords[0]][self.coords[1] + i].color != self.color):
            positions.append((self.coords[0], self.coords[1] + i))

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
        
