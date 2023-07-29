#!/usr/bin/python3

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
import sys, os
from pathlib import Path

sys.path.append(r'..')
from settings import settings_handler

# song = r'sounds/music/main_menu_music.flac'

"""PLAY THE BACKGROUND MUSIC"""
def main_menu_music(music, app):
    us = settings_handler.get_game_settings()
    
    player = QMediaPlayer()

    music = os.path.join(os.getcwd(), music)
    bg_playlist = QMediaPlaylist()
    url = QUrl.fromLocalFile(music)
    bg_playlist.addMedia(QMediaContent(url))
    player.setPlaylist(bg_playlist)
    bg_playlist.setPlaybackMode(QMediaPlaylist.Loop)

    
    player.setVolume(int(us.get("music")))
    player.play()
    app.exec()

# main_menu_music()
