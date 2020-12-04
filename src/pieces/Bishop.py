from PyQt5.QtGui import QPixmap

from .Piece import Piece
from .Blank import Blank
import operator


# Creation of the class Bishop from where the classes BBishop and WBishop will inherit
# This class inherits at the same time from the class Piece
class Bishop(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)

    def possible_movements(self):
        # Creation of a list where the possible positions will be stored
        positions = []
        # Creation of a list with all the comparisons and operations that are going to be needed to check
        # the four possible set of positions (usage of the operator library)
        operators = [[operator.sub, operator.sub, operator.ge, operator.ge, 0, 0], \
                     [operator.add, operator.sub, operator.le, operator.ge, 7, 0], \
                     [operator.sub, operator.add, operator.ge, operator.le, 0, 7], \
                     [operator.add, operator.add, operator.le, operator.le, 7, 7]]

        # The while loop checks all the positions of the diagonals and append to the list the ones
        # that don't go off the board and are blank squares
        # All the ifs check if the last position appended of the diagonal is an enemy piece,
        # in this case this position is appended to the list since it can be eaten
        for j in range(len(operators)):
            i = 1
            while operators[j][2](operators[j][0](self.coords[0], i), operators[j][4]) and \
                    operators[j][3](operators[j][1](self.coords[1], i), operators[j][5]) \
                    and isinstance(self.game.pieces[operators[j][0](self.coords[0], i)][operators[j][1](self.coords[1], i)], Blank):
                positions.append((operators[j][0](self.coords[0], i), operators[j][1](self.coords[1], i)))
                i += 1

            if operators[j][2](operators[j][0](self.coords[0], i), operators[j][4]) and \
                    operators[j][3](operators[j][1](self.coords[1], i), operators[j][5]) \
                    and self.game.pieces[operators[j][0](self.coords[0], i)][operators[j][1](self.coords[1], i)].color != self.color:
                positions.append((operators[j][0](self.coords[0], i), operators[j][1](self.coords[1], i)))

        return positions


# Creation of the class WBishop (the parameters that change are the image, the name and the color)
class WBishop(Bishop):
    def __init__(self, game, x, y):
        Bishop.__init__(self, game, x, y)
        self.image = QPixmap("./img/wB")
        self.name = "wB"
        self.color = "w"


# Creation of the class BBishop (the parameters that change are the same than WBishop)
class BBishop(Bishop):
    def __init__(self, game, x, y):
        Bishop.__init__(self, game, x, y)
        self.image = QPixmap("./img/bB")
        self.name = "bB"
        self.color = "b"
