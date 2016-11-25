import machine 
import time
import dht

sensor = dht.DHT22(machine.Pin(2))

sensor.measure()
time.sleep(3)
delay = 0.5

for i in range(10):
	sensor.measure()
#	time.sleep(delay)
	print('kelembaban', sensor.humidity())
	time.sleep(delay)
	print('suhu', sensor.temperature())
	time.sleep(delay)
