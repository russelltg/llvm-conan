#!/bin/bash

set -xe

if [[ "$(uname -s)" == 'Darwin' ]]; then
    brew update || brew update
    brew outdated pyenv || brew upgrade pyenv
    brew install pyenv-virtualenv
    brew install cmake || true

    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi

    pyenv install 3.5
    pyenv virtualenv 3.5 conan
    pyenv rehash
    pyenv activate conan
fi

pip3 install conan_package_tools
conan user
