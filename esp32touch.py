'''
   Touch Sensor Pin Layout
   T0 = GPIO4
   T1 = GPIO0
   T2 = GPIO2
   T3 = GPIO15
   T4 = GPIO13
   T5 = GPIO12
   T6 = GPIO14
   T7 = GPIO27
   T8 = GPIO33
   T9 = GPIO32'''
   
from machine import TouchPad, Pin
from time import sleep

touch = TouchPad(Pin(15))
led = Pin(17, Pin.OUT)



while True:
    data = touch.read()
    print(data)
    if (data > 2):
      led.value(0)
      
    else:
      led.value(1)
  
	

