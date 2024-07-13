import paho.mqtt.client as mqtt
import requests
import json

# Define MQTT broker details
broker = "public.mqtthq.com"
port = 1883
topic = "mqttHQ-client-test1"  # Replace with your actual MQTT topic

# Define HTTP server URL
http_url = "https://waterlevel.monitoring.oliveiot.in/getdatafromesp.php"

# Callback when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing to the topic
    client.subscribe(topic)

# Callback when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()}")
    
    # Parse JSON payload
    data = json.loads(msg.payload.decode())
    
    # Send data to HTTP server
    response = requests.post(http_url, data=data)
    
    if response.status_code == 200:
        print("Data sent successfully")
    else:
        print(f"Failed to send data, status code: {response.status_code}")

# Create an MQTT client and assign callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker, port, 60)

# Blocking call that processes network traffic, dispatches callbacks, and handles reconnecting
client.loop_forever()
