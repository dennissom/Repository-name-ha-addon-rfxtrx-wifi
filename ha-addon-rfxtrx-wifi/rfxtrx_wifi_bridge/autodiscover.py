import serial
import json
import sys
import paho.mqtt.client as mqtt

serial_port = sys.argv[1] if len(sys.argv) > 1 else "/dev/ttyRFX"
mqtt_host = sys.argv[2] if len(sys.argv) > 2 else "localhost"
mqtt_port = int(sys.argv[3]) if len(sys.argv) > 3 else 1883

ser = serial.Serial(serial_port, 38400, timeout=1)

client = mqtt.Client()
client.connect(mqtt_host, mqtt_port, 60)

devices = {}

print("RFXtrx autodiscovery started")

while True:
    data = ser.read(32)
    if not data:
        continue

    device_id = data.hex()[4:10]

    if device_id not in devices:
        topic = f"homeassistant/cover/rfxtrx_{device_id}/config"

        payload = {
            "name": f"RFX Blind {device_id}",
            "command_topic": f"rfxtrx/{device_id}/set",
            "state_topic": f"rfxtrx/{device_id}/state",
            "payload_open": "OPEN",
            "payload_close": "CLOSE",
            "payload_stop": "STOP",
            "unique_id": f"rfxtrx_{device_id}"
        }

        client.publish(topic, json.dumps(payload), retain=True)
        devices[device_id] = True

        print("Discovered device", device_id)

    client.publish(f"rfxtrx/{device_id}/state", data.hex())