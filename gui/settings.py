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
import sys, os
from pathlib import Path

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
        
        """FPS CONTROLS"""
        fps_layout = QHBoxLayout()
        fps_layout.addStretch()
        fps_layout.addSpacing(10)
        fps_layout.setSpacing(150)
        
        fps_label = QLabel()
        fps_label.setText('FPS')
        fps_label.setFont(QFont(fonts[0], 20))
        # fps_label.setAlignment(Qt.AlignRight)
        
        fps_menu = QComboBox()
        fps_menu.addItems(["45", "60", "75"])
        fps_menu.setFont(QFont(fonts[0], 20))
        fps_menu.setFixedSize(70, 40)
        
        fps_layout.addWidget(fps_label)
        fps_layout.addWidget(fps_menu)
        # fps_layout.setAlignment(Qt.AlignCenter)
        fps_layout.addStretch()
        fps_layout.addSpacing(10)
        fps_layout.setSpacing(150)
        
        """MUSIC VOLUME CONTROLS"""
        music_vol_layout = QHBoxLayout()
        music_vol_layout.addStretch()
        music_vol_layout.addSpacing(20)
        music_vol_layout.setSpacing(97)
        
        music_vol_label = QLabel()
        music_vol_label.setText("Music Volume")
        music_vol_label.setFont(QFont(fonts[0], 20))
        music_vol_label.setAlignment(Qt.AlignCenter)
    
        music_vol_slider = QSlider(Qt.Horizontal)
        music_vol_slider.setTickInterval(20)
        music_vol_slider.setFocusPolicy(Qt.StrongFocus)
        music_vol_slider.setTickPosition(QSlider.TicksBothSides)
        music_vol_slider.setSingleStep(1)
        music_vol_slider.setFixedWidth(200)
        
        music_vol_layout.addWidget(music_vol_label)
        music_vol_layout.addWidget(music_vol_slider)
        music_vol_layout.setAlignment(Qt.AlignCenter)
        music_vol_layout.addStretch()
        music_vol_layout.addSpacing(20)
        music_vol_layout.setSpacing(97)
        
        """EFFECTS VOLUME CONTROLS"""
        effects_vol_layout = QHBoxLayout()
        effects_vol_layout.addStretch()
        effects_vol_layout.addSpacing(20)
        effects_vol_layout.setSpacing(80)
        
        effects_vol_label = QLabel()
        effects_vol_label.setText("Effects Volume")
        effects_vol_label.setFont(QFont(fonts[0], 20))
        effects_vol_label.setAlignment(Qt.AlignCenter)
        
        effects_vol_slider = QSlider(Qt.Horizontal)
        effects_vol_slider.setTickInterval(20)
        effects_vol_slider.setFocusPolicy(Qt.StrongFocus)
        effects_vol_slider.setTickPosition(QSlider.TicksBothSides)
        effects_vol_slider.setSingleStep(1)
        effects_vol_slider.setFixedWidth(200)
        
        effects_vol_layout.addWidget(effects_vol_label)
        effects_vol_layout.addWidget(effects_vol_slider)
        effects_vol_layout.setAlignment(Qt.AlignCenter)
        effects_vol_layout.addStretch()
        effects_vol_layout.addSpacing(20)
        
        
        main_layout = QVBoxLayout()
        main_layout.addStretch(0)
        main_layout.addSpacing(100)
        main_layout.addLayout(fps_layout)
        main_layout.addLayout(music_vol_layout)
        main_layout.addLayout(effects_vol_layout)
        main_layout.addStretch(0)
        main_layout.addSpacing(100)
        self.setLayout(main_layout)
        self.show()
        
        
        
app = QApplication(sys.argv)
app.setStyleSheet(Path('main_menu.qss').read_text())
global main_window
main_window = SettingsMenu()
main_window.show()
app.exec()