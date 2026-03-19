FROM alpine:3.19

RUN apk add --no-cache socat bash jq python3 py3-pip
RUN pip install paho-mqtt pyserial

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]