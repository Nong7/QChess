from PyQt5.QtGui import QPixmap

from .Piece import Piece
from .Blank import Blank


class WRook(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/wR")
        self.name = "wR"
        self.color = "w"

    def possible_movements(self):
        positions = []
        i = 1
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

        movements = []
        for position in positions:
            if isinstance(self.game.pieces[position[0]][position[1]], Blank) \
                    or self.game.pieces[position[0]][position[1]].color != self.color:
                movements.append(position)
        return movements


class BRook(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/bR")
        self.name = "bR"
        self.color = "b"

    def possible_movements(self):
        positions = []
        i = 1
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

        movements = []
        for position in positions:
            if isinstance(self.game.pieces[position[0]][position[1]], Blank) \
                    or self.game.pieces[position[0]][position[1]].color != self.color:
                movements.append(position)
        return movements
