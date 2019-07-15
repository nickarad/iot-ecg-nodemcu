# Quickstart

Follow the instructions below to quickly run clintelli platform locally.

1. Start **RabbitMQ** server with Docker. You will need to have Docker and Docker-compose installed
```
cd docker
docker-compose up
```

2. Prepare the arduino code, compile and upload it to your ESP-enabled arduino board. We have tested 
our prototype in a NodeMCU board. See more at [Arduino Setup](arduino/setup.md). Start the arduino microcontroller.

3. Install necessary Python libraries
```
pip install paho-mqtt
```
and then run the simple test subscriber in the `sub` folder
```
python test_sub.py
```