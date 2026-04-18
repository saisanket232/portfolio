#!/usr/bin/env bash
set -o errexit
pip install -r portfolio_project/requirements.txt
python portfolio_project/manage.py collectstatic --noinput
python portfolio_project/manage.py migrate
