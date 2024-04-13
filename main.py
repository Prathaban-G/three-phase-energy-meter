import paho.mqtt.client as mqtt
import json
import random
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
            time.sleep(2)

    def generate_random_values(self):
        pv01 = round(random.uniform(0.85, 0.95), 2)
        pv02 = round(random.uniform(1500, 1700), 2)
        pv03 = round(random.uniform(49.5, 50.5), 2)
        pv04 = round(random.uniform(390, 410), 2)
        pv05 = round(random.uniform(225, 235), 2)
        pv06 = round(random.uniform(390, 410), 2)
        pv07 = round(random.uniform(390, 410), 2)
        pv08 = round(random.uniform(390, 410), 2)
        pv09 = round(random.uniform(7.5, 8.5), 2)
        pv10 = round(random.uniform(700, 800), 2)
        pv11 = round(random.uniform(150, 175), 2)
        pv12 = round(random.uniform(150, 175), 2)
        pv13 = round(random.uniform(150, 175), 2)
        pv14 = round(random.uniform(700, 800), 2)

        return {
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
            "PV11": pv11,
            "PV12": pv12,   
            "PV13": pv13,
            "PV14": pv14
        }


if __name__ == "__main__":
    broker_address = "mqtt-dashboard.com"
    port =1883
    #username = "energymeter"
    #password = "energy@123"
    topic = "testtopic/143"
    #client_id="clientId-JZnMXefu2U"

    mqtt_client = EnergyMeterMQTTClient(broker_address,port,topic)
    mqtt_client.connect()
    mqtt_client.start()







