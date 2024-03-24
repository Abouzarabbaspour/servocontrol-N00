import os
import glob
import time
import RPi.GPIO as GPIO
from bluetooth import *
from gpiozero import AngularServo
import config as cfg

servo = AngularServo(18, min_angle=-120, max_angle=90)
def set_angle(angle):
    servo.angle = angle
def open_door():
    # read open angle from config file
    open_angle = cfg.angle_values['open']
    set_angle(open_angle)
def close_door():
    # read close angle from config file
    close_angle = cfg.angle_values['close']
    set_angle(close_angle)

def open_close_door():
    open_door()
    time.sleep(1)
    close_door()


close_door()

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
        print("received key [%s]" % data)
        if data== 'open':
            open_close_door()
        elif data == 'open_switch':
            open_door()
        elif data == 'close_switch':
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