#!/bin/bash
SERVICENAME=xtender_mqtt.service

if [ "$(id -u)" -ne 0 ]; then
        echo 'This command must be run by root.' >&2
        exit 1
fi

if [ -e "/etc/systemd/system/$SERVICENAME" ]; then
  systemctl stop $SERVICENAME
  systemctl disable $SERVICENAME
  rm "/etc/systemd/system/$SERVICENAME"
  if [ $? ];then
    echo "Service successfully removed."
  fi
else
  echo "Service is not installed."
fi
