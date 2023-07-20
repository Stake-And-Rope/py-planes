import sys
from collections import deque

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pathlib import Path


class PlanesMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Planes Menu")
        self.setGeometry(200, 150, 600, 500)
        self.setMaximumWidth(600)
        self.setMaximumHeight(500)

        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()
        planes_menu_main_layout = QVBoxLayout()

        bottom_layout.addStretch(0)
        bottom_layout.addSpacing(100)

        top_grid_layout = QGridLayout()
        top_grid_layout.setSpacing(60)

        all_planes = deque(['base_plane', 'base_plane', 'base_plane', 'base_plane', 'base_plane', 'base_plane'])
        for row in range(2):
            for col in range(3):
                plane_image = f"../images/user_plane_images/{all_planes.pop()}.png"

                plane_button = QPushButton()
                plane_button.setIcon(QIcon(plane_image))
                plane_button.setIconSize(QSize(150, 150))
                plane_button.setFixedSize(140, 140)

                top_grid_layout.addWidget(plane_button, row, col)

        top_layout.addLayout(top_grid_layout)

        back_to_main_menu_button = QPushButton()
        back_to_main_menu_button.setText("Back to Main Menu")
        back_to_main_menu_button.setFixedWidth(150)
        back_to_main_menu_button.setFixedHeight(50)

        start_button = QPushButton()
        start_button.setText("Start")
        start_button.setFixedWidth(80)
        start_button.setFixedHeight(50)

        bottom_layout.addWidget(back_to_main_menu_button)
        bottom_layout.addWidget(start_button)

        planes_menu_main_layout.addLayout(top_layout)
        planes_menu_main_layout.addLayout(bottom_layout)

        self.setLayout(planes_menu_main_layout)


        # grid_layout = QGridLayout()
        #
        #
        #
        # for row in range(2):
        #     for col in range(3):
        #         plane_button = QPushButton()
        #         plane_button.setStyleSheet("background-image : url(../images/user_plane_images/base_plane.png);")
        #         plane_button.setGeometry(200, 150, 200, 40)
        #
        #         grid_layout.addWidget(plane_button, row, col)
        #
        # self.setLayout(grid_layout)


def start_plane_menu_window():
    global plane_menu
    plane_menu = PlanesMenu()
    plane_menu.show()
