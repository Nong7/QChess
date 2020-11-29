from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QLabel


class Piece(QLabel):
    def __init__(self, game, x: int, y: int):
        QLabel.__init__(self)
        self.first_move = True
        self.coords = x, y
        self.game = game
        self.color = None
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
                self.game.selected_piece.first_move = False

                if self.highlight:
                    self.game.swap_pieces(self.coords, self.game.selected_piece.coords)

        elif self.color == self.game.turn:
            self.select()

        elif self.color != self.game.turn and self.game.selected_piece:
            # Eated piece: self
            # Eaten by: self.game.selected_piece
            if self.highlight:
                # Pawns can move two cells ahead only once
                self.game.selected_piece.first_move = False
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