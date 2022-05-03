import network
import credentials

sta_if = network.WLAN(network.STA_IF)

sta_if.active(True)
sta_if.connect(credentials.ssid, credentials.password)

while not sta_if.isconnected():  # wait to connect
    pass

print(sta_if.isconnected())
print(sta_if.ifconfig())
