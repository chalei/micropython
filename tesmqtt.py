from machine import Pin
from time import sleep
import machine
import ubinascii
from umqtt.simple import MQTTClient
import network


sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("SSID", "password")
sleep(4)
 
# Setup a GPIO Pin for output
led = Pin(16, Pin.OUT)

# Modify below section as required
CONFIG = {
     # Configuration details of the MQTT broker
     "MQTT_BROKER": "io.adafruit.com",
     "USER": "",
     "PASSWORD": "",
     "PORT": 1883,
     "TOPIC": b"user/feeds/feedsname",
     # unique identifier of the chip
     "CLIENT_ID": b"esp8266_" + ubinascii.hexlify(machine.unique_id())
}
 
# Method to act based on message received   
def onMessage(topic, msg):
    print("Topic: %s, Message: %s" % (topic, msg))
 
    if msg == b"1":
        led.value(1)
        
    elif msg == b"0":
        led.value(0)
        
 
def listen():
    #Create an instance of MQTTClient 
    client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'], user=CONFIG['USER'], password=CONFIG['PASSWORD'], port=CONFIG['PORT'])
    # Attach call back handler to be called on receiving messages
    client.set_callback(onMessage)
    client.connect()
    client.publish(CONFIG['TOPIC'], "on")
    client.subscribe(CONFIG['TOPIC'])
    print("ESP8266 is Connected to %s and subscribed to %s topic" % (CONFIG['MQTT_BROKER'], CONFIG['TOPIC']))
 
    try:
        while True:
            msg = client.wait_msg()
            #msg = (client.check_msg())
    finally:
        client.disconnect()  

listen()        
