#!/bin/bash

echo "Creating venv, activating it, and then running pip install ."
python3 -m venv venv
source "./venv/bin/activate"
python3 -m pip install .

echo "Compiling into a binary using pyinstaller..."
python3 -m PyInstaller app/app.py --name can-data-logger --onefile --hidden-import can.interfaces.socketcan --clean

echo "Compilation succesful, cleaning up *.spec, build and venv..."
rm *.spec
rm -r build
rm -r venv
