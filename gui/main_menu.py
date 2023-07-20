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
                             )
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from collections import deque
from pathlib import Path

sys.path.append(r'..')


# Modify this variable to receive dynamically value from the JSON file
global current_gold, current_rank
current_gold = 100
current_rank = "Airman"

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Py Planes")
        self.setWindowIcon(QIcon(r'../images/menu/plane_icon.jpg'))
        self.setGeometry(200, 150, 600, 500)
        self.setMaximumWidth(600)
        self.setMaximumHeight(500)
        
        
        """ADD CUSTOM FONTS"""
        font = QFontDatabase.addApplicationFont(r'../fonts/American Captain.ttf')
        if font < 0:
            print('Error loading fonts!')
        fonts = QFontDatabase.applicationFontFamilies(font)
        
        """DISPLAY THE USER'S GOLD"""
        gold_layout = QVBoxLayout()
        gold_layout.addStretch()
        gold_layout.addSpacing(2)
        
        gold_horizontal_layout = QHBoxLayout()
        
        gold_icon = QLabel()
        gold_icon.setFixedSize(64, 64)
        gold_icon.setPixmap(QPixmap(r"../images/menu/gold_icon.png"))
        
        gold_value = QLabel()
        gold_value.setText(f"{current_gold} Gold")
        gold_value.setFont(QFont(fonts[0], 20))
        
        gold_horizontal_layout.addWidget(gold_icon)
        gold_horizontal_layout.addWidget(gold_value)
        
        gold_layout.addLayout(gold_horizontal_layout)
        
        """DISPLAY USER RANK"""
        rank_layout = QVBoxLayout()
        rank_layout.addStretch()
        rank_layout.addSpacing(10)
        
        rank_horizontal_layout = QHBoxLayout()
        
        # Read the rank dynamically from the JSON file
        rank_icon = QLabel()
        rank_icon.setFixedSize(64, 64)
        rank_icon.setPixmap(QPixmap(r"../images/ranks/airman_rank.png"))
        
        rank_value = QLabel()
        rank_value.setText(f"{current_rank}")
        rank_value.setFont(QFont(fonts[0], 20))
        
        rank_horizontal_layout.addWidget(rank_icon)
        rank_horizontal_layout.addWidget(rank_value)
        
        rank_layout.addLayout(rank_horizontal_layout)
        
        
        """BUTTONS LAYOUT"""
        main_buttons_layout = QVBoxLayout()
        main_buttons_layout.setAlignment(Qt.AlignCenter)
        buttons = deque(["Start Game", "Settings", "Credits", "Quit Game"])
        
        
        for i in range(4):
            current_button = QPushButton()
            current_button.setText(buttons.popleft())
            current_button.setFont(QFont(fonts[0], 20))
            current_button.setFixedSize(200, 50)
            
            main_buttons_layout.addWidget(current_button)
        
        
        main_layout = QVBoxLayout()
        main_layout.addStretch(2)
        main_layout.addSpacing(10)
        main_layout.addLayout(gold_layout)
        main_layout.addLayout(rank_layout)
        main_layout.addLayout(main_buttons_layout)
        self.setLayout(main_layout)
        self.show()
        


app = QApplication(sys.argv)
app.setStyleSheet(Path('main_menu.qss').read_text())
global main_window
main_window = MainMenu()
main_window.show()
app.exec()
