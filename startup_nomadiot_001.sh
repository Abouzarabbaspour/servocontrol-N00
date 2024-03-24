#!/bin/sh
# Change directory to the location of the script
cd "$(dirname "$0")"

systemctl daemon-reload 
service bluetooth restart
# Start the Bluetooth agent and configure Bluetooth settings
echo "Starting Bluetooth agent..."
echo "Configuring Bluetooth settings..."
bluetoothctl system-alias nomadiot_001 & sleep 5
echo "Powering off Bluetooth..."
bluetoothctl power off & sleep 5
echo "Powering on Bluetooth..."
bluetoothctl power on & sleep 5
echo "Setting device to discoverable..."
bluetoothctl discoverable on & sleep 5
# Navigate to the specified directory
cd /root/servocontrol-N00

# Pull the latest changes from Git repository
git pull

chmod +x startup_nomadiot_001.sh
# Start the Bluetooth agent with specified capabilities and PIN
bt-agent --capability=NoInputNoOutput -p pins &

# Start the servo control script
python bt_servo_control.py
