#
# Micropython ESP8266 code to Publish temperature sensor data to an Adafruit IO Feed using the MQTT protocol
# Also publishes statistics on the number of free bytes on the micropython Heap
#
# Hardware used:
# - Adafruit Huzzah ESP8266 running micropython version esp8266-20160909-v1.8.4.bin
# - Adafruit MCP9808 temperature breakout board
# - USB to serial converter
#

# prerequisites:
# - Adafruit account
# - registered to use Adafruit IO

#
# References and Kudos
#
# Big thanks to Tony DiCola from Adafruit for excellent tutorials on:
#   Ampy tutorial:  valuable tool to efficiently develop python code on ESP8266 hardware:  
#     https://learn.adafruit.com/micropython-basics-load-files-and-run-code
#   i2c on micropython hardware tutorial:  
#     https://learn.adafruit.com/micropython-hardware-i2c-devices
# 

import network
import time
from machine import Pin
from umqtt.simple import MQTTClient

#
# conversion routine, MCP9808 2-byte response --> Degrees C (courtesy of Tony DiCola)
#
'''def convertMCP9808ToDegC(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp
'''
#
# configure i2c for communication to MCP9808 sensor hardware
#
butt = Pin(0, Pin.IN, Pin.PULL_UP)
#
# connect the ESP8266 to local wifi network
#
yourWifiSSID = " "
yourWifiPassword = " "
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(yourWifiSSID, yourWifiPassword)
while not sta_if.isconnected():
  pass
  
#
# connect ESP8266 to Adafruit IO using MQTT
#
myMqttClient = "miket-mqtt-client"  # can be anything unique
adafruitIoUrl = "io.adafruit.com" 
adafruitUsername = " "  # can be found at "My Account" at adafruit.com
adafruitAioKey = " "  # can be found by clicking on "VIEW AIO KEYS" when viewing an Adafruit IO Feed
c = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)

c.connect()

#
# publish temperature and free heap to Adafruit IO using MQTT
#
# note on feed name in the MQTT Publish:  
#    format:
#      "<adafruit-username>/feeds/<adafruitIO-feedname>"
#    example:
#      "MikeTeachman/feeds/feed-TempInDegC"
#
#
while True:
  if not butt.value():
	c.publish("username/feeds/digital", str(1))  #publish num free bytes on the Heap
 
	print("send ok")
	time.sleep(2)  # number of seconds between each Publish

  
  
c.disconnect()  
