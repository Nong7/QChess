from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QLabel


class Piece(QLabel):
    def __init__(self, game, x: int, y: int, color=""):
        QLabel.__init__(self)
        self.coords = x, y
        self.game = game
        self.color = color
        self.is_selected = False
        self.highlight = False
        self.setScaledContents(True)

    def __repr__(self):
        if type(self).__name__ == "Blank":
            return "Blank"
        return f"{type(self).__name__}{self.color} ({self.coords})"

    def select(self):
        # Avoids multiple pieces to be selected:
        if self.game.selected_piece:
            self.game.selected_piece.unselect()
        self.is_selected = True
        self.game.selected_piece = self
        self.game.highlight_possible_moves()
        self.update()

    def unselect(self):
        self.is_selected = False
        self.game.selected_piece = None
        for x in range(8):
            for y in range(8):
                self.game.pieces[x][y].highlight = False
                self.game.pieces[x][y].update()
        self.update()

    def possible_movements(self):
        """
            Returns a list of tuples which represent the possible movements of the piece
        """
        pass

    def mousePressEvent(self, event):
        QLabel.mousePressEvent(self, event)
        if self.name == "blank":
            if self.game.selected_piece:

                # Pawns can move two cells ahead only once
                if isinstance(self.game.selected_piece, Pawn):
                    self.game.selected_piece.first_move = False

                if self.highlight:
                    self.game.swap_pieces(self.coords, self.game.selected_piece.coords)

        elif self.color == self.game.turn:
            self.select()

        elif self.color != self.game.turn and self.game.selected_piece:
            # Eated piece: self
            # Eaten by: self.game.selected_piece
            if self.highlight:
                self.game.eat_piece(self.game.selected_piece.coords, self.coords)

    def paintEvent(self, event):
        QLabel.paintEvent(self, event)
        x, y = self.width(), self.height()
        qp = QPainter(self)
        if (self.coords[0] + self.coords[1]) % 2 == 1:
            qp.fillRect(0, 0, x, y, QColor(200, 200, 200))
        if self.is_selected:
            # Fills the background in yellow if the piece is selected
            qp.fillRect(0, 0, x, y, QColor(255, 240, 0))
        if self.highlight:
            qp.fillRect(0, 0, x, y, QColor(0, 255, 0))
        qp.drawPixmap(0, 0, x, y, self.image)


class Blank(Piece):
    def __init__(self, game, x, y):
        Piece.__init__(self, game, x, y)
        self.image = QPixmap("./img/blank")
        self.name = "blank"


class Rook(Piece):
    def __init__(self, game, x, y, color=""):
        Piece.__init__(self, game, x, y, color)
        if color == "w":
            self.image = QPixmap("./img/wR")
            self.name = "wR"
        else:
            self.image = QPixmap("./img/bR")
            self.name = "bR"

    def possible_movements(self):
        position = self.coords
        movements = [(1, 1)]

        return movements


class Knight(Piece):
    def __init__(self, game, x, y, color=""):
        Piece.__init__(self, game, x, y, color)
        if color == "w":
            self.image = QPixmap("./img/wN")
            self.name = "wN"
        else:
            self.image = QPixmap("./img/bN")
            self.name = "bN"

    def possible_movements(self):
        return [(1, 1)]


class Bishop(Piece):
    def __init__(self, game, x, y, color=""):
        Piece.__init__(self, game, x, y, color)
        if color == "w":
            self.image = QPixmap("./img/wB")
            self.name = "wB"
        else:
            self.image = QPixmap("./img/bB")
            self.name = "bB"

    def possible_movements(self):
        return [(1, 1)]


class Queen(Piece):
    def __init__(self, game, x, y, color=""):
        Piece.__init__(self, game, x, y, color)
        if color == "w":
            self.image = QPixmap("./img/wQ")
            self.name = "wQ"
        else:
            self.image = QPixmap("./img/bQ")
            self.name = "bQ"

    def possible_movements(self):
        return [(1, 1)]


class King(Piece):
    def __init__(self, game, x, y, color=""):
        Piece.__init__(self, game, x, y, color)
        if color == "w":
            self.image = QPixmap("./img/wK")
            self.name = "wK"
        else:
            self.image = QPixmap("./img/bK")
            self.name = "bK"

    def possible_movements(self):
        return [(1, 1)]


class Pawn(Piece):
    def __init__(self, game, x, y, color=""):
        Piece.__init__(self, game, x, y, color)
        self.first_move = True
        if color == "w":
            self.image = QPixmap("./img/wP")
            self.name = "wP"
        else:
            self.image = QPixmap("./img/bP")
            self.name = "bQ"

    def possible_movements(self):
        # positions are not movements
        coords = self.coords
        positions = []

        if self.first_move:
            if self.color == "w":
                positions.append((coords[0] - 1, coords[1]))
                # Avoids jumping
                if isinstance(self.game.pieces[coords[0] - 1][coords[1]], Blank):
                    positions.append((coords[0] - 2, coords[1]))
            else:
                positions.append((coords[0] + 1, coords[1]))
                if isinstance(self.game.pieces[coords[0] + 1][coords[1]], Blank):
                    positions.append((coords[0] + 2, coords[1]))
        else:
            if self.color == "w":
                positions.append((coords[0] - 1, coords[1]))
            else:
                positions.append((coords[0] + 1, coords[1]))

        movements = []
        if self.color == "w":
            if not coords[1] == 7:
                if self.game.pieces[coords[0] - 1][coords[1] + 1].color != self.color \
                        and not isinstance(self.game.pieces[coords[0] - 1][coords[1] + 1], Blank):
                    movements.append((coords[0] - 1, coords[1] + 1))
            if not coords[1] == 0:
                if self.game.pieces[coords[0] - 1][coords[1] - 1].color != self.color \
                        and not isinstance(self.game.pieces[coords[0] - 1][coords[1] - 1], Blank):
                    movements.append((coords[0] - 1, coords[1] - 1))
        else:
            if not coords[0] == 7:
                if self.game.pieces[coords[0] + 1][coords[1] + 1].color != self.color \
                        and not isinstance(self.game.pieces[coords[0] + 1][coords[1] + 1], Blank):
                    movements.append((coords[0] + 1, coords[1] + 1))
            if not coords[0] == 0:
                if self.game.pieces[coords[0] + 1][coords[1] - 1].color != self.color \
                        and not isinstance(self.game.pieces[coords[0] + 1][coords[1] - 1], Blank):
                    movements.append((coords[0] + 1, coords[1] - 1))

        for position in positions:
            if isinstance(self.game.pieces[position[0]][position[1]], Blank):
                movements.append(position)
        return movements
