import smbus
import time

address = 0x48
cmd = 0x40
value = 0

bus = smbus.SMBus(1)

A0 = 0x40 # Temperatursensor
A1 = 0x41 # Fotosensor
A2 = 0x42 # Sticksensor
A3 = 0x43 # Drehsensor

while True: 
    value = bus.read_byte_data(address, A2)
    #time.sleep(0.01)
    #value = bus.read_byte_data(address, A3)
    print("AIN:%1.3f  " %(value))
    time.sleep(0.05)
    



#  Analoger Output
while True:
    bus.write_byte_data(address, cmd, value)
    value += 1
    if value == 256:
        value = 0
    print("AOUT:%3d" %value)
    time.sleep(0.01)

  
    
