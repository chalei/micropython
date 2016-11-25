import network
import time
import json
import urequests
import machine

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("ssid", "password")
sta.ifconfig()
relay = machine.Pin(5, machine.Pin.OUT)

def monitor():
	#mengambil data dari accuweather
	r = urequests.get("http://apidev.accuweather.com/currentconditions/v1/202242.json?language=en&apikey=hoArfRosT1215").json()
	suhu = r[0]['Temperature']['Metric']['Value']
	waktu = r[0]['LocalObservationDateTime']
	jam = waktu[11] + waktu[12] + waktu[13] + waktu[14] + waktu[15]
	#mengambil data dari ubidots
	u = urequests.get("<URL dan API dari ubidots>").json()
	dataRelay = u['results'][0]['value']
	print("Pada jam:", jam)
	print("Suhu di Tangerang adalah", suhu, "C")
	print(dataRelay)

	if dataRelay > 0:
		print("Relay Nyala")
		relay.high()
	else:
		print("Relay Mati")
		relay.low()
	time.sleep(1)

while True:	
	monitor()
	
