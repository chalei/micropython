import charlieplex
from machine import Pin, I2C
from time import sleep
i2c = I2C(scl=Pin(22), sda=Pin(21))
display = charlieplex.Matrix(i2c)
display.fill(0)
x = 0
y = 0
while True:
  display.pixel(y, x, 255)
  x += 1
  print(x, y)
  if( x > 7):
    x = 0
    y += 1
    
    if(y>7):
      display.fill(0)
      x = 0
      y = 0
  sleep(0.5)
  