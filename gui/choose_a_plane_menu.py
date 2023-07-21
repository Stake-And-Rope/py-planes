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

        """ADD CUSTOM FONTS"""
        font = QFontDatabase.addApplicationFont(r'../fonts/American Captain.ttf')
        if font < 0:
            print('Error loading fonts!')
        fonts = QFontDatabase.applicationFontFamilies(font)

        """ADD THE LAYOUTS - ONE AT THE TOP, ONE AT THE BOTTOM AND ONE MAIN LAYOUT FOR BOTH"""
        top_layout = QVBoxLayout()        
        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()
        bottom_layout.addSpacing(10)
        
        planes_menu_main_layout = QVBoxLayout()

        bottom_grid_layout = QGridLayout()

        """ADDED A TOP GRID LAYOUT, WHICH WE WILL PUT IN THE TOP LAYOUT"""
        top_grid_layout = QGridLayout()
        top_grid_layout.setSpacing(30)  # spacing between the cells in the gird layout

        all_planes = deque(['base_plane', 'base_plane', 'base_plane', 'base_plane', 'base_plane', 'base_plane'])
        for row in range(2):
            for col in range(3):
                plane_image = f"../images/user_plane_images/{all_planes.pop()}.png"

                plane_button = QPushButton()
                plane_button.setProperty("class", "planes")
                plane_button.setIcon(QIcon(plane_image))
                plane_button.setIconSize(QSize(150, 150))
                plane_button.setFixedSize(140, 140)
                plane_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

                top_grid_layout.addWidget(plane_button, row, col)

        top_layout.addLayout(top_grid_layout)
        top_layout.addStretch()
        top_layout.addSpacing(10)

        """MAKE THE BUTTONS FOR THE BOTTOM LAYOUT"""
        plane_info_groupbox = QGroupBox()
        plane_info_groupbox.setFixedWidth(300)
        plane_info_groupbox.setFixedHeight(100)
        plane_info_layout = QHBoxLayout()


        # some_test_button = QPushButton()

        # plane_info_layout.addWidget(some_test_button)

        # plane_info_groupbox.setLayout(plane_info_layout)

        back_to_main_menu_button = QPushButton()
        back_to_main_menu_button.setText("Back to Main Menu")
        back_to_main_menu_button.setFont(QFont(fonts[0], 15))
        back_to_main_menu_button.setFixedWidth(175)
        back_to_main_menu_button.setFixedHeight(50)
        back_to_main_menu_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        start_button = QPushButton()
        start_button.setText("Start")
        start_button.setFont(QFont(fonts[0], 15))
        start_button.setFixedWidth(80)
        start_button.setFixedHeight(50)
        start_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        bottom_grid_layout.addWidget(plane_info_groupbox, 0, 0)
        bottom_grid_layout.addWidget(back_to_main_menu_button, 0, 1)
        bottom_grid_layout.addWidget(start_button, 0, 2)
        bottom_grid_layout.setVerticalSpacing(20)


        bottom_layout.addLayout(bottom_grid_layout)
        bottom_layout.addStretch(10)
        bottom_layout.addSpacing(20)
        top_layout.addStretch(10)
        top_layout.addSpacing(20)
        planes_menu_main_layout.addLayout(top_layout)
        planes_menu_main_layout.addLayout(bottom_layout)


        self.setLayout(planes_menu_main_layout)


def start_plane_menu_window():
    global plane_menu
    plane_menu = PlanesMenu()
    plane_menu.show()
