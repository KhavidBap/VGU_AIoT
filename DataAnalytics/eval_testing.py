import sys
import requests
import random
import time
from Adafruit_IO import MQTTClient

AIO_FEED_ID = ""
AIO_USERNAME = "KhavidNgo"
AIO_KEY = "<api_key>"

global_equation = ""  # global variable


def init_global_equation():
    global global_equation
    headers = {}
    aio_url = "https://io.adafruit.com/api/v2/KhavidNgo/feeds/equation"
    x = requests.get(url=aio_url, headers=headers, verify=False)
    data = x.json()
    global_equation = data["last_value"]
    print("Get lastest value:", global_equation)


def modify_value(x1, x2, x3):
    result = eval(global_equation)
    print(result)
    return result


def connected(client):
    print("Server connected ...")
    # client.subscribe("button1")
    # client.subscribe("button2")
    client.subscribe("equation")


def subscribe(client, userdata, mid, granted_qos):
    print("Subscribe successfully ...")


def disconnected(client):
    print("Disconnecting ...")
    sys.exit(1)


def message(client, feed_id, payload):
    print("Received: " + payload)
    if feed_id == "equation":
        global_equation = payload
        print(global_equation)


client = MQTTClient(AIO_USERNAME, AIO_KEY)

client.on_connect = connected  # function pointer
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

init_global_equation()
client.connect()
client.loop_background()

while True:
    x1 = random.randint(20,70)
    x2 = random.randint(0,100)
    x3 = random.randint(0,1000)
    client.publish("sensor1", x1)
    client.publish("sensor2", x2)
    client.publish("sensor3", x3)
    client.publish("result", modify_value(x1, x2, x3))
    time.sleep(60)
    pass
