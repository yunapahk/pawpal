#!/usr/bin/env bash

# exit when any command fails
set -o errexit

## Install dependencies via pip
pip3 install -r dependencies.txt

## Run migration just in case
python3 manage.py migrate