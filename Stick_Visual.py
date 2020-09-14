import smbus
import time
import turtle
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)

oldInputVal = False

bus = smbus.SMBus(1)
value_X = 0
value_Y = 0
address = 0x48

Wert_Y = 0x41 # A1
Wert_X = 0x42 # A2

x = 134
y = 129

wn = turtle.Screen()
wn.title("Stick Runner")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
#ball.penup()
ball.goto(0, 0)

wn.listen()

def InputFlanke():
    global oldInputVal
    ret = False
    actInputVal = GPIO.input(6)
    if (actInputVal == True) & (oldInputVal == False):
        ret = True
    if oldInputVal == True:
        time.sleep(1)
    oldInputVal = actInputVal
    return(ret)

while True:
    wn.update()

    if InputFlanke():
        farbe = input("Color?\n")
        ball.color(str(farbe))
        #print("hello")
    
    value_X = bus.read_byte_data(address, Wert_X)
    value_Y = bus.read_byte_data(address, Wert_Y)
    
    if x != value_X:
        dif = (value_X - x) * 2.5
        X_cor = ball.xcor()
        X_cor += dif
        ball.setx(X_cor)

    if y != value_Y:
        dif = ((value_Y - y) * (-1)) * 2.5
        Y_cor = ball.ycor()
        Y_cor += dif
        ball.sety(Y_cor)

    x = value_X
    y = value_Y

          
