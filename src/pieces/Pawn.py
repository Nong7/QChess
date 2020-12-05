from PyQt5.QtGui import QPixmap

from .Piece import Piece


# The pawn piece is the only one that has not been compressed into a single class and then inherited by two other
# classes since black pawns and white pawns have different directions. Therefore, they will have different possible
# movements

# Creation of the class WPiece which inherits from the class Piece
class WPawn(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/wP")
        self.name = "wP"
        self.color = "w"

    def possible_eatings(self):
        coords = self.coords
        eatings = []
        if not coords[1] == 7 and not coords[0] == 7:
            eatings.append((coords[0] - 1, coords[1] + 1))

        if not coords[1] == 0 and not coords[0] == 7:
            eatings.append((coords[0] - 1, coords[1] - 1))
        return eatings

    def possible_movements(self):
        # positions are not movements
        coords = self.coords
        positions = []

        if self.first_move:
            positions.append((coords[0] - 1, coords[1]))
            # Avoids jumping
            if not self.game.pieces[coords[0] - 1][coords[1]].color:
                positions.append((coords[0] - 2, coords[1]))
        else:
            positions.append((coords[0] - 1, coords[1]))

        movements = []

        if not coords[1] == 7 and not coords[0] == 0:
            if self.game.pieces[coords[0] - 1][coords[1] + 1].color != self.color \
                    and self.game.pieces[coords[0] - 1][coords[1] + 1].color:
                movements.append((coords[0] - 1, coords[1] + 1))
        if not coords[1] == 0 and not coords[0] == 0:
            if self.game.pieces[coords[0] - 1][coords[1] - 1].color != self.color \
                    and self.game.pieces[coords[0] - 1][coords[1] - 1].color:
                movements.append((coords[0] - 1, coords[1] - 1))

        for position in positions:
            if not self.game.pieces[position[0]][position[1]].color:
                movements.append(position)
        return movements


# Creation of the class BPawn which inherits from the class Piece
class BPawn(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/bP")
        self.name = "bP"
        self.color = "b"

    def possible_eatings(self):
        coords = self.coords
        eatings = []
        if not coords[1] == 7 and not coords[0] == 7:
            eatings.append((coords[0] + 1, coords[1] + 1))

        if not coords[1] == 0 and not coords[0] == 7:
            eatings.append((coords[0] + 1, coords[1] - 1))
        return eatings

    def possible_movements(self):
        # positions are not movements
        coords = self.coords
        pieces = self.game.pieces
        positions = []

        if self.first_move:
            positions.append((coords[0] + 1, coords[1]))
            # Avoids jumping
            if not pieces[coords[0] + 1][coords[1]].color:
                positions.append((coords[0] + 2, coords[1]))
        elif coords[0] != 7:
            positions.append((coords[0] + 1, coords[1]))

        movements = []

        if not coords[1] == 7 and not coords[0] == 7:
            if pieces[coords[0] + 1][coords[1] + 1].color != self.color and pieces[coords[0] + 1][coords[1] + 1].color:
                movements.append((coords[0] + 1, coords[1] + 1))

        if not coords[1] == 0 and not coords[0] == 7:
            if pieces[coords[0] + 1][coords[1] - 1].color != self.color and pieces[coords[0] + 1][coords[1] - 1].color:
                movements.append((coords[0] + 1, coords[1] - 1))

        for position in positions:
            if not pieces[position[0]][position[1]].color:
                movements.append(position)

        return movements
