FROM alpine:3.19

RUN apk add --no-cache socat bash jq python3 py3-pip
RUN pip install pyserial paho-mqtt flask

COPY run.sh /run.sh
COPY rf_monitor.py /rf_monitor.py

RUN chmod +x /run.sh

CMD [ "/run.sh" ]