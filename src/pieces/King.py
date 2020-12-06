from PyQt5.QtGui import QPixmap

from .Blank import Blank
from .Piece import Piece, QColor, QPainter, QLabel


# Creation of the class King from where the classes BKing and WKing will inherit
# This class inherits at the same time from the class Piece
class King(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)

    def is_on_check(self):
        mov = self.game.movements()

        for position in mov:
            if self.coords[0] == position[0] and self.coords[1] == position[1]:
                return True
                # print(self.coords[0], self.coords[1])
                # print(position)
        # print(mov)
        return False

    def paintEvent(self, event):
        Piece.paintEvent(self, event)
        x, y = self.width(), self.height()
        qp = QPainter(self)
        if self.is_on_check():
            qp.fillRect(0, 0, x, y, QColor(225, 0, 0))

        qp.drawPixmap(0, 0, x, y, self.image)

    def possible_movements(self):
        # Creation of a list to append all the possible positions
        positions = []
        i = 1

        # The if statements check all the squares that surround the king to see if they go off the
        # board and if they are a blank space, if those two conditions are correct the position is appended
        # In the case that the first condition isn't met if the squares that surround
        # the king are enemy pieces its position is appended
        if (self.coords[0] - i) >= 0 and (self.coords[1] - i) >= 0 \
                and (isinstance(self.game.pieces[self.coords[0] - i][self.coords[1] - i], Blank)
                     or self.game.pieces[self.coords[0] - i][self.coords[1] - i].color != self.color):
            positions.append((self.coords[0] - i, self.coords[1] - i))

        if (self.coords[0] + i) <= 7 and (self.coords[1] - i) >= 0 \
                and (isinstance(self.game.pieces[self.coords[0] + i][self.coords[1] - i], Blank)
                     or self.game.pieces[self.coords[0] + i][self.coords[1] - i].color != self.color):
            positions.append((self.coords[0] + i, self.coords[1] - i))

        if (self.coords[0] - i) >= 0 and (self.coords[1] + i) <= 7 \
                and (isinstance(self.game.pieces[self.coords[0] - i][self.coords[1] + i], Blank)
                     or self.game.pieces[self.coords[0] - i][self.coords[1] + i].color != self.color):
            positions.append((self.coords[0] - i, self.coords[1] + i))

        if (self.coords[0] + i) <= 7 and (self.coords[1] + i) <= 7 \
                and (isinstance(self.game.pieces[self.coords[0] + i][self.coords[1] + i], Blank)
                     or self.game.pieces[self.coords[0] + i][self.coords[1] + i].color != self.color):
            positions.append((self.coords[0] + i, self.coords[1] + i))

        if (self.coords[0] - i) >= 0 and (isinstance(self.game.pieces[self.coords[0] - i][self.coords[1]], Blank)
                                          or self.game.pieces[self.coords[0] - i][self.coords[1]].color != self.color):
            positions.append((self.coords[0] - i, self.coords[1]))

        if (self.coords[0] + i) <= 7 and (isinstance(self.game.pieces[self.coords[0] + i][self.coords[1]], Blank)
                                          or self.game.pieces[self.coords[0] + i][self.coords[1]].color != self.color):
            positions.append((self.coords[0] + i, self.coords[1]))

        if (self.coords[1] - i) >= 0 and (isinstance(self.game.pieces[self.coords[0]][self.coords[1] - i], Blank)
                                          or self.game.pieces[self.coords[0]][self.coords[1] - i].color != self.color):
            positions.append((self.coords[0], self.coords[1] - i))

        if (self.coords[1] + i) <= 7 and (isinstance(self.game.pieces[self.coords[0]][self.coords[1] + i], Blank)
                                          or self.game.pieces[self.coords[0]][self.coords[1] + i].color != self.color):
            positions.append((self.coords[0], self.coords[1] + i))

        return positions


# Creation of the class WKing (the parameters that change are the image, the name and the color)
class WKing(King):
    def __init__(self, game, x, y):
        King.__init__(self, game, x, y)
        self.image_path = f"./images/{self.game.piece_set}/wK"
        self.image = QPixmap(self.image_path)
        self.name = "wK"
        self.color = "w"


# Creation of the class BKing (the parameters that change are the same than WKing)
class BKing(King):
    def __init__(self, game, x, y):
        King.__init__(self, game, x, y)
        self.image_path = f"./images/{self.game.piece_set}/bK"
        self.image = QPixmap(self.image_path)
        self.name = "bK"
        self.color = "b"
