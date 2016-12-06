# Ben Woodfield
# Sense Hat Raspberry Pi Logo - used in my cartoon

from sense_hat import SenseHat
import time

sense = SenseHat()

G = [0,255,0]
R = [255,0,255]
O = [0,0,0]

pi_logo = [
O, G, G, O, O, G, G, O, 
O, O, G, G, G, G, O, O,
O, O, R, R, R, R, O, O, 
O, R, R, R, R, R, R, O,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
O, R, R R, R, R, R, O,
O, O, R, R, R, R, O, O,
]

sense.set_pixels(pi_logo)
