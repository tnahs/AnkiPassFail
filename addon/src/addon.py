import os
from typing import Callable, List, Tuple

import aqt
import aqt.gui_hooks
import aqt.reviewer
import aqt.webview

from .helpers import Defaults, Key


class AnkiPassFail:
    def setup(self) -> None:
        def hook__disable_shortcuts(
            state: str, shortcuts: List[Tuple[str, Callable]]
        ) -> None:

            if state != Key.REVIEW:
                return

            """
            class Reviewer:
                ...
                def _shortcutKeys():
                    ...
                    ("1", lambda: self._answerCard(1)),
                    ("2", lambda: self._answerCard(2)),
                    ("3", lambda: self._answerCard(3)),
                    ("4", lambda: self._answerCard(4)),
                    ...

            via https://github.com/ankitects/anki/blob/main/qt/aqt/reviewer.py
            """

            disable: List[int] = []

            for index, (shortcut, _) in enumerate(shortcuts):
                if shortcut in ["2", "4"]:
                    disable.append(index)

            for index in sorted(disable, reverse=True):
                del shortcuts[index]

        aqt.gui_hooks.state_shortcuts_will_change.append(hook__disable_shortcuts)

        def hook__append_css(
            web_content: aqt.webview.WebContent, context: object
        ) -> None:

            if not isinstance(context, aqt.reviewer.ReviewerBottomBar):
                return

            # Add-ons may expose their own web assets by utilizing
            # aqt.addons.AddonManager.setWebExports(). Web exports registered
            # in this manner may then be accessed under the `/_addons` subpath.
            #
            # E.g., to allow access to a `my-addon.js` and `my-addon.css` residing
            # in a "web" subfolder in your add-on package, first register the
            # corresponding web export:
            #
            # > from aqt import mw
            # > mw.addonManager.setWebExports(__name__, r"web/.*(css|js)")
            #
            # via https://github.com/ankitects/anki/blob/main/qt/aqt/webview.py

            aqt.mw.addonManager.setWebExports(  # type: ignore
                __name__, fr"{Key.SRC}{os.sep}{Key.ASSETS}{os.sep}.*\.css"
            )

            web_content.css.append(str(Defaults.MAIN_CSS))

        aqt.gui_hooks.webview_will_set_content.append(hook__append_css)
