from machine import Pin
import time
import dht
sensor = dht.DHT11(Pin(2))
delay = 1

while True:
	sensor.measure()
	time.sleep(delay)
	print(sensor.temperature(), "C")
	time.sleep(delay)
	print(sensor.humidity(), "persen")
	time.sleep(delay)