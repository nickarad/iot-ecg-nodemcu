#!/bin/bash
arduino-cli compile --fqbn esp8266:esp8266:nodemcu .
arduino-cli upload -p /dev/ttyUSB0 --fqbn esp8266:esp8266:nodemcu .