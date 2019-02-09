#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    brew update
    brew upgrade python
else
    dpkg --add-architecture i386
    apt update
    apt install -y libc6:i386 libncurses5:i386 libstdc++6:i386 multiarch-support
fi

pip3 install conan conan_package_tools --upgrade

conan user
