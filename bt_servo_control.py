import os
import glob
import time
import RPi.GPIO as GPIO
from bluetooth import *
from gpiozero import AngularServo

servo = AngularServo(18, min_angle=-90, max_angle=90)
def set_angle(angle):
    servo.angle = angle

def open_door():
    set_angle(90)

def close_door():
    set_angle(-90)

# base_dir = '/sys/bus/w1/devices/'
# device_folder = glob.glob(base_dir + '28*')[0]
# device_file = device_folder + '/w1_slave'

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "NomadHomeServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )
while True:          
    print("Waiting for connection on RFCOMM channel %d" % port)
    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)
    try:
        data = client_sock.recv(1024)
        if len(data) == 0: 
            break

        data = data.decode('utf-8')
        data = data.strip()
        data = data.lower()
        data = data.replace('\n', '')
        data = data.replace('\r', '')
        print("received [%s]" % data)
        if data == 'open':
            open_door()
        elif data == 'close':
            close_door()
        else:
            data = 'WTF!' 
            client_sock.send(data)
        print("sending [%s]" % data)
    except IOError:
        pass
    except KeyboardInterrupt:
        print("disconnected")
        client_sock.close()
        server_sock.close()
        print("all done")
        break