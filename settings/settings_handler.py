from json import (load,
                  dump
                  )


class SettingsHandler:

    @property
    def file_name(self):
        return "settings.json"

    @property
    def default_settings(self):
        """
        If we come up with another setting idea, just add it here.
        """
        return {
            "fps": 60,
            "music": 100,
            "sound": 100,
        }

    def get_json_data(self):
        """
        returns the settings if there is a file already,
        otherwise it returns the default settings from the @property
        """

        try:
            with open(self.file_name, "r") as settings:
                return load(settings)

        except FileNotFoundError as error:
            return self.default_settings

    def overwrite_settings(self, **kwargs):
        """
        :param kwargs:  you can pass the new settings like this ->  fps=30, sound=80  OR  **{"fps": 30, "sound: 80}
        just pass the new values you want to overwrite, or pass all of them.

        converted the kwargs keys to lowercase to avoid duplicated keys such as -> [fpS, fps, FPS] and so on

        keys which are different from the @property ones will be ignored

        overwriting the whole file with the new settings.
        """

        kwargs = {k.lower(): v for k, v in kwargs.items()}

        new_settings = {}
        for key, value in self.default_settings.items():
            if key in new_settings:
                continue

            if kwargs.get(key):
                settings_value = kwargs.get(key)

            # elif not kwargs.get(key):
            else:
                settings_value = value

            new_settings[key] = settings_value

        with open(self.file_name, "w") as json_file:
            dump(new_settings, json_file, indent=4)



# settings = SettingsHandler()

# get from file
# data_from_json = settings.get_json_data()


# overwrite the file with new settings
# settings.overwrite_settings(sound=30, fps=65)


# another way of doing it
# settings.overwrite_settings(**{"sound": 30, "music": 80, "fps": 75})

