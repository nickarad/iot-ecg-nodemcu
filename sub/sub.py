# Python MQTT subscriber test
#
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *



plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt = 0
ecg = []
values = []

# def makeFig(): #Create a function that makes our desired plot
#     # plt.ylim(0,1)     
#     plt.style.use('ggplot')                            #Set y min and max values
#     plt.title('My Live Streaming Sensor Data')      #Plot the title
#     plt.grid(True)                                  #Turn the grid on
#     plt.ylabel('ECG')                            #Set ylabels
#     plt.plot(ecg, label='ecg')       #plot the temperature
#     plt.legend(loc='upper left')                    #plot the legend
#                   #plot the legend

def plotValues():
    plt.title('My Live Streaming Sensor Data')
    plt.style.use('ggplot') 
    plt.grid(True)
    plt.ylabel('EECG')
    plt.plot(values, 'b', label='ecg')
    plt.legend(loc='upper right')
    

#pre-load dummy data
for i in range(0,400):
    values.append(0)
 
def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
 
def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))
    with open('ecg.txt','a+') as f:
         f.write(message.payload + "\n")
    # sample = sample + 1
    data =  float(message.payload)
    valueRead = data

    #check if valid value can be casted
    try:
        valueInInt = float(valueRead)
        print(valueInInt)
        if valueInInt <= 1024:
            if valueInInt >= 0:
                values.append(valueInInt)
                values.pop(0)
                drawnow(plotValues)
            else:
                print
                'Invalid! negative number'
        else:
            print("Invalid! too large")
    except ValueError:
        print("Invalid! cannot cast")
    # ecg.append(data) 
    # drawnow(makeFig)                       #Call drawnow to update our live graph
    # plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    # cnt = cnt + 1
    # if(cnt > 50):                            #If you have 50 or more points, delete the first one from the array
    #     tempC.pop(0)                       #This allows us to just see the last 50 data points
        

client = mqtt.Client()
client.username_pw_set("rabbitmq", password='rabbitmq')
client.connect("104.155.172.54", 1883) 

client.on_connect = on_connect       #attach function to callback
client.on_message = on_message       #attach function to callback
QoS = 1
client.subscribe("mq2_mqtt",QoS) 
client.loop_forever()                 #start the loop
