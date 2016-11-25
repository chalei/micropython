import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

while True:
	led.low()
	time.sleep(0.5)
	led.high()
	time.sleep(0.5)
