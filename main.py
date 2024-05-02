import paho.mqtt.client as mqtt
import json
import random
import time

import datetime
import time
class EnergyMeterMQTTClient:
    def __init__(self, broker_address,port,topic):
        self.broker_address = broker_address
        self.port = port
        #self.client_id=client_id
        #self.username = username
        #self.password = password
        self.topic = topic

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        #self.client.username_pw_set(username, password)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    def connect(self):
        self.client.connect(self.broker_address, self.port,60)

    def start(self):
        self.client.loop_start()
        while True:
            random_values = self.generate_random_values()
            status_code, _ = self.client.publish(self.topic, json.dumps(random_values))
            print("Published with status code:", status_code)
            print("Data sent:", random_values)
            time.sleep(10)
     
   
    def generate_random_values(self):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        pv01 = round(random.uniform(200, 250), 2)
        pv02 = round(random.uniform(240, 280), 2)
        pv03 = round(random.uniform(200, 300), 2)
        pv04 = round(random.uniform(210, 220), 2)
        pv05 = round(random.uniform(225, 245), 2)
        pv06 = round(random.uniform(220, 270), 2)
        pv07 = round(random.uniform(270, 300), 2)
        pv08 = round(random.uniform(260, 290), 2)
        pv09 = round(random.uniform(230, 267), 2)
        pv10 = 1
       

        return {

            "timestamp":timestamp,
            "PV01": pv01,
            "PV02": pv02,
            "PV03": pv03,
            "PV04": pv04,
            "PV05": pv05,
            "PV06": pv06,
            "PV07": pv07,
            "PV08": pv08,
            "PV09": pv09,
            "PV10": pv10,
           
        }


if __name__ == "__main__":
    broker_address = "mqtt-dashboard.com"
    port =1883
    topic = "testtopic/470"
    #client_id="clientId-JZnMXefu2U"

    mqtt_client = EnergyMeterMQTTClient(broker_address,port,topic)
    mqtt_client.connect()
    mqtt_client.start()







