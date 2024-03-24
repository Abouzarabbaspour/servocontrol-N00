#!/bin/sh
# change directory to the location of the script
cd /home/servocontrol-N00
git pull

# Start the bluetooth agent
bluetoothctl system-alias nomadiot_001
bluetoothctl power off
bluetoothctl power on
bluetoothctl discoverable on
bt-agent --capability=NoInputNoOutput -p pins &

# Start the servo control script
python bt_servo_control.py