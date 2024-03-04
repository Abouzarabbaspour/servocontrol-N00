
from gpiozero import AngularServo
from time import sleep
import requests

servo = AngularServo(18, min_angle=-90, max_angle=90)

def set_angle(angle):
    servo.angle = angle


# while True:
#     response = requests.get("https://api.example.com/data?id=10001") 
#     data = response.json()
#     value = data['value']
#     servo.angle = value
#     sleep(5)
