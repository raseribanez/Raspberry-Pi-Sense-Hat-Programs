# Ben Woodfield
# This draws the Pi Logo with a smiley Face  
# Logo image taken from demo. I added the face to it

from sense_hat import SenseHat

sense = SenseHat()

G = [0,255,0]
R = [255,0,255]
O = [0,0,0]
B = [0,0,255]
L = [178,34,34]

pilogo = [
O, G, G, O, O, G, G, O, 
O, O, G, G, G, G, O, O,
O, O, R, R, R, R, O, O, 
O, R, B, R, R, B, R, O,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
O, R, L, L, L, L, R, O,
O, O, R, R, R, R, O, O,
]

    
sense.set_pixels(pilogo)
