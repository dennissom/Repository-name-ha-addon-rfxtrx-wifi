#!/usr/bin/with-contenv bash

HOST=$(jq -r '.host' /data/options.json)
PORT=$(jq -r '.port' /data/options.json)
MQTT_HOST=$(jq -r '.mqtt_host' /data/options.json)
MQTT_PORT=$(jq -r '.mqtt_port' /data/options.json)

echo "Starting RFXtrx PRO bridge"
echo "TCP $HOST:$PORT"

socat PTY,link=/dev/ttyRFX,raw,echo=0 TCP:$HOST:$PORT &

sleep 3

python3 /rf_monitor.py /dev/ttyRFX $MQTT_HOST $MQTT_PORT &

wait