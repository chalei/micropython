import time
import machine
import ssd1306
import dht



#sensor.measure()


i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
oled = ssd1306.SSD1306_I2C(64, 48, i2c)
oled.text('Micro', 0, 0)
oled.text('Python', 10, 10)
oled.text('Weather', 0, 30)
oled.text('Station', 10, 40)

oled.show()
sensor = dht.DHT22(machine.Pin(2))
time.sleep(2)	



def monitor():
	sensor.measure()
	kelembaban = sensor.humidity()
	suhu = sensor.temperature()
	print('kelembaban: {0:0.2f}'.format(kelembaban))
	datahumid = '{0:0.2f}'.format(kelembaban)
	oled.fill(0)
	oled.text('suhu', 0, 0)
	oled.text(str('{0:0.2f}'.format(suhu)), 0, 10)
	oled.text('humid', 0, 20)
	oled.text(str(datahumid), 0, 30)
	time.sleep(2)
	oled.show()

	#time.sleep(0.5)



#for i in range(1,20):
while True:
	try:
		monitor()
	except OSError:
		pass
	