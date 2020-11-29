from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QLabel
from .Piece import Piece


class WPawn(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y, "w")
        self.image = QPixmap("./img/wP")
        self.name = "wP"

    def possible_movements(self):
        # positions are not movements
        coords = self.coords
        positions = []

        if self.first_move:
            positions.append((coords[0] - 1, coords[1]))
            # Avoids jumping
            if self.game.pieces[coords[0] - 1][coords[1]].color == "":
                positions.append((coords[0] - 2, coords[1]))
        else:
            positions.append((coords[0] - 1, coords[1]))

        movements = []

        if not coords[1] == 7:
            if self.game.pieces[coords[0] - 1][coords[1] + 1].color != self.color \
                    and self.game.pieces[coords[0] - 1][coords[1] + 1].color != "":
                movements.append((coords[0] - 1, coords[1] + 1))
        if not coords[1] == 0:
            if self.game.pieces[coords[0] - 1][coords[1] - 1].color != self.color \
                    and self.game.pieces[coords[0] - 1][coords[1] - 1].color != "":
                movements.append((coords[0] - 1, coords[1] - 1))

        for position in positions:
            if self.game.pieces[position[0]][position[1]].color == "":
                movements.append(position)
        return movements


class BPawn(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y, "b")
        self.image = QPixmap("./img/bP")
        self.name = "bP"

    def possible_movements(self):
        # positions are not movements
        coords = self.coords
        positions = []

        if self.first_move:
            positions.append((coords[0] + 1, coords[1]))
            if self.game.pieces[coords[0] + 1][coords[1]].color == "":
                positions.append((coords[0] + 2, coords[1]))
        else:
            positions.append((coords[0] + 1, coords[1]))

        movements = []
        if not coords[0] == 7:
            if self.game.pieces[coords[0] + 1][coords[1] + 1].color != self.color \
                    and self.game.pieces[coords[0] + 1][coords[1] + 1].color != "":
                movements.append((coords[0] + 1, coords[1] + 1))
        if not coords[0] == 0:
            if self.game.pieces[coords[0] + 1][coords[1] - 1].color != self.color \
                    and self.game.pieces[coords[0] + 1][coords[1] - 1].color != "":
                movements.append((coords[0] + 1, coords[1] - 1))

        for position in positions:
            if self.game.pieces[position[0]][position[1]].color == "":
                movements.append(position)
        return movements
