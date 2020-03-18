import pathlib
from typing import Any, Callable, List, Optional, Tuple

import aqt


class AnkiPassFail:

    name = "AnkiPassFail"

    main_root = pathlib.Path(__file__).parent.parent

    # Add-ons may expose their own web assets by utilizing
    # aqt.addons.AddonManager.setWebExports(). Web exports registered
    # in this manner may then be accessed under the `/_addons` subpath.
    #
    # via https://github.com/ankitects/anki/blob/3d7f643184cf9625293a397e1a73109659b77734/qt/aqt/webview.py#L132
    web_export_root = pathlib.Path("/_addons")
    main_css_path = web_export_root / main_root.name / "src" / "web" / "main.css"

    def setup(self) -> None:
        def hook__append_shortcuts(
            state: str, shortcuts: List[Tuple[str, Callable]]
        ) -> None:

            if state != "review":
                return

            """
            class Reviewer:
                ...
                def _shortcutKeys():
                    ...
                    ("1", lambda: self._answerCard(1)),  # Again
                    ("2", lambda: self._answerCard(2)),  # Easy
                    ("3", lambda: self._answerCard(3)),  # Good
                    ("4", lambda: self._answerCard(4)),  # Hard
                    ...

            via https://github.com/ankitects/anki/blob/31347ffbaa2b4caceccd3a694b3834841595867c/qt/aqt/reviewer.py#L275
            """

            to_remove: List[int] = []

            for index, shortcut in enumerate(shortcuts):

                try:
                    key_sequence = shortcut[0]
                except IndexError:
                    continue

                if key_sequence in ["2", "4"]:
                    to_remove.append(index)

            for index in sorted(to_remove, reverse=True):
                del shortcuts[index]

        aqt.gui_hooks.state_shortcuts_will_change.append(hook__append_shortcuts)

        def hook__append_css(
            web_content: aqt.webview.WebContent, context: Optional[Any]
        ) -> None:

            # Add-ons may expose their own web assets by utilizing
            # aqt.addons.AddonManager.setWebExports(). Web exports registered
            # in this manner may then be accessed under the `/_addons` subpath.
            #
            # E.g., to allow access to a `my-addon.js` and `my-addon.css`
            # residing in a "web" subfolder in your add-on package, first
            # register the corresponding web export:
            #
            #   > from aqt import mw
            #   > mw.addonManager.setWebExports(__name__, r"web/.*(css|js)")
            #
            # via https://github.com/ankitects/anki/blob/3d7f643184cf9625293a397e1a73109659b77734/qt/aqt/webview.py#L132
            aqt.mw.addonManager.setWebExports(__name__, r".+\.css")

            web_content.css.append(str(self.main_css_path))

        aqt.gui_hooks.webview_will_set_content.append(hook__append_css)
