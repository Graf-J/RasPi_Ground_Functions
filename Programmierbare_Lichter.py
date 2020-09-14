import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Outputs setzen

GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.LOW)

GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.LOW)

GPIO.setup(4, GPIO.OUT)
GPIO.output(4, GPIO.LOW)

GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.LOW)

GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.LOW)

GPIO.setup(5, GPIO.OUT)
GPIO.output(5, GPIO.LOW)

GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.LOW)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)

# Inputs setzen

GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

# Lichter Methoden definieren

def eins():
    GPIO.output(21, GPIO.HIGH)

def zwei():
    GPIO.output(18, GPIO.HIGH)

def drei():
    GPIO.output(4, GPIO.HIGH)

def vier():
    GPIO.output(25, GPIO.HIGH)

def fuenf():
    GPIO.output(13, GPIO.HIGH)

def sechs():
    GPIO.output(5, GPIO.HIGH)

def sieben():
    GPIO.output(22, GPIO.HIGH)

def acht():
    GPIO.output(17, GPIO.HIGH) 

# Ausgabefunktion

def funktion(x):
    
    if x == "1":
        eins()
    elif x == "2":
        zwei()
    elif x == "3":
        drei()
    elif x == "4":
        vier()
    elif x == "5":
        fuenf()
    elif x == "6":
        sechs()
    elif x == "7":
        sieben()
    elif x == "8":
        acht()
    else:
        print("Geh hoim")

# Taster False setzen

taster_1 = False
taster_2 = False
i = 0
x = 0
pause = 0

# Array

arr = [0, 0, 0, 0, 0, 0, 0, 0]

# Anleitung

print("Drücken Sie Taster 2 für eine Eingabe, sobald Taster 1 betätigt wird wird das Eingegebene Programm abgespielt.")

# Taster überprüfen
while 1:
    
    if GPIO.input(23):
        taster_1 = True
        taster_2 = False
    
    if GPIO.input(24):
        taster_2 = True
        taster_1 = False 
    
    if taster_1 == True:
        pause = input("Wie lange sollen die Pausen zwischen erscheinen der Lichter sein?\n")
        
        try:
            while arr[x] != 0:
                funktion(arr[x])
                x += 1
                time.sleep(float(pause))

        except:
          print("Well done!")
          break 
            
    if taster_2 == True:
        Licht_an = input("[1][2][3][4][5][6][7][8]\nWelches Licht soll angeschaltet werden?\n")
        arr[i] = Licht_an
        i += 1
        
        

    

    

