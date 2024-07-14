#!/bin/bash

PROJECT_DIR="/root/lms-portfolio"

cd $PROJECT_DIR
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

systemctl deamon-reload
systemctl restart myportfolio