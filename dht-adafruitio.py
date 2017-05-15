import time
import machine
import ssd1306
import dht
import network
from umqtt.simple import MQTTClient

yourWifiSSID = "RAHARJA"
yourWifiPassword = " "
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(yourWifiSSID, yourWifiPassword)
while not sta_if.isconnected():
  pass

#sensor.measure()

myMqttClient = "miket-mqtt-client"  # can be anything unique
adafruitIoUrl = "io.adafruit.com" 
adafruitUsername = "username"  # can be found at "My Account" at adafruit.com
adafruitAioKey = "adafruit-key"  # can be found by clicking on "VIEW AIO KEYS" when viewing an Adafruit IO Feed
c = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)

c.connect()


i2c = machine.I2C(-1, scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(64, 48, i2c)
oled.text('Monitor', 0, 0)
oled.text('Suhu', 10, 10)
oled.text('SBMPTN', 0, 30)
oled.text('Demo', 10, 40)

oled.show()
sensor = dht.DHT22(machine.Pin(2))
sensor.measure()
kelembaban = sensor.humidity()
suhu = sensor.temperature()
c.publish("chalei/feeds/esptemp", str(suhu))  #publish num free bytes on the Heap
  #c.subscribe("chalei/feeds/digital")
print("send ok")
time.sleep(2)	



def monitor():
	
	print('kelembaban: {0:0.2f}'.format(kelembaban))
	datahumid = '{0:0.2f}'.format(kelembaban)
	oled.fill(0)
	oled.text('Suhu', 0, 0)
	oled.text(str('{0:0.2f}'.format(suhu)), 0, 10)
	oled.text('C', 40, 10)
	oled.text('Lembab', 0, 30)
	oled.text(str(datahumid), 0, 40)
	oled.text('%', 40, 40)
	time.sleep(2)
	oled.show()

	#time.sleep(0.5)



#for i in range(1,20):
while True:
	try:
		monitor()
	except OSError:
		pass
	
