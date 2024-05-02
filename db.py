import paho.mqtt.client as mqtt
import firebase_admin
from firebase_admin import credentials, db
import datetime
import time

# Initialize Firebase
cred = credentials.Certificate("C:/Users/PRATHABAN/Desktop/Energy Project/three-phase-energy-meter/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://three-phase-energy-meter-default-rtdb.firebaseio.com/'
})

# MQTT Settings
mqtt_broker = "mqtt-dashboard.com"
mqtt_port = 1883
mqtt_topic = "testtopic/470"

# Callback when MQTT message is received
def on_message(client, userdata, message):
    mqtt_data = message.payload.decode()
    print("Received MQTT data:", mqtt_data)

    # Get today's date
   

    # Get a reference to the Firebase database with today's date as the path
    ref = db.reference(f'mqttDataBase')

    # Get current timestamp for data storage
    
    # Update Firebase with data under the timestamp path
    ref.child("data").set(mqtt_data)
    print("Data sent to Firebase")

# Initialize MQTT Client
client = mqtt.Client()
client.on_message = on_message

# Connect to MQTT Broker
client.connect(mqtt_broker, mqtt_port, keepalive=60)
client.subscribe(mqtt_topic)

# Start MQTT loop
client.loop_start()

try:
    while True:
        # Sleep for 10 seconds
        time.sleep(10)
except KeyboardInterrupt:
    # Stop MQTT loop on keyboard interrupt
    client.loop_stop()
