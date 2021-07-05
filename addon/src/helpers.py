import pathlib

import aqt


class ConfigError(Exception):
    pass


class Key:
    ASSETS = "assets"
    MAIN_CSS = "main.css"
    REVIEW = "review"
    SRC = "src"


class Defaults:
    NAME = "AnkiPassFail"
    NAME_INTERNAL = (
        aqt.mw.addonManager.addonFromModule(__name__) if aqt.mw is not None else NAME
    )

    # [/absolute/path/to/addon]
    ADDON_ROOT = pathlib.Path(__file__).parent.parent

    # /_addons
    WEB_ROOT = pathlib.Path("/_addons")
    # /_addons/[addon-name]/src/assets/main.css
    MAIN_CSS = WEB_ROOT / NAME_INTERNAL / Key.SRC / Key.ASSETS / Key.MAIN_CSS
