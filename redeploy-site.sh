#!/bin/bash

PROJECT_DIR="/root/lms-portfolio"

cd $PROJECT_DIR
git fetch && git reset origin/main --hard
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build