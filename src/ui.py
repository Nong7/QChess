from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import socket
import multiprocess
from time import sleep
from sys import exit


# Port used by the app for network connections. Could be changed
PORT = 8000


class BaseWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        w = QWidget()
        # Main layout
        self.main_layout = QVBoxLayout()
        w.setLayout(self.main_layout)
        self.setCentralWidget(w)
        font = QFont("Arial")
        font.setPointSize(10)
        self.setFont(font)


class GuestNetworkSetUp(BaseWindow):
    def __init__(self):
        BaseWindow.__init__(self)

        # Avoids other windows to be manipulated
        self.setWindowModality(Qt.ApplicationModal)

        # This does not always work in all systems
        ip_label = QLabel(f"Your IP: {socket.gethostbyname(socket.gethostname())}")
        self.main_layout.addWidget(ip_label)

        host_ip_label = QLabel("Introduce other player's private IP:")
        self.main_layout.addWidget(host_ip_label)

        self.host_ip_input = QLineEdit()
        self.host_ip_input.setText("192.168.0.0")
        self.host_ip_input.setInputMask("000.000.000.000")
        self.main_layout.addWidget(self.host_ip_input)

        self.connect_button = QPushButton("Connect to other player")
        self.connect_button.clicked.connect(self.guest_set_up)
        self.main_layout.addWidget(self.connect_button)

        self.show()

    def guest_set_up(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host_ip_input.text(), PORT))
            s.sendall(b'Hello, world')
            data = s.recv(1024)
        print('Received', repr(data))


class HostNetworkSetUp(BaseWindow):
    def __init__(self):
        BaseWindow.__init__(self)

        # Avoids other windows to be manipulated
        self.setWindowModality(Qt.ApplicationModal)

        # This does not always work in all systems
        self.ip = socket.gethostbyname(socket.gethostname())
        ip_label = QLabel(f"Your IP: {self.ip}")
        self.main_layout.addWidget(ip_label)

        waiting_label = QLabel("Waiting for a player to join the game")
        self.main_layout.addWidget(waiting_label)
        p = multiprocessing.Process(target=self.host_set_up)
        p.start()
        p.join()
        self.show()

    def host_set_up(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.ip, PORT))
            sock.listen()
            connection, addr = sock.accept()
            # connection is a socket connected to the client
            with connection:
                print('Connected by', addr)
                while True:
                    print("A")
                    sleep(1)
                    data = connection.recv(1024)
                    print(data.decode("utf-8"))
                    if not data:
                        break
                    connection.sendall(data)


class ModeSelectionWindow(BaseWindow):
    def __init__(self, parent: "MainWindow"):
        BaseWindow.__init__(self)
        self.setWindowTitle("Choose mode")

        # Avoids other windows to be manipulated
        self.setWindowModality(Qt.ApplicationModal)

        # Changes the type of window to a simpler one
        self.setWindowFlags(Qt.Tool)

        setup_label = QLabel("Choose mode:")
        self.main_layout.addWidget(setup_label)

        offline_button = QPushButton("Offline mode")
        self.main_layout.addWidget(offline_button)
        offline_button.clicked.connect(parent.offline_mode_set_up)

        online_label = QLabel("Online mode:")
        self.main_layout.addWidget(online_label)

        host_button = QPushButton("Host")
        self.main_layout.addWidget(host_button)
        host_button.clicked.connect(parent.host_mode_set_up)

        guest_button = QPushButton("Guest")
        self.main_layout.addWidget(guest_button)
        guest_button.clicked.connect(parent.guest_mode_set_up)


class MainWindow(BaseWindow):
    def __init__(self, app):
        BaseWindow.__init__(self)
        self.app = app
        self.show()
        self.modeSelectionWindow = ModeSelectionWindow(self)
        self.modeSelectionWindow.show()

    def offline_mode_set_up(self):
        self.modeSelectionWindow.close()
        print("To do")

    def host_mode_set_up(self):
        self.modeSelectionWindow.close()
        self.host_set_up = HostNetworkSetUp()

    def guest_mode_set_up(self):
        self.modeSelectionWindow.close()
        self.guest_set_up = GuestNetworkSetUp()

    def closeEvent(self, event):
        QMainWindow.closeEvent(self, event)
        self.app.quit()
        self.host_set_up.stop_thread.set()

