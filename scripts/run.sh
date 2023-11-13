#!/bin/bash

SCRIPT_DIR="$(dirname "$(realpath "$0")")"

cd $SCRIPT_DIR/../scom

pipenv run python ../src/xtender_mqtt.py
