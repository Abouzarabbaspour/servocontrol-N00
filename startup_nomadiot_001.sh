#!/bin/sh
# Change directory to the location of the script
cd "$(dirname "$0")"

# Start the Bluetooth agent and configure Bluetooth settings
bluetoothctl system-alias nomadiot_001
bluetoothctl power off
bluetoothctl power on
bluetoothctl discoverable on

# Navigate to the specified directory
cd /home/servocontrol-N00

# Pull the latest changes from Git repository
git pull

# Start the Bluetooth agent with specified capabilities and PIN
bt-agent --capability=NoInputNoOutput -p pins &

# Start the servo control script
python bt_servo_control.py
