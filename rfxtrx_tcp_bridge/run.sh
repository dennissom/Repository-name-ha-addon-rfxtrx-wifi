#!/usr/bin/env bash

HOST=$(jq -r '.host' /data/options.json)
PORT=$(jq -r '.port' /data/options.json)

echo "Starting RFXtrx TCP Bridge"
echo "Connecting to $HOST:$PORT"

while true
do
  socat -d -d PTY,link=/dev/ttyRFX,raw,echo=0 TCP:$HOST:$PORT
  echo "Connection lost. Reconnecting in 5 seconds."
  sleep 5
done