import pathlib

import aqt


class Key:
    ASSETS = "assets"
    MAIN_CSS = "main.css"
    REVIEW = "review"


class Defaults:
    NAME = "AnkiPassFail"
    NAME_INTERNAL = (
        aqt.mw.addonManager.addonFromModule(__name__) if aqt.mw is not None else NAME
    )

    # [/absolute/path/to/addon]
    ADDON_ROOT = pathlib.Path(__file__).parent.parent

    # Add-ons may expose their own web assets by utilizing
    # aqt.addons.AddonManager.setWebExports(). Web exports registered
    # in this manner may then be accessed under the `/_addons` subpath.
    #
    # via https://github.com/ankitects/anki/blob/main/qt/aqt/webview.py
    WEB_ROOT = pathlib.Path("/_addons")
    ASSET_MAIN_CSS = WEB_ROOT / NAME_INTERNAL / Key.ASSETS / Key.MAIN_CSS


class ConfigError(Exception):
    pass
