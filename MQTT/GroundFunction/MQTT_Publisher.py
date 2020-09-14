import paho.mqtt.publish as publish
    
publish.single("CoreElectronics/test", "Hello")
publish.single("CoreElectronics/topic", "World!")

print("Done")
