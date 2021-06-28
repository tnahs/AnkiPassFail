#! /bin/zsh

root=${0:A:h:h}

black "$root/addon" && \
isort "$root/addon" && \
zsh "$root/scripts/bundle.sh"