import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("CoreElectronics/test")
    client.subscribe("CoreElectronics/topic")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# When trying to get messages from oter Computer: Instead of 'localhost' put in 192.168.178.48  (which is the IP-Adress of the PI)
client.connect("localhost", 1883, 60)

client.loop_forever()
