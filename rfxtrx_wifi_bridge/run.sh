#!/usr/bin/with-contenv bash

HOST=$(jq --raw-output '.host' /data/options.json)
PORT=$(jq --raw-output '.port' /data/options.json)

echo "Starting RFXtrx WiFi bridge"

while true
do
  socat -d -d PTY,link=/dev/ttyRFX,raw,echo=0 TCP:$HOST:$PORT
  sleep 5
done