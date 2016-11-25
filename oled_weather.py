import network
import time
import json
import urequests
import machine
import ssd1306
import dht


sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("ssid", "password")
#sta.ifconfig()

#print(ip)

sensor = dht.DHT22(machine.Pin(2))

#sensor.measure()
time.sleep(3)
delay = 0.5


#mengambil data dari accuweather

r = urequests.get("http://apidev.accuweather.com/currentconditions/v1/202242.json?language=en&apikey=hoArfRosT1215").json()
suhu = r[0]['Temperature']['Metric']['Value']
waktu = r[0]['LocalObservationDateTime']
jam = waktu[11] + waktu[12] + waktu[13] + waktu[14] + waktu[15]



i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
oled = ssd1306.SSD1306_I2C(64, 48, i2c)
oled.fill(1)
oled.show()
time.sleep(2)	



def monitor():
	sensor.measure()
	kelembaban = sensor.humidity()
	time.sleep(2)
	oled.fill(0)
	oled.text('cuaca', 0, 0)
	oled.text(str(suhu), 0, 10)
	oled.text(jam, 0, 20)
	oled.text(str(kelembaban), 0, 40)
	oled.show()
	print(kelembaban)
	#time.sleep(0.5)



#for i in range(1,20):
while True:
	monitor()

	
