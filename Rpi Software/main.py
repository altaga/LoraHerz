import binascii
import struct
import time
from bluepy.btle import *
import argparse
import paho.mqtt.client as paho
import ssl

# This function trigger if the client connected
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc) )
    #client.subscribe("#" , 1 ) # Wild Card

# This function trigger every time we receive a message from the platform
def on_message(client, userdata, msg):
    print("topic: "+msg.topic)
    print("payload: "+str(msg.payload))
    
# This function trigger when we publish  
def on_publish(client, obj, mid):
    print("Data Sent")
    
# This function trigger when we subscribe to a new topic  
def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

EndPoint = "XXXXXXXXXXXXXX-ats.iot.us-east-1.amazonaws.com"

caPath = "Certs/aws-iot-rootCA.crt"
certPath = "Certs/Thunder.cert.pem"
keyPath = "Certs/Thunder.private.key"

# We subscribe to the topic we use to communicate from the Webapp to the Raspberry
PubTopic = '/Device1/EnvironmentData'

parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()

MAC_ADDR = str(args.echo)

TVOC = ""
eCO2 = ""
Pressure = ""
Sound = ""
temperature = ""
humidity = ""
bat = ""
sound =""
lig=""
uv=""

while 1:
    try:
        p = Peripheral(MAC_ADDR, "public")
        services=p.getServices()
        print("BT:ok")
        mqttc = paho.Client()
        # We prepare all callback functions and credentials.
        mqttc.on_connect = on_connect
        mqttc.on_message = on_message
        mqttc.on_publish = on_publish
        mqttc.on_subscribe = on_subscribe
        mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
        mqttc.connect(EndPoint, 8883, keepalive=60)
        rc = 0
        print("MQTT:ok")
        while 1:
            rc = mqttc.loop()
            characteristics = p.getCharacteristics()
            print("")
            for k in characteristics:
                if k.uuid == "efd658ae-c401-ef33-76e7-91b00019103b":
                    print("eCO2 Level")
                    eCO2 = int.from_bytes(k.read(), "little")
                    print(int.from_bytes(k.read(), "little"))
                if k.uuid == "efd658ae-c402-ef33-76e7-91b00019103b":
                    print("TVOC Level")
                    TVOC = int.from_bytes(k.read(), "little")
                    print(int.from_bytes(k.read(), "little"))
                if k.uuid == "00002a6d-0000-1000-8000-00805f9b34fb":
                    print("Pressure Level")
                    Pressure = (int.from_bytes(k.read(), "little"))/10
                    print((int.from_bytes(k.read(), "little"))/10)
                if k.uuid == "c8546913-bf02-45eb-8dde-9f8754f4a32e":
                    print("Sound Level")
                    Sound = (int.from_bytes(k.read(), "little"))/100
                    print((int.from_bytes(k.read(), "little"))/100)
                if k.uuid == "c8546913-bfd9-45eb-8dde-9f8754f4a32e":
                    print("Lux Level")
                    lig = (int.from_bytes(k.read(), "little"))/100
                    print((int.from_bytes(k.read(), "little"))/100)
                if k.uuid == "00002a6e-0000-1000-8000-00805f9b34fb":
                    print("Temperature")
                    temperature = (int.from_bytes(k.read(), "little"))/100
                    print((int.from_bytes(k.read(), "little"))/100)
                if k.uuid == "00002a6f-0000-1000-8000-00805f9b34fb":
                    print("Humidity")
                    humidity = (int.from_bytes(k.read(), "little"))/100
                    print((int.from_bytes(k.read(), "little"))/100)
                if k.uuid == "00002a19-0000-1000-8000-00805f9b34fb":
                    print("Battery")
                    bat = int.from_bytes(k.read(), "little")
                    print(int.from_bytes(k.read(), "little"))
                if k.uuid == "00002a76-0000-1000-8000-00805f9b34fb":
                    print("UV index")
                    uv = int.from_bytes(k.read(), "little")
                    print(int.from_bytes(k.read(), "little"))

            temp='{"TVOC":"'+str(TVOC)+'","eCO2":"'+str(eCO2)+'","Press":"'+str(Pressure)+'","Sound":"'+str(Sound)+'","Temp":"'+str(temperature)+'","Hum":"'+str(humidity)+'","Bat":"'+str(bat)+'","light":"'+str(lig)+'","UV":"'+str(uv)+'"}'
            mqttc.publish(PubTopic,temp)
            

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    
    except:
        print(".", end = '')