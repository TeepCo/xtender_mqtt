#!/bin/bash
SCRIPT_DIR="$(dirname "$(realpath "$0")")"

WORK_DIR="${SCRIPT_DIR}/../scom/src/sino/scom"


if [ -d "scom" ]; then
  if [ -n "$(ls -A "scom")" ]; then
    read -p "Directory scom exists and contains files. If you proceed with the installation, all the files will be overwritten. Do you wish to continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
  fi
  rm -Rf scom

fi

curl -L -O https://github.com/hesso-valais/scom/archive/refs/heads/master.zip

unzip master.zip
rm master.zip
mv "${SCRIPT_DIR}"/../scom-master/ "${SCRIPT_DIR}"/../scom/
rm -rf scom-master
cp -f "${SCRIPT_DIR}"/../src/xtender.py "${SCRIPT_DIR}"/../scom/src/sino/scom/device/xtender.py
cp -f "${SCRIPT_DIR}"/../scripts/build-scomlib.sh "${SCRIPT_DIR}"/../scom/scripts/
chmod u+x "${SCRIPT_DIR}"/../scom/scripts/*
export PIPENV_VENV_IN_PROJECT=1
./scom/scripts/build-sdist.sh
./scom/scripts/build-scomlib.sh

# mv -f $(find scom/ | grep baseframe.*so) "${WORK_DIR}//"
# mv -f $(find scom/ | grep property.*so) "${WORK_DIR}//"

