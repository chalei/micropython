import network
import json
import urequests
from machine import Pin
from neopixel import NeoPixel
from time import sleep

pin = Pin(2, Pin.OUT)
np = NeoPixel(pin, 3)

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("ssid", "passwrd")
sta.ifconfig()

def monitor():
	#mengambil data dari accuweather
	r = urequests.get("http://apidev.accuweather.com/currentconditions/v1/202242.json?language=en&apikey=hoArfRosT1215").json()
	suhu = r[0]['Temperature']['Metric']['Value']
	waktu = r[0]['LocalObservationDateTime']
	jam = waktu[11] + waktu[12] + waktu[13] + waktu[14] + waktu[15]
	#mengambil data dari ubidots
	
	print("Pada jam:", jam)
	print("Suhu di Tangerang adalah", suhu, "C")
	
	if suhu < 26:
		np[0] = (0, 0, 255)
		np[1] = (0, 0, 255)
		np[2] = (0, 0, 255)
		np.write()
	else:
		np[0] = (255,255, 0)
		np[1] = (255, 255, 0)
		np[2] = (255, 255, 0)
		np.write()
	sleep(1)
	

#for i in range(1,10):
while True:	
	monitor()
	
