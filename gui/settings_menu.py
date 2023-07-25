#!/usr/bin/python3

"""IMPORT PyQt5 ENGINE"""
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QGridLayout,
                             QLabel,
                             QFrame,
                             QSlider,
                             QGroupBox,
                             QLineEdit,
                             QMessageBox,
                             QComboBox,
                             QPlainTextEdit,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGraphicsDropShadowEffect,
                             QGraphicsOpacityEffect,
                             )
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, os, json
from pathlib import Path

sys.path.append('..')
from settings import settings_handler
gs = settings_handler.get_game_settings('../settings/game_settings.json')


class SettingsMenu(QWidget):
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
        
        """MAIN HORIZONTAL LAYOUT"""
        main_horizontal_layout = QHBoxLayout()
        main_horizontal_layout.addStretch()
        main_horizontal_layout.addSpacing(-250)
        # main_horizontal_layout.setAlignment(Qt.AlignCenter)
        
        """LEFT VERTICAL LAYOUT"""
        left_vertrical_layout = QVBoxLayout()
        left_vertrical_layout.setAlignment(Qt.AlignCenter)
        
        fps_label = QLabel()
        fps_label.setText('FPS')
        fps_label.setFont(QFont(fonts[0], 20))
        fps_label.setAlignment(Qt.AlignCenter)    
        
        music_vol_label = QLabel()
        music_vol_label.setText("Music Volume")
        music_vol_label.setFont(QFont(fonts[0], 20))
        music_vol_label.setAlignment(Qt.AlignCenter)        
        
        effects_vol_label = QLabel()
        effects_vol_label.setText("Effects Volume")
        effects_vol_label.setFont(QFont(fonts[0], 20))
        effects_vol_label.setAlignment(Qt.AlignCenter)        
        
        user_name_label = QLabel()
        user_name_label.setAlignment(Qt.AlignCenter)
        user_name_label.setText("Username")
        user_name_label.setFont(QFont(fonts[0], 20))
        
        left_vertrical_layout.addWidget(fps_label)
        left_vertrical_layout.addWidget(music_vol_label)
        left_vertrical_layout.addWidget(effects_vol_label)
        left_vertrical_layout.addWidget(user_name_label)
        
        """RIGHT VERTICAL LAYOUT"""
        right_vertrical_layout = QVBoxLayout()
        right_vertrical_layout.setAlignment(Qt.AlignCenter)
        
        fps_menu = QComboBox()
        fps_menu.addItems(["45", "60", "75"])
        fps_menu.setFont(QFont(fonts[0], 18))
        fps_menu.setFixedSize(70, 30)
        fps_menu.setCurrentText(gs.get('fps'))

        
        music_vol_slider = QSlider(Qt.Horizontal)
        # music_vol_slider.setValue()
        music_vol_slider.setTickInterval(20)
        music_vol_slider.setFocusPolicy(Qt.StrongFocus)
        music_vol_slider.setTickPosition(QSlider.TicksBothSides)
        music_vol_slider.setSingleStep(1)
        music_vol_slider.setFixedWidth(200)
        # print(music_vol_slider.value())

        effects_vol_slider = QSlider(Qt.Horizontal)
        effects_vol_slider.setTickInterval(20)
        effects_vol_slider.setFocusPolicy(Qt.StrongFocus)
        effects_vol_slider.setTickPosition(QSlider.TicksBothSides)
        effects_vol_slider.setSingleStep(1)
        effects_vol_slider.setFixedWidth(200)

        user_name_textbox = QLineEdit()
        # user_name_textbox.setText()
        user_name_textbox.setFont(QFont(fonts[0], 18))
        user_name_textbox.setFixedSize(200, 30)
        user_name_textbox.setAlignment(Qt.AlignCenter)

        right_vertrical_layout.addWidget(fps_menu)
        right_vertrical_layout.addWidget(music_vol_slider)
        right_vertrical_layout.addWidget(effects_vol_slider)
        right_vertrical_layout.addWidget(user_name_textbox)
        
        main_horizontal_layout.addLayout(left_vertrical_layout)
        main_horizontal_layout.addLayout(right_vertrical_layout)
        
        
        """BUTTONS LAYOUT"""
        main_buttons_layout = QVBoxLayout()
        main_buttons_layout.addStretch()
        main_buttons_layout.addSpacing(10)
        main_buttons_layout.setAlignment(Qt.AlignCenter)
        
        save_settings_button = QPushButton()
        save_settings_button.setText("Save Settings")
        save_settings_button.setFont(QFont(fonts[0], 18))
        save_settings_button.setFixedSize(300, 50)
        
        back_button = QPushButton()
        back_button.setText("Back to Main Menu")
        back_button.setFont(QFont(fonts[0], 18))
        back_button.setFixedSize(300, 50)
        
        main_buttons_layout.addWidget(save_settings_button)
        main_buttons_layout.addWidget(back_button)
                
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addSpacing(20)
        # main_layout.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(main_horizontal_layout)
        main_layout.addLayout(main_buttons_layout)
        self.setLayout(main_layout)
        self.show()
        
        
        
app = QApplication(sys.argv)
app.setStyleSheet(Path('main_menu.qss').read_text())
global main_window
main_window = SettingsMenu()
main_window.show()
app.exec()