from PyQt5.QtGui import QPixmap

from .Piece import Piece
from .Blank import Blank
import operator


# Creation of the class Knight from where the classes BKnight and WKnight will inherit
# This class inherits at the same time from the class Piece
class Knight(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)

    def possible_movements(self):
        # Creation of a list to append all the possible positions
        positions = []
        # Creation of a list with all the comparisons and operations that are going to be needed to check
        # the eight possible positions a knight can move to (usage of the operator library)
        operators = [[operator.sub, operator.sub, operator.ge, operator.ge, 2, 1, 0, 0], \
                     [operator.sub, operator.add, operator.ge, operator.le, 2, 1, 0, 7], \
                     [operator.sub, operator.sub, operator.ge, operator.ge, 1, 2, 0, 0], \
                     [operator.sub, operator.add, operator.ge, operator.le, 1, 2, 0, 7], \
                     [operator.add, operator.add, operator.le, operator.le, 2, 1, 7, 7], \
                     [operator.add, operator.sub, operator.le, operator.ge, 2, 1, 7, 0], \
                     [operator.add, operator.add, operator.le, operator.le, 1, 2, 7, 7], \
                     [operator.add, operator.sub, operator.le, operator.ge, 1, 2, 7, 0]]

        # The if statement checks all the possible positions a knight can cover
        # If the position checked is in the board and is a blank square the position is appended
        # If the position checked is in the board and is an enemy piece the position is appended as well
        for i in range(len(operators)):
            if operators[i][2](operators[i][0](self.coords[0], operators[i][4]), operators[i][6]) and \
                    operators[i][3](operators[i][1](self.coords[1], operators[i][5]), operators[i][7]) \
                    and (self.game.pieces[operators[i][0](self.coords[0], operators[i][4])][operators[i][1](self.coords[1], operators[i][5])].color != self.color or
                        isinstance(self.game.pieces[operators[i][0](self.coords[0], operators[i][4])][operators[i][1](self.coords[1], operators[i][5])], Blank)):
                positions.append((operators[i][0](self.coords[0], operators[i][4]), operators[i][1](self.coords[1], operators[i][5])))

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
