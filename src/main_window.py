from PyQt5.QtCore import Qt, QUrl, QFileInfo
from PyQt5.QtGui import QFont, QDesktopServices, QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QAction, QApplication, QComboBox, QPushButton

from .game_widget import GameWidget


class ChangePiecesWindow(QMainWindow):
    def __init__(self, w):
        QMainWindow.__init__(self)

        self.setWindowTitle("Change piece set")
        self.setWindowFlag(Qt.Tool)
        self.setWindowModality(Qt.ApplicationModal)

        self.w = w
        cw = QWidget(self)
        self.setCentralWidget(cw)

        font = QFont("Arial")
        font.setPointSize(10)
        self.setFont(font)

        self.piece_sets = ["Default", "Condal", "Kingdom", "Leipzig", "Magnetic",
                           "Marroquin", "Maya", "Medieval", "Motif"]

        label = QLabel("Choose a piece set:", cw)
        label.setGeometry(10, 10, 180, 25)

        self.combo_box = QComboBox(cw)
        self.combo_box.setGeometry(10, 40, 180, 30)

        for s in self.piece_sets:
            self.combo_box.addItem(s)

        self.accept_button = QPushButton("Accept", cw)
        self.accept_button.setGeometry(10, 80, 90, 30)
        self.accept_button.clicked.connect(lambda: self.change())

        self.cancel_button = QPushButton("Cancel", cw)
        self.cancel_button.setGeometry(100, 80, 90, 30)

        self.setFixedSize(200, 120)

    def change(self):
        self.w.game_widget.piece_set = self.combo_box.currentText()
        self.w.game_widget.change_images()
        self.close()


class MainWindow(QMainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)

        self.app = app
        self.setWindowTitle("QChess")
        self.setMinimumSize(400, 450)
        w = QWidget()

        self.setCentralWidget(w)
        font = QFont("Arial")
        font.setPointSize(10)
        self.setFont(font)

        # Label that shows whose turn it is. It is updated in "game_widget.py" via the function "change_turn"
        self.turn_label = QLabel("White's turn", w)

        self.game_widget = GameWidget(self, w)

        # Creation of the menu bar and insertion of the different actions that it has
        self.menu_bar = self.menuBar()

        # Options menu
        self.options_menu = self.menu_bar.addMenu("Options")
        self.action_change_theme = QAction("Set dark theme")
        self.action_change_theme.triggered.connect(lambda: self.change_theme())
        self.options_menu.addAction(self.action_change_theme)

        self.manual = QAction("Game Manual", self)
        self.options_menu.addAction(self.manual)

        self.guia = QUrl.fromLocalFile(QFileInfo("./guide.pdf").absoluteFilePath())
        self.manual.triggered.connect(lambda: QDesktopServices.openUrl(self.guia))

        self.change_pieces_action = QAction("Change piece images")
        self.options_menu.addAction(self.change_pieces_action)
        self.change_pieces_window = ChangePiecesWindow(self)
        self.change_pieces_action.triggered.connect(lambda: self.change_pieces_window.show())

        # Restart action (restarts the game)
        self.restart_action = QAction("Restart game", self)
        # When "Restart game" is triggered it calls a lambda function which restarts the board
        self.restart_action.triggered.connect(lambda: self.game_widget.reset_board())
        self.options_menu.addAction(self.restart_action)

        # Exit action (exits the app via clicking the action or typing the shortcut)
        self.exit_action = QAction("Exit App", self)
        self.exit_action.setShortcut("Ctrl+Q")
        # When "Exit App" is triggered it calls a lambda function that exits the app
        self.exit_action.triggered.connect(lambda: QApplication.quit())
        self.options_menu.addAction(self.exit_action)

        self.show()

    def update_turn_label(self, text: str):
        self.turn_label.setText(text)

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)

        # This is an ugly way of centering the widgets which relies in a lot of magic numbers hardcoded,
        # but I have not found how to center the QGridLayout without destroying the geometry of its cells

        self.turn_label.setGeometry((self.width() + 20) // 2 - self.turn_label.width() // 2,
                                    5, self.turn_label.width(), 20)
        if self.width() > self.height():
            mx = self.width() // 2
            x0 = mx - (self.height() - 30) // 2
            y0 = 30
            x = self.height() - 30
            y = self.height() - 60
        else:
            mx = self.width() // 2
            x0 = mx - (self.width() - 25) // 2
            y0 = 30
            x = self.width() - 30
            y = self.width() - 60
            self.game_widget.setGeometry(x0, y0, x, y)

        self.game_widget.setGeometry(x0, y0, x, y)

    def change_theme(self):
        if self.action_change_theme.text() == "Set dark theme":
            # Set dark theme
            dark_theme = QPalette()

            # Background color
            dark_theme.setColor(QPalette.Window, QColor(30, 30, 30))

            # Text label color
            dark_theme.setColor(QPalette.WindowText, Qt.white)

            self.setPalette(dark_theme)
            self.menu_bar.setStyleSheet("""QMenuBar {background-color: black;}
            QMenuBar::item {background-color: #383838; color: white}""")
            self.action_change_theme.setText("Set light theme")
        else:
            # Set light mode
            light_theme = QPalette(self.style().standardPalette())
            self.setPalette(light_theme)
            self.action_change_theme.setText("Set dark theme")
            self.menu_bar.setStyleSheet("""QMenuBar {background-color: white;}
            QMenuBar::item {background-color: white; color: black}""")
