# Python MQTT subscriber test
#
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *

plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0
tempC= []

def makeFig(): #Create a function that makes our desired plot
    plt.ylim(10,40)     
    plt.style.use('ggplot')                            #Set y min and max values
    plt.title('My Live Streaming Sensor Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Temp Celcius')                            #Set ylabels
    plt.plot(tempC, 'ro-', label='Degrees C')       #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend
                  #plot the legend


 
def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
 
def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))
    temp =  float(message.payload)
    tempC.append(temp) 
    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
        tempC.pop(0)                       #This allows us to just see the last 50 data points
        

client = mqtt.Client()
client.username_pw_set("rabbitmq", password='rabbitmq')
client.connect("192.168.0.129", 1883) 

client.on_connect = on_connect       #attach function to callback
client.on_message = on_message       #attach function to callback

client.subscribe("mq2_mqtt") 
client.loop_forever()                 #start the loop