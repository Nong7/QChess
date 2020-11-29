from PyQt5.QtGui import QPixmap

from .Piece import Piece


class WKnight(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/wN")
        self.name = "wN"
        self.color = "w"

    def possible_movements(self):
        positions = []
        if (self.coords[0] - 2) >= (0) and (self.coords[1] - 1) >= (0) \
                and (self.game.pieces[self.coords[0] - 2][self.coords[1] - 1].color != self.color or isinstance(self.game.pieces[self.coords[0] - 2][self.coords[1] - 1], Blank)):
            positions.append((self.coords[0] - 2, self.coords[1] - 1))
        if (self.coords[0] - 2) >= (0) and (self.coords[1] + 1) <= (7) \
                and (self.game.pieces[self.coords[0] - 2][self.coords[1] + 1].color != self.color or isinstance(self.game.pieces[self.coords[0] - 2][self.coords[1] + 1], Blank)):
            positions.append((self.coords[0] - 2, self.coords[1] + 1))
        if (self.coords[0] - 1) >= (0) and (self.coords[1] - 2) >= (0) \
                and (self.game.pieces[self.coords[0] - 1][self.coords[1] - 2].color != self.color or isinstance(self.game.pieces[self.coords[0] - 1][self.coords[1] - 2], Blank)):
            positions.append((self.coords[0] - 1, self.coords[1] - 2))
        if (self.coords[0] - 1) >= (0) and (self.coords[1] + 2) <= (7) \
                and (self.game.pieces[self.coords[0] - 1][self.coords[1] + 2].color != self.color or isinstance(self.game.pieces[self.coords[0] - 1][self.coords[1] + 2], Blank)):
            positions.append((self.coords[0] - 1, self.coords[1] + 2))
        if (self.coords[0] + 2) <= (7) and (self.coords[1] + 1) <= (7) \
                and (self.game.pieces[self.coords[0] + 2][self.coords[1] + 1].color != self.color or isinstance(self.game.pieces[self.coords[0] + 2][self.coords[1] + 1], Blank)):
            positions.append((self.coords[0] + 2, self.coords[1] + 1))
        if (self.coords[0] + 2) <= (7) and (self.coords[1] - 1) >= (0) \
                and (self.game.pieces[self.coords[0] + 2][self.coords[1] - 1].color != self.color or isinstance(self.game.pieces[self.coords[0] + 2][self.coords[1] - 1], Blank)):
            positions.append((self.coords[0] + 2, self.coords[1] - 1))
        if (self.coords[0] + 1) <= (7) and (self.coords[1] + 2) <= (7) \
                and (self.game.pieces[self.coords[0] + 1][self.coords[1] + 2].color != self.color or isinstance(self.game.pieces[self.coords[0] + 1][self.coords[1] + 2], Blank)):
            positions.append((self.coords[0] + 1, self.coords[1] + 2))
        if (self.coords[0] + 1) <= (7) and (self.coords[1] - 2) >= (0) \
                and (self.game.pieces[self.coords[0] + 1][self.coords[1] - 2].color != self.color or isinstance(self.game.pieces[self.coords[0] + 1][self.coords[1] - 2], Blank)):
            positions.append((self.coords[0] + 1, self.coords[1] - 2))

        movements = []
        for position in positions:
            if isinstance(self.game.pieces[position[0]][position[1]], Blank) \
                    or self.game.pieces[position[0]][position[1]].color != self.color:
                movements.append(position)
        return movements


class BKnight(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/bN")
        self.name = "bN"
        self.color = "b"

    def possible_movements(self):
        positions = []
        if (self.coords[0] - 2) >= (0) and (self.coords[1] - 1) >= (0) \
                and (self.game.pieces[self.coords[0] - 2][self.coords[1] - 1].color != self.color or isinstance(
            self.game.pieces[self.coords[0] - 2][self.coords[1] - 1], Blank)):
            positions.append((self.coords[0] - 2, self.coords[1] - 1))
        if (self.coords[0] - 2) >= (0) and (self.coords[1] + 1) <= (7) \
                and (self.game.pieces[self.coords[0] - 2][self.coords[1] + 1].color != self.color or isinstance(
            self.game.pieces[self.coords[0] - 2][self.coords[1] + 1], Blank)):
            positions.append((self.coords[0] - 2, self.coords[1] + 1))
        if (self.coords[0] - 1) >= (0) and (self.coords[1] - 2) >= (0) \
                and (self.game.pieces[self.coords[0] - 1][self.coords[1] - 2].color != self.color or isinstance(
            self.game.pieces[self.coords[0] - 1][self.coords[1] - 2], Blank)):
            positions.append((self.coords[0] - 1, self.coords[1] - 2))
        if (self.coords[0] - 1) >= (0) and (self.coords[1] + 2) <= (7) \
                and (self.game.pieces[self.coords[0] - 1][self.coords[1] + 2].color != self.color or isinstance(
            self.game.pieces[self.coords[0] - 1][self.coords[1] + 2], Blank)):
            positions.append((self.coords[0] - 1, self.coords[1] + 2))
        if (self.coords[0] + 2) <= (7) and (self.coords[1] + 1) <= (7) \
                and (self.game.pieces[self.coords[0] + 2][self.coords[1] + 1].color != self.color or isinstance(
            self.game.pieces[self.coords[0] + 2][self.coords[1] + 1], Blank)):
            positions.append((self.coords[0] + 2, self.coords[1] + 1))
        if (self.coords[0] + 2) <= (7) and (self.coords[1] - 1) >= (0) \
                and (self.game.pieces[self.coords[0] + 2][self.coords[1] - 1].color != self.color or isinstance(
            self.game.pieces[self.coords[0] + 2][self.coords[1] - 1], Blank)):
            positions.append((self.coords[0] + 2, self.coords[1] - 1))
        if (self.coords[0] + 1) <= (7) and (self.coords[1] + 2) <= (7) \
                and (self.game.pieces[self.coords[0] + 1][self.coords[1] + 2].color != self.color or isinstance(
            self.game.pieces[self.coords[0] + 1][self.coords[1] + 2], Blank)):
            positions.append((self.coords[0] + 1, self.coords[1] + 2))
        if (self.coords[0] + 1) <= (7) and (self.coords[1] - 2) >= (0) \
                and (self.game.pieces[self.coords[0] + 1][self.coords[1] - 2].color != self.color or isinstance(
            self.game.pieces[self.coords[0] + 1][self.coords[1] - 2], Blank)):
            positions.append((self.coords[0] + 1, self.coords[1] - 2))

        movements = []
        for position in positions:
            if isinstance(self.game.pieces[position[0]][position[1]], Blank) \
                    or self.game.pieces[position[0]][position[1]].color != self.color:
                movements.append(position)
        return movements