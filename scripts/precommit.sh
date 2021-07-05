#! /bin/zsh

root=${0:A:h:h}

black "$root/addon" \
&& isort "$root/addon" \
&& rm -f "$root/addon/meta.json" \
&& rm -f "$root/bundle/anki-pass-fail.ankiaddon" \
&& zsh "$root/scripts/bundle.sh"