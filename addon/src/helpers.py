import pathlib

import aqt


class Key:
    """A class defining re-usable strings."""

    ASSETS = "assets"
    MAIN_CSS = "main.css"
    REVIEW = "review"
    SRC = "src"


class Defaults:
    """A class defining all the add-on's default values."""

    NAME = "AnkiPassFail"

    # This name is used for properly setting the path to where the web exports
    # are located. Anki expects this to be: `/_addons/[addon-name]/`. Hard-
    # coding the name can result in missing web assets as depending on how the
    # add-on is installed, its name will be different.
    NAME_INTERNAL = (
        aqt.mw.addonManager.addonFromModule(__name__) if aqt.mw is not None else NAME
    )

    # [path-to-addon]
    ADDON_ROOT = pathlib.Path(__file__).parent.parent

    # /_addons
    WEB_ROOT = pathlib.Path("/_addons")
    # /_addons/[addon-name]/src/assets/main.css
    MAIN_CSS = WEB_ROOT / NAME_INTERNAL / Key.SRC / Key.ASSETS / Key.MAIN_CSS
