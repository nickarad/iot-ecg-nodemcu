# import os
from time import sleep
import serial

# os.system("arduino-cli compile --fqbn esp8266:esp8266:nodemcu .")
# os.system("esptool.py --chip esp8266 --port /dev/ttyUSB0 write_flash --flash_mode dio --flash_size detect 0x0 ..esp8266.esp8266.nodemcu.bin")

ser = serial.Serial('/dev/ttyUSB0', 115200) # Establish the connection on a specific port
counter = 32 # Below 32 everything in ASCII is gibberish
while True:
     counter +=1
     ser.write(str(chr(counter))) # Convert the decimal number to ASCII then send it to the Arduino
     print(ser.readline()) # Read the newest output from the Arduino
     sleep(.1) # Delay for one tenth of a second
     if counter == 255:
		counter = 32