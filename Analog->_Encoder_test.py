import time
import RPi.GPIO as GPIO
import smbus

GPIO.setmode(GPIO.BCM)

# Direction
GPIO.setup(23, GPIO.OUT)

# Enable
GPIO.setup(18, GPIO.OUT)

# Input
GPIO.setup(22, GPIO.IN)

# Outputs 
def OutDirection_ON():
    GPIO.output(23, GPIO.HIGH)
    #global direction

def OutDirection_OFF():
    GPIO.output(23, GPIO.LOW)

def OutEnable_ON():
    GPIO.output(18, GPIO.HIGH)

def OutEnable_OFF(): 
    GPIO.output(18, GPIO.LOW)

# Callbackfunktion mit Zähler
def callbackfun(inputnr):
    global i
    i = i + 1

i = 0

# Eventdetect Funktion
def Eventdetect():
    GPIO.add_event_detect(22, GPIO.RISING, callback=callbackfun)

# Nach Rechts drehen
def rechts_an():
    OutDirection_OFF()
    OutEnable_ON()

# Nach Links drehen
def links_an():
    OutDirection_ON()
    OutEnable_ON()

# Motor anhalten
def stop():
    OutEnable_OFF()
    OutDirection_OFF()
    
# Ausgänge auf OFF setzen
OutDirection_OFF()
OutEnable_OFF()

# Eventdetect ausführen
Eventdetect()

########################################################################

address = 0x48
cmd = 0x40
value = 0

bus = smbus.SMBus(1)

A0 = 0x40 # Temperatursensor
A1 = 0x41 # Fotosensor
A2 = 0x42
A3 = 0x43 # Drehsensor

while True:
    eins = bus.read_byte_data(address, A3)
    time.sleep(0.05)
    zwei = bus.read_byte_data(address, A3)
    if eins < zwei:
        print("rechts")
        stop()
        rechts_an()
        
    elif eins > zwei:
        print("links")
        stop()
        links_an()
        
    else:
        print("---")
        stop()
        
    time.sleep(0.05)
















