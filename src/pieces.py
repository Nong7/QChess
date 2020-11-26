from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QLabel


class Piece(QLabel):
    def __init__(self, game, x: int, y: int, color=""):
        QLabel.__init__(self)
        self.coords = x, y
        self.game = game
        self.color = color
        self.is_selected = False
        self.setScaledContents(True)

    def __repr__(self):
        return f"{type(self).__name__} ({self.color})"

    def select(self):
        self.is_selected = True
        self.game.selected_piece = self
        self.update()

    def unselect(self):
        self.is_selected = False
        self.game.selected_piece = None
        self.update()

    def mousePressEvent(self, event):
        QLabel.mousePressEvent(self, event)

        if self.name == "blank":
            if self.game.selected_piece:
                self.game.swap_pieces(self.coords, self.game.selected_piece.coords)
                self.game.selected_piece.unselect()
                self.unselect()

        elif self.color == self.game.turn:
            if not self.game.selected_piece:
                # Todo: pathfinding
                self.select()

        elif self.color != self.game.turn and self.game.selected_piece:
            self.game.eat_piece(self)

    def paintEvent(self, event):
        QLabel.paintEvent(self, event)
        x, y = self.width(), self.height()
        qp = QPainter(self)
        if (self.coords[0] + self.coords[1]) % 2 == 1:
            qp.fillRect(0, 0, x, y, QColor(200, 200, 200))
        if self.is_selected:
            qp.fillRect(0, 0, x, y, QColor(255, 240, 0))
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


class Knight(Piece):
    def __init__(self, game, x, y, color=""):
        Piece.__init__(self, game, x, y, color)
        if color == "w":
            self.image = QPixmap("./img/wN")
            self.name = "wN"
        else:
            self.image = QPixmap("./img/bN")
            self.name = "bN"


class Bishop(Piece):
    def __init__(self, game, x, y, color=""):
        Piece.__init__(self, game, x, y, color)
        if color == "w":
            self.image = QPixmap("./img/wB")
            self.name = "wB"
        else:
            self.image = QPixmap("./img/bB")
            self.name = "bB"


class Queen(Piece):
    def __init__(self, game, x, y, color=""):
        Piece.__init__(self, game, x, y, color)
        if color == "w":
            self.image = QPixmap("./img/wQ")
            self.name = "wQ"
        else:
            self.image = QPixmap("./img/bQ")
            self.name = "bQ"


class King(Piece):
    def __init__(self, game, x, y, color=""):
        Piece.__init__(self, game, x, y, color)
        if color == "w":
            self.image = QPixmap("./img/wK")
            self.name = "wK"
        else:
            self.image = QPixmap("./img/bK")
            self.name = "bK"


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
