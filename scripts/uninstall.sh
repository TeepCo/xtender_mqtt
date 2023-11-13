#!/bin/bash
WORKDIR="$(dirname "$(realpath "$0")")"
REMOVEDIR=$(realpath $WORKDIR/..)
SERVICENAME=xtender_mqtt.service
SERVICE_REMOVE_NAME="service_remove.sh"
if [ "$(id -u)" -ne 0 ]; then
        echo 'This command must be run by root.' >&2
        exit 1
fi

read -p "Service ${SERVICENAME} will be stopped,disabled and removed and all the files in the ${REMOVEDIR}/ directory will be deleted. Do you wish to continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

/bin/bash "$WORKDIR/$SERVICE_REMOVE_NAME" > /dev/null

if [ $? ];then
  echo "Service removed successfully."
fi
rm -rf  "${REMOVEDIR}"

if [ $? ]; then
  echo "Script has been successfully uninstalled."
fi
