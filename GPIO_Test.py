import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set Outputs
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

def ledBlink(gpioInput):
    GPIO.output(gpioInput, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(gpioInput, GPIO.LOW)
    time.sleep(1)

while True:
    ledBlink(20)
