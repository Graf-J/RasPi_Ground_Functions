import smbus
import paho.mqtt.publish as publish
import time

#Convert Bit -> Temperature
def convertTemp(dist, bit):
    div = 5 / dist
    if dist == 12:
        temp = 15
        bitZ = 179 
        while bitZ != bit:
            temp += div
            bitZ -= 1

        return temp
    
    elif dist == 13:
        temp = 25
        bitZ = 154
        while bitZ != bit:
            temp += div
            bitZ -= 1
            
        return temp
    
    
#Convert Bit -> Temperature
def getTemp(bit):
    dist = 0
    
    if bit <= 154:
        dist = 13
    else:
        dist = 12

    temp = convertTemp(dist, bit)
    return temp


# Analog Variables   
address = 0x48
bus = smbus.SMBus(1)
A0 = 0x40
A1 = 0x41

while True:
    # Get Values from Sensors
    tempValue = bus.read_byte_data(address, A0)
    lightValue = bus.read_byte_data(address, A1)
    
    # Publish them via MQTT
    publish.single("PI/Temperature", tempValue)
    publish.single("PI/Light", lightValue)

    # Send every <x> Seconds
    time.sleep(3)
