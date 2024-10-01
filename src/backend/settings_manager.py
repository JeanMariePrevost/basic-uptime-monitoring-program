"""
Central point for reading and writing application settings.
It reads the settings from the app_config.json file and provides a way to get and set the settings.
"""

import json

_cached_app_config = None


def _read_configs_file():
    with open("configs/app_config.json", "r") as f:
        return json.load(f)


def _get_app_configs():
    global _cached_app_config
    if _cached_app_config is not None:
        return _cached_app_config
    else:
        _cached_app_config = _read_configs_file()
        return _cached_app_config


def get_value(key, default=None):
    return _get_app_configs().get(key, default)


def set_value(key, value):
    _get_app_configs()[key] = value
    with open("configs/app_config.json", "w") as f:
        json.dump(_cached_app_config, f, indent=4)
