
from gpiozero import AngularServo
from time import sleep
import time
import requests
import bluetooth 

servo = AngularServo(18, min_angle=-90, max_angle=90)

def set_angle(angle):
    servo.angle = angle


# while True:
#     response = requests.get("https://api.example.com/data?id=10001") 
#     data = response.json()
#     value = data['value']
#     servo.angle = value
#     sleep(5)

# Function to get paired Bluetooth devices
def get_paired_devices():
    try:
        # Run the bluetoothctl command to get paired devices
        output = subprocess.check_output(["bluetoothctl", "paired-devices"], stderr=subprocess.STDOUT).decode()
        
        # Split the output by lines
        lines = output.split('\n')
        
        paired_devices = {}
        # Parse each line to extract MAC addresses and names
        for line in lines:
            line = line.strip()
            if line.startswith("Device"):
                parts = line.split(' ')
                mac_address = parts[1]
                device_name = ' '.join(parts[2:])
                paired_devices[device_name] = mac_address
        
        return paired_devices
    
    except subprocess.CalledProcessError as e:
        print("Error:", e.output)
        return {}
    

# Main function
def main():
    paired_devices = get_paired_devices()
    if not paired_devices:
        print("No paired devices found.")
        return

    # Select the first paired device as the target
    target_device_name = list(paired_devices.keys())[0]
    target_device_address = paired_devices[target_device_name]

    print(f"Connecting to {target_device_name} ({target_device_address})")

    while True:
        try:
            # Connect to the Bluetooth device
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((target_device_address, 1))
            print("Connected to device")
            
            while True:
                # Receive data (assuming the data received is the angle)
                data = sock.recv(1024).decode()
                if data:
                    angle = float(data)
                    set_angle(angle)
                
                time.sleep(1)  # Adjust this delay as needed
                
        except bluetooth.btcommon.BluetoothError as e:
            print("Bluetooth connection error:", e)
            time.sleep(5)  # Wait before trying to reconnect

if __name__ == "__main__":
    main()