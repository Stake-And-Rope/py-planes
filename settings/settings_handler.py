#!/usr/bin/python3

import json


def read_file(filename):
    with open(filename, "r") as file:
        return json.load(file)


# def save_file(filename):
#     with open(filename, "w") as file:
#         return dump(file)


def get_plane_settings():
    """
    :return:  dictionary with the plane settings
    """
    pass


def get_game_settings(file):
    """
    :return: dictionary with the game settings
    """
    return read_file(file)


def overwrite_game_settings(**kwargs):
    pass




# def overwrite_settings(self, **kwargs):
#     kwargs = {k.lower(): v for k, v in kwargs.items()}
#
#     new_settings = {}
#     for key, value in self.default_settings.items():
#         if key in new_settings:
#             continue
#
#         if kwargs.get(key):
#             settings_value = kwargs.get(key)
#
#         # elif not kwargs.get(key):
#         else:
#             settings_value = value
#
#         new_settings[key] = settings_value
#
#     with open(self.file_name, "w") as json_file:
#         dump(new_settings, json_file, indent=4)
