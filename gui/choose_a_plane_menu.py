import sys
from collections import deque

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

sys.path.append(r'.')
from gui import display_plane_info
from gui import main_menu

sys.path.append(r"..")
from settings import settings_handler



global current_gold, current_rank
current_gold = 100

class PlanesMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Planes Menu")
        self.setWindowIcon(QIcon(r"images/menu/plane_icon.jpg"))
        self.setGeometry(200, 150, 600, 500)
        self.setMaximumWidth(600)
        self.setMaximumHeight(500)
        
        """READ THE PLANES SETTINGS"""
        ps = settings_handler.get_planes_settings()

        def plane_info_display(curr_plane_name):
            plane_info_groupbox.hide()

            current_groupbox = display_plane_info.plane_info_return_groupbox(read_plane_stats(curr_plane_name))
            # current_groupbox = display_plane_info.plane_info_return_groupbox(curr_plane_name)
            bottom_grid_layout.itemAtPosition(0, 0).widget().setParent(None)
            bottom_grid_layout.addWidget(current_groupbox, 0, 0)


        def open_plane_info(plane_name):
            return lambda: plane_info_display(plane_name)

        """ADD CUSTOM FONTS"""
        font = QFontDatabase.addApplicationFont(r'fonts/American Captain.ttf')
        if font < 0:
            print('Error loading fonts!')
        fonts = QFontDatabase.applicationFontFamilies(font)

        """MAKE A HORIZONTAL LAYOUT FOR THE GOLD"""
        top_gold_layout = QHBoxLayout()

        gold_icon = QLabel()
        gold_icon.setFixedSize(64, 64)
        gold_icon.setPixmap(QPixmap(f"images/menu/gold_icon.png"))

        gold_value = QLabel()
        gold_value.setText(f"{current_gold} Gold")
        gold_value.setFont(QFont(fonts[0], 16))

        top_gold_layout.addWidget(gold_icon)
        top_gold_layout.addWidget(gold_value)

        """ADD THE LAYOUTS - ONE AT THE TOP, ONE AT THE BOTTOM AND ONE MAIN LAYOUT FOR BOTH"""
        top_layout = QVBoxLayout()        
        bottom_layout = QVBoxLayout()
        bottom_layout.addStretch()
        bottom_layout.addSpacing(10)
        
        planes_menu_main_layout = QVBoxLayout()

        bottom_grid_layout = QGridLayout()

        """ADDED A TOP GRID LAYOUT, WHICH WE WILL PUT IN THE TOP LAYOUT"""
        top_grid_layout = QGridLayout()
        top_grid_layout.setSpacing(30)  # spacing between the cells in the gird layout

        all_planes = deque(['user_plane_1', 'user_plane_2', 'user_plane_3', 'user_plane_4', 'user_plane_5', 'user_plane_6'])
        
        for row in range(2):
            for col in range(3):
                curr_name_plane = all_planes.popleft()
                plane_image = f"images/user_plane_images/{curr_name_plane}.png"

                plane_button = QPushButton()
                plane_button.setProperty("class", "planes")
                plane_button.setIcon(QIcon(plane_image))
                plane_button.setIconSize(QSize(150, 150))
                plane_button.setFixedSize(140, 140)
                plane_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                plane_button.clicked.connect(open_plane_info(curr_name_plane))


                top_grid_layout.addWidget(plane_button, row, col)

        top_layout.addLayout(top_grid_layout)
        top_layout.addStretch()
        top_layout.addSpacing(10)

        """MAKE THE LAYOUT FOR THE PLANE'S INFO LABEL"""
        layout_for_plane_info_name = QVBoxLayout()
        plane_info_name_label = QLabel()
        plane_info_name_label.setText("Plane's info")
        plane_info_name_label.setFont(QFont(fonts[0], 12))
        layout_for_plane_info_name.addWidget(plane_info_name_label)
        layout_for_plane_info_name.addSpacing(-25)

        """MAKE THE BUTTONS FOR THE BOTTOM LAYOUT"""
        plane_info_groupbox = QGroupBox()
        plane_info_groupbox.setFixedWidth(300)
        plane_info_groupbox.setFixedHeight(120)

        back_to_main_menu_button = QPushButton()
        back_to_main_menu_button.setText("Back to Main Menu")
        back_to_main_menu_button.setFont(QFont(fonts[0], 15))
        back_to_main_menu_button.setFixedWidth(175)
        back_to_main_menu_button.setFixedHeight(50)
        back_to_main_menu_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        back_to_main_menu_button.clicked.connect(lambda: back_to_main_menu())

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
        top_layout.addSpacing(0)

        planes_menu_main_layout.addLayout(top_gold_layout)
        planes_menu_main_layout.addLayout(top_layout)
        planes_menu_main_layout.addLayout(layout_for_plane_info_name)
        planes_menu_main_layout.addLayout(bottom_layout)

        self.setLayout(planes_menu_main_layout)
        
        def read_plane_stats(plane):
            plane_stats = ps.get(plane)
            global result
            result = []
            for k,v in plane_stats.items():
                cur_res = k + " --> " + v
                result.append(cur_res)
            return result 

def start_plane_menu_window():
    global plane_menu
    plane_menu = PlanesMenu()
    plane_menu.show()

def back_to_main_menu():
    global plane_menu
    plane_menu.hide()
    main_menu.open_main_menu()