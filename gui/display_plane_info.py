from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QPlainTextEdit, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *



def plane_info_return_groupbox(curr_plane_stats):
    
    
    """ADD CUSTOM FONTS"""
    font = QFontDatabase.addApplicationFont(r'fonts/American Captain.ttf')
    if font < 0:
        print('Error loading fonts!')
    fonts = QFontDatabase.applicationFontFamilies(font)
    
    print(curr_plane_stats)
    curr_plane_info_groupbox = QGroupBox()
    curr_plane_info_groupbox.setFixedWidth(300)
    curr_plane_info_groupbox.setFixedHeight(200)

    plane_info_layout = QVBoxLayout()
    # plane_info_layout.addStretch()
    # plane_info_layout.addSpacing(0)

    for i in curr_plane_stats:
        current_label = QLabel()
        current_label.setText(str(i))
        current_label.setFont(QFont(fonts[0], 10))
        
        
        plane_info_layout.addWidget(current_label)

    curr_plane_info_groupbox.setLayout(plane_info_layout)
    curr_plane_info_groupbox.setContentsMargins(0,0,0,0)

    return curr_plane_info_groupbox

