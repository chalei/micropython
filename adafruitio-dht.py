import time
import machine
import dht
import network
from umqtt.simple import MQTTClient

yourWifiSSID = " "
yourWifiPassword = " "
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(yourWifiSSID, yourWifiPassword)
while not sta_if.isconnected():
  pass

myMqttClient = "chalei-mqtt"  # can be anything unique
adafruitIoUrl = "io.adafruit.com" 
adafruitUsername = "user"  # can be found at "My Account" at adafruit.com
adafruitAioKey = "aiokey"  # can be found by clicking on "VIEW AIO KEYS" when viewing an Adafruit IO Feed
c = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)
c.connect()

sensor = dht.DHT22(machine.Pin(2))
sensor.measure()
kelembaban = sensor.humidity()
suhu = sensor.temperature()
time.sleep(2)

def monitor():
	sensor.measure()
	
	time.sleep(1)
	print('kelembaban: {0:0.2f}'.format(kelembaban))
	c.publish("user/feeds/esptemp", str(suhu))
	c.publish("user/feeds/esphum", str(kelembaban))
	time.sleep(60*10)
	

	#time.sleep(0.5)



#for i in range(1,20):
while True:
	try:
		monitor()
	except OSError:
		pass
	
