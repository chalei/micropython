import network
sta = network.WLAN(network.STA_IF)

#mengambil data dari accuweather
r = urequests.get("http://apidev.accuweather.com/currentconditions/v1/202242.json?language=en&apikey=hoArfRosT1215").json()
#mengambil data dari ubidots
#kelembaban = u['results'][0]['value']
i2c = machine.I2C(machine.Pin(5), machine.Pin(4))

def monitor():

#for i in range(1,20):
	