#!/bin/bash
XQ_USER=xtender_mqtt
WORKDIR="$(dirname "$(realpath "$0")")"
SERVICENAME=xtender_mqtt.service


if [ "$(id -u)" -ne 0 ]; then
        echo 'This command must be run by root.' >&2
        exit 1
fi

if [ -e "/etc/systemd/system/$SERVICENAME" ]; then
   read -rp "Service $SERVICENAME already exists. If you proceed, it will be overwritten. Do you want to continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
fi

echo "Under which user should the service run?"
echo "(1) New user '${XQ_USER} without home directory and shell access will be automatically created."
echo "(2) $(logname)"
echo "(3) root"
echo "(4) Other user"

CHOICE=0
while [ "$CHOICE" -lt 1 ] || [ "$CHOICE" -gt 4 ]
do
read -rp "Please enter 1-4: "  CHOICE
done

case $CHOICE in
  1)
    :;;
  2)
    XQ_USER=$(logname);;
  3)
    XQ_USER=root;;
  4)

    XQ_USER=""
    while [ -z "$XQ_USER" ]
    do
      read -rp "Please provide name of the user under which shall be the service ran: " XQ_USER
    done;;
  *)
    exit 1;;
esac


if ! id "$XQ_USER" > /dev/null 2>&1; then
  if ! adduser "$XQ_USER" --shell=/bin/false --no-create-home;then
    exit 1;
  fi
fi


cat > "/etc/systemd/system/$SERVICENAME" <<EOL
[Unit]
Description=Service for restarting xtender_mqtt program upon failure

[Service]
User=${XQ_USER}
Restart=always
RestartSec=10s
WorkingDirectory=${WORKDIR}
ExecStart=${WORKDIR}/run.sh

[Install]
WantedBy=multi-user.target
EOL
if [ !  $? ];then
  exit 1
fi


systemctl daemon-reload

if [ $? ];then
  echo "Service installed successfully. You can start it with 'systemctl start ${SERVICENAME}'. If you want it to be started automatically after reboot, you can enable it by 'systemctl enable ${SERVICENAME}'. Please make sure that the user '${XQ_USER}' has permissions for the serial port specified in the 'config/user_config.yaml file.'"
fi