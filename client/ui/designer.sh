#!/bin/zsh
eval "$(conda shell.bash hook)"
cd /home/ma/code/qtdesigner/PyQt-Fluent-Widgets
conda activate qyqt
python ./tools/designer.py
echo "fuck stupid Qt"
