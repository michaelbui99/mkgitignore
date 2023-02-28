#!/bin/bash
# TODO: Update this and add bashrc setup
echo "Setting up mkgitignore..."

SCRIPTS_PATH="$HOME/Scripts"
WORKING_DIR=$(pwd)

if [[ ! -d "$SCRIPTS_PATH" ]];then
    echo "Creating new Scripts folder..."
    cd "$HOME" && mkdir Scripts
fi

cd $SCRIPTS_PATH

if [[ -d "$SCRIPTS_PATH/mkgitignore" ]]; then
    echo "Removing existing mkgitignore..."
    rm -rf ./mkgitignore
fi

echo "Cloning mkgitignore..."
git clone https://github.com/michaelbui99/mkgitignore.git

cd mkgitignore
pip install -r requirements.txt