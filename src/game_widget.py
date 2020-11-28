from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout

from .pieces import Pawn, Queen, Bishop, King, Knight, Rook, Blank


class GameWidget(QWidget):
    def __init__(self, window):
        QWidget.__init__(self)

        self.main_window = window

        font = QFont("Arial")
        font.setPointSize(10)
        self.setFont(font)

        # Main layout
        self.main_layout = QGridLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)

        self.pieces = [
            [Rook(self, 0, 0, "b"), Knight(self, 1, 0, "b"), Bishop(self, 2, 0, "b"), Queen(self, 3, 0, "b"),
             King(self, 4, 0, "b"), Bishop(self, 5, 0, "b"), Knight(self, 6, 0, "b"), Rook(self, 7, 0, "b")],
            [Pawn(self, 0, 1, "b"), Pawn(self, 1, 1, "b"), Pawn(self, 2, 1, "b"), Pawn(self, 3, 1, "b"),
             Pawn(self, 4, 1, "b"), Pawn(self, 5, 1, "b"), Pawn(self, 6, 1, "b"), Pawn(self, 7, 1, "b")],
            [Blank(self, 0, 2), Blank(self, 1, 2), Blank(self, 2, 2), Blank(self, 3, 2),
             Blank(self, 4, 2), Blank(self, 5, 2), Blank(self, 6, 2), Blank(self, 7, 2)],
            [Blank(self, 0, 3), Blank(self, 1, 3), Blank(self, 2, 3), Blank(self, 3, 3),
             Blank(self, 4, 3), Blank(self, 5, 3), Blank(self, 6, 3), Blank(self, 7, 3)],
            [Blank(self, 0, 4), Blank(self, 1, 4), Blank(self, 2, 4), Blank(self, 3, 4),
             Blank(self, 4, 4), Blank(self, 5, 4), Blank(self, 6, 4), Blank(self, 7, 4)],
            [Blank(self, 0, 5), Blank(self, 1, 5), Blank(self, 2, 5), Blank(self, 3, 5),
             Blank(self, 4, 5), Blank(self, 5, 5), Blank(self, 6, 5), Blank(self, 7, 5)],
            [Pawn(self, 0, 6, "w"), Pawn(self, 1, 6, "w"), Pawn(self, 2, 6, "w"), Pawn(self, 3, 6, "w"),
             Pawn(self, 4, 6, "w"), Pawn(self, 5, 6, "w"), Pawn(self, 6, 6, "w"), Pawn(self, 7, 6, "w")],
            [Rook(self, 0, 7, "w"), Knight(self, 1, 7, "w"), Bishop(self, 2, 7, "w"), Queen(self, 3, 7, "w"),
             King(self, 4, 7, "w"), Bishop(self, 5, 7, "w"), Knight(self, 6, 7, "w"), Rook(self, 7, 7, "w")]
        ]
        self.set_up_pieces()
        self.turn = "w"
        self.selected_piece = None

    def set_up_pieces(self):
        self.pieces = [
            [Rook(self, 0, 0, "b"), Knight(self, 1, 0, "b"), Bishop(self, 2, 0, "b"), Queen(self, 3, 0, "b"),
             King(self, 4, 0, "b"), Bishop(self, 5, 0, "b"), Knight(self, 6, 0, "b"), Rook(self, 7, 0, "b")],
            [Pawn(self, 0, 1, "b"), Pawn(self, 1, 1, "b"), Pawn(self, 2, 1, "b"), Pawn(self, 3, 1, "b"),
             Pawn(self, 4, 1, "b"), Pawn(self, 5, 1, "b"), Pawn(self, 6, 1, "b"), Pawn(self, 7, 1, "b")],
            [Blank(self, 0, 2), Blank(self, 1, 2), Blank(self, 2, 2), Blank(self, 3, 2),
             Blank(self, 4, 2), Blank(self, 5, 2), Blank(self, 6, 2), Blank(self, 7, 2)],
            [Blank(self, 0, 3), Blank(self, 1, 3), Blank(self, 2, 3), Blank(self, 3, 3),
             Blank(self, 4, 3), Blank(self, 5, 3), Blank(self, 6, 3), Blank(self, 7, 3)],
            [Blank(self, 0, 4), Blank(self, 1, 4), Blank(self, 2, 4), Blank(self, 3, 4),
             Blank(self, 4, 4), Blank(self, 5, 4), Blank(self, 6, 4), Blank(self, 7, 4)],
            [Blank(self, 0, 5), Blank(self, 1, 5), Blank(self, 2, 5), Blank(self, 3, 5),
             Blank(self, 4, 5), Blank(self, 5, 5), Blank(self, 6, 5), Blank(self, 7, 5)],
            [Pawn(self, 0, 6, "w"), Pawn(self, 1, 6, "w"), Pawn(self, 2, 6, "w"), Pawn(self, 3, 6, "w"),
             Pawn(self, 4, 6, "w"), Pawn(self, 5, 6, "w"), Pawn(self, 6, 6, "w"), Pawn(self, 7, 6, "w")],
            [Rook(self, 0, 7, "w"), Knight(self, 1, 7, "w"), Bishop(self, 2, 7, "w"), Queen(self, 3, 7, "w"),
             King(self, 4, 7, "w"), Bishop(self, 5, 7, "w"), Knight(self, 6, 7, "w"), Rook(self, 7, 7, "w")]
        ]
        for x in range(8):
            for y in range(8):
                self.main_layout.addWidget(self.pieces[x][y], x, y)

    def set_selected_piece(self, piece):
        if self.selected_piece:
            self.selected_piece.unselect()
        self.selected_piece = piece

    def change_turn(self):
        if self.selected_piece:
            self.selected_piece.unselect()
        if self.turn == "b":
            self.turn = "w"
            self.main_window.update_turn_label("White's turn")
        else:
            self.turn = "b"
            self.main_window.update_turn_label("Black's turn")

    def board(self):
        mat = []
        for i in range(8):
            row = [self.main_layout.itemAtPosition(i, j).widget() for j in range(8)]
            mat.append(row)
        return mat

    def update_board(self):
        for x in range(8):
            for y in range(8):
                self.main_layout.removeWidget(self.pieces[x][y])

        for x in range(8):
            for y in range(8):
                self.main_layout.addWidget(self.pieces[x][y], x, y)
        # self.debug_board()

    def eat_piece(self, eater_coords, eated_coords):
        # print(eater_coords, " eated ", eated_coords)

        eater_coords = eater_coords[1], eater_coords[0]
        eated_coords = eated_coords[1], eated_coords[0]

        self.main_layout.removeWidget(self.pieces[eated_coords[0]][eated_coords[1]])
        self.pieces[eated_coords[0]][eated_coords[1]].deleteLater()

        w1 = self.pieces[eater_coords[0]][eater_coords[1]]
        w2 = Blank(self, *eater_coords)

        self.pieces[eated_coords[0]][eated_coords[1]] = w1
        self.pieces[eater_coords[0]][eater_coords[1]] = w2

        self.update_board()

        w1.coords = eated_coords[1], eated_coords[0]
        w2.coords = eater_coords[1], eater_coords[0]
        w1.update()
        w2.update()
        self.change_turn()

        # self.debug_board()

    def swap_pieces(self, coords1: tuple, coords2: tuple):
        coords1 = coords1[1], coords1[0]
        coords2 = coords2[1], coords2[0]

        # print("Swaped ", coords1, coords2)

        # * is also an unpack operator, *(x, y) -> x, y
        w1 = self.main_layout.itemAtPosition(*coords1).widget()
        w2 = self.main_layout.itemAtPosition(*coords2).widget()

        # Swap:
        self.pieces[coords1[0]][coords1[1]], self.pieces[coords2[0]][coords2[1]] = \
            self.pieces[coords2[0]][coords2[1]], self.pieces[coords1[0]][coords1[1]]

        self.update_board()

        w1.coords = coords2[1], coords2[0]
        w2.coords = coords1[1], coords1[0]
        w1.update()
        w2.update()
        self.change_turn()
        # self.debug_board()

    def resizeEvent(self, event):
        QWidget.resizeEvent(self, event)
        # Keeps square aspect ratio
        if self.width() > self.height():
            self.resize(self.height(), self.height())
        else:
            self.resize(self.width(), self.width())

    def debug_board(self):
        try:
            assert self.board() == self.pieces
        except AssertionError:
            for row in self.board():
                print(row)
            # pprint(self.pieces, width=100)
