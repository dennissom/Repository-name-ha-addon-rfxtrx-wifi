import serial, sys, json, threading
from flask import Flask
import paho.mqtt.client as mqtt

serial_port = sys.argv[1]
mqtt_host = sys.argv[2]
mqtt_port = int(sys.argv[3])

ser = serial.Serial(serial_port,38400,timeout=1)

client = mqtt.Client()
client.connect(mqtt_host,mqtt_port,60)

events=[]

def read_rf():
    while True:
        data=ser.read(32)
        if not data:
            continue
        hexdata=data.hex()
        device_id=hexdata[4:10]
        event={
            "device_id":device_id,
            "raw":hexdata
        }
        events.append(event)
        if len(events)>50:
            events.pop(0)
        client.publish("rfxtrx/event",json.dumps(event))
        print("RF EVENT",event)

threading.Thread(target=read_rf,daemon=True).start()

app=Flask(__name__)

@app.route("/")
def index():
    html="<h2>RFXtrx RF Monitor</h2>"
    for e in reversed(events):
        html+=f"<p>{e}</p>"
    return html

app.run(host="0.0.0.0",port=8099)