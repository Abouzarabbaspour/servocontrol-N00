

##### startup script

cp startup_nomadiot_001.sh /etc/init.d/startup_nomadiot_001.sh
chmod +x /etc/init.d/startup_nomadiot_001.sh




####
cd ~
git clone https://github.com/abouzarabbaspour/servocontrol-N00.git

sudo hciconfig hci0 piscan
sudo hciconfig hci0 name 'Device Name'

sudo apt-get install bluetooth libbluetooth-dev -y
pip install pybluez

bluetoothctl system-alias new-name
bluetoothctl power off
bluetoothctl power on
bluetoothctl discoverable on
bt-agent --capability=NoInputNoOutput -p pins


##fix 'no such file or directory erro'
Running bluetooth in compatibility mode,
by modifying /etc/systemd/system/dbus-org.bluez.service,
changing
ExecStart=/usr/lib/bluetooth/bluetoothd
into
ExecStart=/usr/lib/bluetooth/bluetoothd -C
Then adding the Serial Port Profile, executing: 
sudo sdptool add SP
after that run
systemctl daemon-reload 
service bluetooth restart