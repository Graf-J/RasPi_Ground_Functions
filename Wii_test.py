from nunchuck import nunchuck
from time import sleep

wii = nunchuck()

while True:
    wii.joystick()
    sleep(0.2)
