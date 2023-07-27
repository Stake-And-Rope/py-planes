#!/usr/bin/python3

"""IMPORT PyQt5 ENGINE"""
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QGridLayout,
                             QLabel,
                             QFrame,
                             QGroupBox,
                             QLineEdit,
                             QMessageBox,
                             QPlainTextEdit,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGraphicsDropShadowEffect,
                             QGraphicsOpacityEffect,
                             QSizePolicy
                             )
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, os
from collections import deque
from pathlib import Path


sys.path.append(r'.')
from gui import choose_a_plane_menu
from gui import settings_menu
sys.path.append(r'..')
from sounds.sounds import main_menu_music
song = r'sounds/music/main_menu_music.flac'



# Modify this variable to receive dynamically value from the JSON file
global current_gold, current_rank
current_gold = 100
current_rank = "Airman"

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Py Planes")
        self.setWindowIcon(QIcon(r'images/menu/plane_icon.jpg'))
        self.setGeometry(200, 150, 600, 500)
        self.setMaximumWidth(600)
        self.setMaximumHeight(500)

        """BACKGROUND PICTURE GROUPBOX"""
        bg_image_groupbox = QGroupBox()
        bg_image_groupbox.setProperty("class", "background")
        
        """ADD CUSTOM FONTS"""
        font = QFontDatabase.addApplicationFont(r'fonts/American Captain.ttf')
        if font < 0:
            print('Error loading fonts!')
        fonts = QFontDatabase.applicationFontFamilies(font)
        
        """DISPLAY THE USER'S GOLD"""
        gold_layout = QVBoxLayout()
        # gold_layout.addStretch()
        gold_layout.addSpacing(0)
        
        gold_horizontal_layout = QHBoxLayout()
        
        gold_icon = QLabel()
        gold_icon.setFixedSize(50, 50)
        gold_icon.setScaledContents(True)
        gold_icon.setPixmap(QPixmap(r"images/menu/gold_icon.png"))
        
        gold_value = QLabel()
        gold_value.setText(f"{current_gold} Gold")
        gold_value.setFont(QFont(fonts[0], 20))
        
        gold_horizontal_layout.addWidget(gold_icon)
        gold_horizontal_layout.addWidget(gold_value)
        
        gold_layout.addLayout(gold_horizontal_layout)
        
        """DISPLAY USER RANK"""
        rank_layout = QVBoxLayout()
        # rank_layout.addStretch()
        # rank_layout.addSpacing(10)
        
        rank_horizontal_layout = QHBoxLayout()
        
        # Read the rank dynamically from the JSON file
        rank_icon = QLabel()
        rank_icon.setFixedSize(50, 50)
        rank_icon.setScaledContents(True)
        rank_icon.setPixmap(QPixmap(r"images/ranks/airman_rank.png"))
        
        rank_value = QLabel()
        rank_value.setText(f"{current_rank}")
        rank_value.setFont(QFont(fonts[0], 20))
        
        rank_horizontal_layout.addWidget(rank_icon)
        rank_horizontal_layout.addWidget(rank_value)
        
        rank_layout.addLayout(rank_horizontal_layout)
        rank_layout.addStretch()
        
        """BUTTONS LAYOUT"""
        main_buttons_layout = QVBoxLayout()
        main_buttons_layout.setAlignment(Qt.AlignCenter)
        buttons = deque(["Start Game", "Settings", "Credits", "Quit Game"])
        
        for i in range(4):
            current_button = QPushButton()
            current_button.setProperty("class", "menu_button")
            button = buttons.popleft()
            current_button.setText(button)
            current_button.setFont(QFont(fonts[0], 20))
            current_button.setFixedSize(200, 50)
            if button == "Start Game":
                current_button.clicked.connect(lambda: self.start_game_button_func())
            if button == "Settings":
                current_button.clicked.connect(lambda: open_settings_menu())
            if button == "Credits":
                pass
            if button == "Quit Game":
                current_button.clicked.connect(lambda: app.quit())
                
            
            main_buttons_layout.addWidget(current_button)
        main_buttons_layout.addStretch(10)
        main_buttons_layout.addSpacing(20)

        main_menu_layout = QVBoxLayout()
        # main_menu_layout.addStretch()
        # main_menu_layout.addSpacing(0)
        main_menu_layout.addLayout(gold_layout)
        main_menu_layout.addLayout(rank_layout)
        main_menu_layout.addLayout(main_buttons_layout)
        bg_image_groupbox.setLayout(main_menu_layout)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(bg_image_groupbox)
        self.setLayout(main_layout)
        self.show()

    def start_game_button_func(self):
        choose_a_plane_menu.start_plane_menu_window()
        self.hide()


def init_app():
    global app
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('gui/main_menu.qss').read_text())
    global main_window
    main_window = MainMenu()
    main_window.show()
    # app.exec() # Keep this line commented for now. The app is initiated by the main_menu_music function
    main_menu_music(song, app)
    
def open_main_menu():
    main_window.show()
    
global open_settings_menu
def open_settings_menu():
    main_window.hide()
    settings_menu.open_settings()
    