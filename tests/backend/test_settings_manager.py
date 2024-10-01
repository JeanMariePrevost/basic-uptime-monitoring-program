import os
from src.backend.settings_manager import get_value, set_value


def test_get_value():
    # assert the config file exists
    assert os.path.exists("configs/app_config.json")

    assert get_value("logging_level") is not None
    assert get_value("non_existing_key") is None


def test_set_value():
    # assert the config file exists
    assert os.path.exists("configs/app_config.json")

    original_value = get_value("logging_level")
    assert get_value("logging_level") is not None

    # set the value
    set_value("logging_level", "test_value")
    assert get_value("logging_level") == "test_value"

    # set the value back to original
    set_value("logging_level", original_value)
    assert get_value("logging_level") == original_value
