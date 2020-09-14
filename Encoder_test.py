# Imports
from tkinter import *
import time
import RPi.GPIO as GPIO

# Modus setzen
GPIO.setmode(GPIO.BCM)

# Direction Output festlegen
GPIO.setup(23, GPIO.OUT)

# Enable Output festlegen
GPIO.setup(18, GPIO.OUT)

# Input festlegen
GPIO.setup(22, GPIO.IN)

# Outputs 
def OutDirection_ON():
    GPIO.output(23, GPIO.HIGH)

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

# Nach Links drehen
def rechts_an():
    OutDirection_OFF()
    OutEnable_ON()
    l = Label(root, text="Dreht nach rechts..").grid(row=2, column=0, columnspan=2)

# Nach Rechts drehen
def links_an():
    OutDirection_ON()
    OutEnable_ON()
    l = Label(root, text="Dreht nach links...").grid(row=2, column=0, columnspan=2)

# Motor anhalten
def stop():
    OutEnable_OFF()
    OutDirection_OFF()
    l = Label(root, text="-----------------------------").grid(row=2, column=0, columnspan=2)
    
# Ausgänge auf OFF setzen
OutDirection_OFF()
OutEnable_OFF()

# Eventdetect ausführen
Eventdetect()

# GUI
root = Tk()
root.geometry("400x400")
root.title("Motor Experiment")

b_links = Button(root, text="Nach links drehn", padx=45, pady=20, command=links_an).grid(row=0, column=0)
b_rechts = Button(root, text="Nach rechts drehn", padx=45, pady=20, command=rechts_an).grid(row=0, column=1)
b_stop = Button(root, text="Stop", padx=45, pady=20, command=stop).grid(row=1, column=0, columnspan=2)

root.mainloop()




