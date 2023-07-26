#!/usr/bin/python3

import json
import os


def get_relative_path_to_settings():
    target_directory = os.path.join(os.path.dirname(__file__), '..', 'settings')
    current_directory = os.getcwd()
    relative_path = os.path.relpath(target_directory, start=current_directory)

    return relative_path


def read_file(path: str):
    with open(path, "r") as file:
        return json.load(file)


def save_file(path_to_file, new_data: dict):
    with open(path_to_file, "w") as file:
        return json.dump(new_data, file, indent=4)


def get_game_settings():
    """
    :return: dictionary with the game settings information
    """

    path_to_file = f"{get_relative_path_to_settings()}\game_settings.json"
    return read_file(path_to_file)


def get_planes_settings():
    """
    :return: dictionary with the planes settings information
    """

    path_to_file = f"{get_relative_path_to_settings()}\planes_settings.json"
    return read_file(path_to_file)


def get_user_settings():
    """
    :return: dictionary with the user settings information
    """

    path_to_file = f"{get_relative_path_to_settings()}\\user_settings.json"
    return read_file(path_to_file)


def overwrite_game_settings(**new_settings):
    """
    :param new_settings: key-value pairs containing new game settings
    if bad key is passed, KeyError will be raised

    """
    new_settings = {k.lower(): v for k, v in new_settings.items()}

    data = get_game_settings()

    for key in new_settings:
        if not data.get(key):
            raise KeyError(f"{key} is not a correct key.For more information, open settings/game_settings.json")

        data[key] = new_settings[key]

    save_file(f"{get_relative_path_to_settings()}\game_settings.json",
              data
              )


def overwrite_user_settings(**new_settings):
    """
    :param new_settings: key-value pairs containing new game settings
    if bad key is passed, KeyError will be raised

    """
    new_settings = {k.lower(): v for k, v in new_settings.items()}

    data = get_user_settings()

    for key in new_settings:
        if not data.get(key):
            raise KeyError(f"{key} is not a correct key.For more information, open settings/user_settings.json")

        data[key] = new_settings[key]

    save_file(f"{get_relative_path_to_settings()}\\user_settings.json",
              data
              )
