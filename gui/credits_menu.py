#!/usr/bin/python3

"""IMPORT PyQt5 ENGINE"""
from PyQt5.QtWidgets import (QWidget,
                             QPushButton,
                             QLabel,
                             QGroupBox,
                             QVBoxLayout,
                             QGraphicsDropShadowEffect,
                             QTextEdit,
                             )
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, webbrowser
sys.path.append(r'.')
from gui import main_menu
sys.path.append(r'..')



class CreditsMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Py Planes")
        self.setWindowIcon(QIcon(r'images/menu/plane_icon.jpg'))
        self.setGeometry(200, 150, 600, 500)
        self.setMaximumWidth(600)
        self.setMaximumHeight(500)
        
        
        """CREATE SHADOW EFFECTS"""
        title_shadow = QGraphicsDropShadowEffect()
        title_shadow.setBlurRadius(10)
        title_shadow.setOffset(2, 5)
        title_shadow.setColor(QColor(0, 0, 0))
        
        description_shadow = QGraphicsDropShadowEffect()
        description_shadow.setBlurRadius(2)
        description_shadow.setOffset(2, 3)
        description_shadow.setColor(QColor(200, 8, 8))
        
        """ADD CUSTOM FONTS"""
        font = QFontDatabase.addApplicationFont(r'fonts/American Captain.ttf')
        if font < 0:
            print('Error loading fonts!')
        fonts = QFontDatabase.applicationFontFamilies(font)
        
        """BACKGROUND PICTURE GROUPBOX"""
        bg_image_groupbox = QGroupBox()
        bg_image_groupbox.setProperty("class", "credits_background")
        
        """TITLE LAYOUT"""
        title_layout = QVBoxLayout()
        title_layout.setSpacing(2)
        
        title_area = QLabel()
        title_area.setText("Py-Planes")
        title_area.setProperty("class", "title_area")
        title_area.setFont(QFont(fonts[0], 30))
        title_area.setFixedSize(300, 50)
        title_area.setAlignment(Qt.AlignCenter)
        title_area.setGraphicsEffect(title_shadow)

        version_area = QLabel()
        version_area.setText("Version 1.0")
        version_area.setProperty("class", "title_area")
        version_area.setFont(QFont(fonts[0], 15))
        version_area.setAlignment(Qt.AlignCenter)
        
        title_layout.addWidget(title_area)
        title_layout.addWidget(version_area)
        title_layout.setAlignment(Qt.AlignCenter)

        """DESCRIPTION LAYOUT"""
        description_layout = QVBoxLayout()
        description_layout.addStretch(10)
        
        description_area = QTextEdit()
        description_area.setProperty("class", "description_area")
        description_area.setText("Python game written in Qt Framework and PyGame")
        description_area.setFont(QFont(fonts[0], 18))
        description_area.setAlignment(Qt.AlignCenter)
        description_area.setDisabled(True)
        description_area.viewport().setAutoFillBackground(False)
        description_area.setGraphicsEffect(description_shadow)
        
        description_layout.addWidget(description_area)
        
        
        """INFO LAYOUT"""
        info_layout = QVBoxLayout()
        
        github_button = QPushButton()
        github_button.setProperty("class", "github_button")
        github_button.setText("GitHub Project")
        github_button.setFont(QFont(fonts[0], 15))
        github_button.setFixedSize(150, 25)
        github_button.clicked.connect(lambda: open_webbrowser())
        
        info_layout.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(github_button)
        
        """MAIN BUTTONS"""
        buttons_layout = QVBoxLayout()
        buttons_layout.setAlignment(Qt.AlignCenter)
        
        back_button = QPushButton()
        back_button.setText("main menu")
        back_button.setFont(QFont(fonts[0], 20))
        back_button.setProperty("class", "menu_button")
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(lambda: open_main_menu())
        
        buttons_layout.addWidget(back_button)    
        
        main_credits_layout = QVBoxLayout()
        main_credits_layout.addLayout(title_layout)
        main_credits_layout.addLayout(description_layout)
        main_credits_layout.addLayout(info_layout)
        main_credits_layout.addLayout(buttons_layout)    
        
        bg_image_groupbox.setLayout(main_credits_layout)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(bg_image_groupbox)
        self.setLayout(main_layout)
        self.show()
        
        
        
        def open_webbrowser():
            # if you want please remember to check its valid url or not
            url = str('https://github.com/Stake-And-Rope/py-planes')
            webbrowser.open(url) 


def open_credits():
    global credits_window
    credits_window = CreditsMenu()
    credits_window.show()
    
def open_main_menu():
    credits_window.hide()
    main_menu.open_main_menu()