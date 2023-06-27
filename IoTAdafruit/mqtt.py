import sys
import random
import time
from Adafruit_IO import MQTTClient

AIO_FEED_ID = ""
AIO_USERNAME = "KhavidNgo"
AIO_KEY = "aio_MwSU57uPmBTvlQodQaxYEBMhMWZa"


def connected(client):
    print("Connecting to the server ...")
    client.subscribe(AIO_FEED_ID)
    client.subscribe("button1")
    client.subscribe("button2")


def subscribe(client, userdata, mid, granted_qos):
    print("Subscribe successfully ...")


def disconnected(client):
    print("Disconnecting ...")
    sys.exit (1)


def message(client, feed_id, payload):
    print("Input data: " + payload)


client = MQTTClient(AIO_USERNAME , AIO_KEY)

client.on_connect = connected  # function pointer
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()

while True:
    time.sleep(5)
    value1 = random.randint(20, 70)
    value2 = random.randint(0, 100)
    value3 = random.randint(0, 1000)
    print("Updating ...")
    client.publish("sensor1", value1)
    client.publish("sensor2", value2)
    client.publish("sensor3", value3)
    pass
