from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout
from .pieces.Bishop import WBishop, BBishop
from .pieces.Blank import Blank
from .pieces.Knight import WKnight, BKnight
from .pieces.King import WKing, BKing
from .pieces.Pawn import WPawn, BPawn
from .pieces.Queen import WQueen, BQueen
from .pieces.Rook import WRook, BRook


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

        # Initial board state
        self.PIECES = [
            [BRook(self, 0, 0,), BKnight(self, 0, 1), BBishop(self, 0, 2), BQueen(self, 0, 3),
             BKing(self, 0, 4,), BBishop(self, 0, 5), BKnight(self, 0, 6), BRook(self, 0, 7)],
            [BPawn(self, 1, 0,), BPawn(self, 1, 1),   BPawn(self, 1, 2),   BPawn(self, 1, 3),
             BPawn(self, 1, 4,), BPawn(self, 1, 5),   BPawn(self, 1, 6),   BPawn(self, 1, 7)],
            [Blank(self, 2, 0),  Blank(self, 2, 1),   Blank(self, 2, 2),   Blank(self, 2, 3),
             Blank(self, 2, 4),  Blank(self, 2, 5),   Blank(self, 2, 6),   Blank(self, 2, 7)],
            [Blank(self, 3, 0),  Blank(self, 3, 1),   Blank(self, 3, 2),   Blank(self, 3, 3),
             Blank(self, 3, 4),  Blank(self, 3, 5),   Blank(self, 3, 6),   Blank(self, 3, 7)],
            [Blank(self, 4, 0),  Blank(self, 4, 1),   Blank(self, 4, 2),   Blank(self, 4, 3),
             Blank(self, 4, 4),  Blank(self, 4, 5),   Blank(self, 4, 6),   Blank(self, 4, 7)],
            [Blank(self, 5, 0),  Blank(self, 5, 1),   Blank(self, 5, 2),   Blank(self, 5, 3),
             Blank(self, 5, 4),  Blank(self, 5, 5),   Blank(self, 5, 6),   Blank(self, 5, 7)],
            [WPawn(self, 6, 0),  WPawn(self, 6, 1),   WPawn(self, 6, 2),   WPawn(self, 6, 3),
             WPawn(self, 6, 4),  WPawn(self, 6, 5),   WPawn(self, 6, 6),   WPawn(self, 6, 7)],
            [WRook(self, 7, 0),  WKnight(self, 7, 1), WBishop(self, 7, 2), WQueen(self, 7, 3),
             WKing(self, 7, 4),  WBishop(self, 7, 5), WKnight(self, 7, 6), WRook(self, 7, 7)]
        ]
        # Ugly way of doing a fake deepcopy of a list of lists
        self.pieces = [row[:] for row in self.PIECES]

        self.set_up_pieces()
        self.turn = "w"
        self.selected_piece = None

    def set_up_pieces(self):
        self.turn = "w"
        self.main_window.update_turn_label("White's turn")
        self.selected_piece = None
        # Ugly way of doing a fake deepcopy of a list of lists
        self.pieces = [row[:] for row in self.PIECES]
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

    def highlight_possible_moves(self):
        if self.selected_piece:
            possible_movements = self.selected_piece.possible_movements()
            for movement in possible_movements:
                self.pieces[movement[0]][movement[1]].highlight = True
                self.pieces[movement[0]][movement[1]].update()

    def eat_piece(self, eater_coords, eated_coords):
        # print(eater_coords, " eated ", eated_coords)

        self.main_layout.removeWidget(self.pieces[eated_coords[0]][eated_coords[1]])
        self.pieces[eated_coords[0]][eated_coords[1]].deleteLater()

        w1 = self.pieces[eater_coords[0]][eater_coords[1]]
        w2 = Blank(self, *eater_coords)

        self.pieces[eated_coords[0]][eated_coords[1]] = w1
        self.pieces[eater_coords[0]][eater_coords[1]] = w2

        self.update_board()

        w1.coords = eated_coords
        w2.coords = eater_coords
        w1.update()
        w2.update()
        self.change_turn()

        # self.debug_board()

    def swap_pieces(self, coords1: tuple, coords2: tuple):
        # print("Swaped ", coords1, coords2)

        # * is also an unpack operator, *(x, y) -> x, y
        w1 = self.main_layout.itemAtPosition(*coords1).widget()
        w2 = self.main_layout.itemAtPosition(*coords2).widget()

        # Swap:
        self.pieces[coords1[0]][coords1[1]], self.pieces[coords2[0]][coords2[1]] = \
            self.pieces[coords2[0]][coords2[1]], self.pieces[coords1[0]][coords1[1]]

        self.update_board()

        w1.coords = coords2
        w2.coords = coords1
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
