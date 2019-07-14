# Python MQTT subscriber test
#
import paho.mqtt.client as mqtt
 
def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
 
def on_message(client, userdata, message):
    print ("Message received: "  + message.payload)

client = mqtt.Client()
client.username_pw_set("admin1", password='admin1')
client.connect("192.168.0.121", 1883) 

client.on_connect = on_connect       #attach function to callback
client.on_message = on_message       #attach function to callback

client.subscribe("mq2_mqtt") 
client.loop_forever()                 #start the loop