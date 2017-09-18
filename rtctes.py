#test the DS1307 rtc module with esp8266

import urtc
from machine import Pin, I2C
from time import sleep


i2c = I2C(scl=Pin(5), sda=Pin(4))
rtc = urtc.DS1307(i2c)
datetime = rtc.datetime()
print(datetime)
led = Pin(2, Pin.OUT)
led(1)
while True:
  datetime = rtc.datetime()
  print(datetime.hour, datetime.minute, datetime.second)
  if (datetime.second == 0):
    led(0)
    sleep(1)
    led(1)
  else:
    led(1)
  sleep(1)
