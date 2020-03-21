#hardware platform: ESP32
import network
import time
import json
import urequests

from machine import Pin,SPI
import ssd1306
from time import sleep

spi = SPI(2, baudrate=80000000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
lcd = ssd1306.SSD1306_SPI(128, 64, spi, Pin(4), Pin(2), Pin(5))

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("SSID", "PASSWORD")
print(sta.ifconfig())
sleep(2)

lcd.fill(0)
lcd.text("Total Kasus",0,0)
lcd.text("Corona Indonesia",0,10)
lcd.text("Untuk Hari ini",0,20)
lcd.show()
sleep(1)
lcd.fill(0)
lcd.text("Mengambil Data",0,0)
lcd.text("Terbaru",20,10)

lcd.show()
sleep(1)

def disp_data():
  c = urequests.get("https://corona.lmao.ninja/countries/indonesia").json()
  kasus = c['cases']
  meninggal = c['deaths']
  sembuh = c['recovered']
  lcd.fill(0)
  lcd.text("Total Kasus",0,0)
  lcd.text(str(kasus),20,10)
  lcd.text("Meninggal",0,20)
  lcd.text(str(meninggal),20,30)
  lcd.text("Sembuh",0,40)
  lcd.text(str(sembuh),20,50)
  lcd.show()
  sleep(5)
  
while True:
    disp_data()
  
  
  
  
  


