#!/bin/zsh
eval "$(conda shell.bash hook)"
cd /home/ma/code/qtdesigner/PyQt-Fluent-Widgets/tools
conda activate qyqt
python designer.py
echo "fuck stupid Qt"
