import paho.mqtt.publish as publish
import smbus
import time

# Analog Standards
bus = smbus.SMBus(1)
address = 0x48

# Analog Inputs
A0 = 0x40
A1 = 0x41

while True:
    # Get Inputs
    temp = bus.read_byte_data(address, A0)
    print(temp)
    # light = bus.read_byte_data(address, A1)

    # Publish Data via MQTT
    publish.single("PI/Temp", temp)
    # publish.single("PI/Light", light)


    time.sleep(2)




