#! /bin/zsh

# https://unix.stackexchange.com/a/115431
root=${0:A:h:h}

ln -s \
    "$root/addon" \
    "$HOME/Library/Application Support/Anki2/addons21/dev-anki-pass-fail"
