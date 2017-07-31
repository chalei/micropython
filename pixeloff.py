from machine import Pin
from neopixel import NeoPixel

pin = Pin(2, Pin.OUT) # the NeoPixel is on GPIO2
np = NeoPixel(pin, 3) # only one pixel is connected

np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np[2] = (0, 0, 0)
np.write()