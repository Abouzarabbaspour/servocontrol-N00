#!/bin/sh
# Change directory to the location of the script
cd "$(dirname "$0")"

# Start the Bluetooth agent and configure Bluetooth settings
echo "Starting Bluetooth agent..."
echo "Configuring Bluetooth settings..."
bluetoothctl system-alias nomadiot_001
echo "Powering off Bluetooth..."
bluetoothctl power off
echo "Powering on Bluetooth..."
bluetoothctl power on
echo "Setting device to discoverable..."
bluetoothctl discoverable on
# Navigate to the specified directory
cd /home/servocontrol-N00

# Pull the latest changes from Git repository
git pull

# Start the Bluetooth agent with specified capabilities and PIN
bt-agent --capability=NoInputNoOutput -p pins &

# Start the servo control script
python bt_servo_control.py
