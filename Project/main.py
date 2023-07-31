import time
import sys
from Adafruit_IO import MQTTClient
from Adafruit_IO import Client
from AI_detect import *
import serial.tools.list_ports
AIO_FEED_ID = ["result","camera","guest","caution","alarm"]
AIO_USERNAME = "KhavidNgo"
AIO_KEY = "aio_QhjM61p9Pu8ssAYWFZY3hYeY0PkE"

try:
    ser = serial.Serial(port="COMx",baudrate=115200)
except:
    print("Can not open the port")

def sendCommand(cmd):
    ser.write(cmd.encode())

def connected(client):
    print("Connected to server...")
    for things in AIO_FEED_ID:
        client.subscribe(things)

def subscribe(client, userdata, mid, granted_qos):
    print("Subscribe sucessfully...")

def disconnected ( client ) :
    print("Disconnected...")
    sys.exit(1)

def message ( client , feed_id , payload ) :
    print(f"AI result from { feed_id } : { payload }")

client = MQTTClient(AIO_USERNAME, AIO_KEY)
aio = Client(AIO_USERNAME, AIO_KEY)

client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

ai_result = ""
count = 5
pre_guest = 0
guest = 0
pre_caution = 0
caution = 0

while True :
    count = count - 1
    if count == 0:
        count = 5

        pre_guest = guest
        pre_caution = caution

        ai_result, ai_cap = AI_Identify()

        if ai_result == "Guests":
            guest = 1
        else:
            guest = 0
        if pre_guest == guest:
            caution = 1
        else:
            caution = 0

        client.publish("result", ai_result)
        client.publish("camera", ai_cap)
        client.publish("guest", guest)
        client.publish("caution", caution)

    alarm = aio.receive("alarm")
    if alarm == "1":
        sendCommand("2")
    else:
        sendCommand("3")

    time.sleep(1)

    keyboard_input = cv2 . waitKey(1)
    if keyboard_input == 27:
        break