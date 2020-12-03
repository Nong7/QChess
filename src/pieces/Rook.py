from PyQt5.QtGui import QPixmap

from .Piece import Piece
from .Blank import Blank
import operator


# Creation of the class Rook from where the classes BRook and WRook will inherit
# This class inherits at the same time from the class Piece
class Rook(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)

    def possible_movements(self):
        # Creation of a list to append all the possible positions
        positions = []
        # Creation of a list with all the comparisons and operations that are going to be needed to check
        # the four possible set of positions (usage of the operator library)
        operators = [[operator.sub, operator.ge, 0, 1, 0], [operator.add, operator.le, 7, 1, 0], \
                     [operator.sub, operator.ge, 0, 0, 1], [operator.add, operator.le, 7, 0, 1]]

        # The while loop checks all the positions of the columns and rows containing the rook and append
        # to the list the ones that don't go off the board and are blank squares
        # All the ifs check if the last position appended of the while is an enemy piece,
        # in this case this position is appended to the list since it can be eaten
        for j in range(len(operators)):
            i = 1
            while (operators[j][1](operators[j][0](self.coords[operators[j][4]], i), operators[j][2])) and \
                    isinstance(self.game.pieces[operators[j][0](self.coords[0], i * operators[j][3])][operators[j][0](self.coords[1], i * operators[j][4])], Blank):
                positions.append((operators[j][0](self.coords[0], i * operators[j][3]), operators[j][0](self.coords[1], i * operators[j][4])))
                i += 1

            if (operators[j][1](operators[j][0](self.coords[operators[j][4]], i), operators[j][2])) and \
                    self.game.pieces[operators[j][0](self.coords[0], i * operators[j][3])][operators[j][0](self.coords[1], i * operators[j][4])].color != self.color:
                positions.append((operators[j][0](self.coords[0], i * operators[j][3]), operators[j][0](self.coords[1], i * operators[j][4])))

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
