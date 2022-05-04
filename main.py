import network
from umqtt.simple import MQTTClient
import ubinascii
import credentials
import machine

# mqtt config variables
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
print("CLIENT_ID is {}".format(CLIENT_ID))

# connect to wifi
sta_if = network.WLAN(network.STA_IF)

sta_if.active(True)
sta_if.connect(credentials.ssid, credentials.password)

while not sta_if.isconnected():  # wait to connect
    pass

print(sta_if.ifconfig())

# mqtt pulication loop
while True:
    c = MQTTClient(
           'esp8266_21195000',
           credentials.mqtt_server,
           port = 8883,
           keepalive = 10000,
           ssl = True,
           ssl_params = {
               'cert': credentials.cert,
               'key': credentials.key
               }
           )
    try:
        c.connect()
    except OSError:
        print('error connecting to server')
        machine.lightsleep(1000)
        continue
    c.publish(topic = 'test', msg = 'hi hi hi', qos = 0)
    c.disconnect()
    machine.lightsleep(1000)
