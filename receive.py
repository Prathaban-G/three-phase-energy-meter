import paho.mqtt.client as mqtt
import firebase_admin
from firebase_admin import credentials, db
import datetime


import time



# Initialize Firebase
cred = credentials.Certificate("C:/Users/GOKUL/Desktop/Project/three-phase-energy-meter/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://three-phase-energy-meter-default-rtdb.firebaseio.com/'
})

# MQTT Settings
mqtt_broker = "mqtt-dashboard.com"
mqtt_port = 1883
mqtt_topic = "testtopic/470"

# Firebase Realtime Database Reference
ref = db.reference('mqttData/HW-20')
mqtt_data_list = []
# Callback when MQTT message is received
def on_message(client, userdata, message):
    mqtt_data = message.payload.decode()
    print("Received MQTT data:", mqtt_data)
    # Send data to Firebase Realtime Database
    ref.update({'data': mqtt_data})
    print("Data sent to Firebase")
    time.sleep(10)
    
# Initialize MQTT Client
client = mqtt.Client()
client.on_message = on_message

# Connect to MQTT Broker
client.connect(mqtt_broker, mqtt_port, keepalive=60)
client.subscribe(mqtt_topic)

# Start MQTT loop
client.loop_forever()






