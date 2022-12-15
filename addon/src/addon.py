import pathlib
from typing import Callable

import aqt
import aqt.gui_hooks
import aqt.reviewer
import aqt.webview

from .helpers import Defaults, Key


class AnkiPassFail:
    def setup(self) -> None:
        """Regsiters the add-on's hooks to append its CSS and disable some reviewer
        shortcuts."""

        if aqt.mw is None:
            return

        # Add-ons may expose their own web assets by utilizing
        # aqt.addons.AddonManager.setWebExports(). Web exports registered in this manner
        # may then be accessed under the `/_addons` subpath.
        #
        # E.g., to allow access to a `my-addon.js` and `my-addon.css` residing in a
        # "web" subfolder in your add-on package, first register the corresponding web
        # export:
        #
        # > from aqt import mw
        # > mw.addonManager.setWebExports(__name__, r"web/.*(css|js)")

        aqt.mw.addonManager.setWebExports(
            __name__, str(pathlib.Path() / Key.SRC / Key.ASSETS / r".*\.css")
        )

        # The following functions are nested to prevent the need for declaring `self` as
        # the first argument in order to maintain the correct function signature while
        # still being able to access `self`.

        def hook__append_css(
            web_content: aqt.webview.WebContent, context: object
        ) -> None:
            """Disables the "Easy" and "Hard" buttons via CSS."""

            if not isinstance(context, aqt.reviewer.ReviewerBottomBar):
                return

            web_content.css.append(str(Defaults.MAIN_CSS))

        aqt.gui_hooks.webview_will_set_content.append(hook__append_css)

        def hook__disable_shortcuts(
            state: str, shortcuts: list[tuple[str, Callable]]
        ) -> None:
            """Disables the "Easy" and "Hard" hotkeys.

            The shortcuts are defined as a list of tuples with the first entry being the
            keystore and the second a callable.

            # ...
            ("1", lambda: self._answerCard(1)),  # Again
            ("2", lambda: self._answerCard(2)),  # Easy
            ("3", lambda: self._answerCard(3)),  # Good
            ("4", lambda: self._answerCard(4)),  # Hard
            # ...

            via https://github.com/ankitects/anki/blob/main/qt/aqt/reviewer.py
            """

            if state != Key.REVIEW:
                return

            disable: list[int] = []

            for index, (shortcut, _) in enumerate(shortcuts):
                if shortcut in ["2", "4"]:
                    disable.append(index)

            for index in sorted(disable, reverse=True):
                del shortcuts[index]

        aqt.gui_hooks.state_shortcuts_will_change.append(hook__disable_shortcuts)
