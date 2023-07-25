from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout


def plane_info_return_groupbox(curr_plane_name):
    curr_plane_info_groupbox = QGroupBox()
    curr_plane_info_groupbox.setFixedWidth(300)
    curr_plane_info_groupbox.setFixedHeight(120)

    plane_info_layout = QVBoxLayout()

    test_button = QPushButton()
    test_button.setText(curr_plane_name)

    plane_info_layout.addWidget(test_button)

    curr_plane_info_groupbox.setLayout(plane_info_layout)

    return curr_plane_info_groupbox