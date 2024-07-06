#!/bin/bash

PROJECT_DIR="/root/lms-portfolio"

tmux kill-session -t portfolio
cd $PROJECT_DIR
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

tmux new-session -d -s portfolio "cd $PROJECT_DIR && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"
