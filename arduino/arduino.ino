/*
 Basic ESP8266 MQTT publish client example
*/
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include "secret-config.h"

WiFiClient espClient;
PubSubClient client(espClient);
String msg;
char payload[50];
unsigned long lastMicros = 0;
const int analogInPin = 17;  

float getECG(void) {
	float analog0;
	// Read from analogic in. 
	analog0=analogRead(analogInPin);
	// binary to voltage conversion
	return analog0 = (float)analog0 * 3.3 / 1023.0;   
}

void setup_wifi() {
	// Connecting to a WiFi network
	WiFi.begin(ssid, password);
	while (WiFi.status() != WL_CONNECTED) {
		delay(500);
		Serial.print(".");
	}
	Serial.println("WiFi connected");
	Serial.println("IP address: ");
	Serial.println(WiFi.localIP());
}

void reconnect() {
	// Loop until we're reconnected
	Serial.println("In reconnect...");
	while (!client.connected()) {
		Serial.print("Attempting MQTT connection...");
		// Attempt to connect
		if (client.connect("Arduino_Gas", mqtt_user, mqtt_pass)) {
			Serial.println("connected");
		} 
		else {
			Serial.print("failed, rc=");
			Serial.print(client.state());
			Serial.println(" try again in 5 seconds");
			delay(5000);
		}
	}
}

void setup() {
	Serial.begin(115200);
	setup_wifi();
	client.setServer(mqtt_server, 1883);
}

void loop() {
  
	char msg[8];

	// Desired sample rate T=7812microseconds
	if (micros() - lastMicros > 7812) {
		lastMicros = micros();
		// float temperatureC = getTemperature() ;
		float ecg = getECG();
		sprintf(msg,"%f",ecg);
		// Serial.print("temperature read");
		if (!client.connected()) {
			Serial.print("trying to reconnect...");
			reconnect();
		}

		client.publish("mq2_mqtt", msg);
		Serial.print("Payload: ");
		Serial.println(msg);
	}
}