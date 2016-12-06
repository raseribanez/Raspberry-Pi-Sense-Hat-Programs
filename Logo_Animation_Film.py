# Ben Woodfield
# This draws the Pi Logo with a smiley Face  
# The Trinket site has a little demo of an animation - I took the Pi logo from that to use in my own program
# The adds an animation to it, it's 12 frames or images
# He is being sick and the screen fills up

# Notice his eyes close just before the sick hits that level!!

from sense_hat import SenseHat
import time

sense = SenseHat()

G = [0,255,0]
R = [255,0,255]
O = [0,0,0]
B = [0,0,255]
L = [178,34,34]
E = [128,128,128]
Y = [255,255,0]

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

pilogo1 = [
O, G, G, O, O, G, G, O, 
O, O, G, G, G, G, O, O,
O, O, E, R, R, E, O, O, 
O, R, B, E, E, B, R, O,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
O, R, R, L, L, R, R, O,
O, O, L, R, R, L, O, O,
]

pilogo2 = [
O, G, G, O, O, G, G, O, 
O, O, G, G, G, G, O, O,
O, O, E, R, R, E, O, O, 
O, R, B, E, E, B, R, O,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
O, R, R, L, L, R, R, O,
O, O, R, R, R, R, O, O,
]

pilogo3 = [
O, G, G, O, O, G, G, O, 
O, O, G, G, G, G, O, O,
O, O, E, R, R, E, O, O, 
O, R, B, E, E, B, R, O,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
O, R, L, L, L, L, R, O,
O, O, L, Y, Y, L, O, O,
]

pilogo4 = [
O, G, G, O, O, G, G, O, 
O, O, G, G, G, G, O, O,
O, O, E, R, R, E, O, O, 
O, R, B, E, E, B, R, O,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
O, R, L, L, L, L, R, O,
O, Y, Y, Y, Y, Y, Y, O,
]

pilogo5 = [
O, G, G, O, O, G, G, O, 
O, O, G, G, G, G, O, O,
O, O, E, R, R, E, O, O, 
O, R, B, E, E, B, R, O,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
O, R, Y, Y, Y, Y, R, O,
Y, Y, Y, Y, Y, Y, Y, Y,
]

pilogo6 = [
O, G, G, O, O, G, G, O, 
O, O, G, G, G, G, O, O,
O, O, E, R, R, E, O, O, 
O, R, B, E, E, B, R, O,
R, R, R, R, R, R, R, R,
R, R, Y, Y, Y, Y, R, R,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
]

pilogo7 = [
O, G, G, O, O, G, G, O, 
O, O, G, G, G, G, O, O,
O, O, E, R, R, E, O, O, 
O, R, R, E, E, R, R, O,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
]

pilogo8 = [
O, G, G, O, O, G, G, O, 
O, O, G, G, G, G, O, O,
O, O, E, R, R, E, O, O, 
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
]

pilogo9 = [
O, G, G, O, O, G, G, O, 
O, O, G, G, G, G, O, O,
Y, Y, Y, Y, Y, Y, Y, Y, 
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
]

pilogo10 = [
O, G, G, O, O, G, G, O, 
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y, 
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
]

pilogo11 = [
Y, Y, Y, Y, Y, Y, Y, Y, 
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y, 
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
]

picList = [pilogo,pilogo1,pilogo2,pilogo3,pilogo4,pilogo5,pilogo6,pilogo7,pilogo8,pilogo9,pilogo10,pilogo11]

while True:
    for image in picList:
        sense.set_pixels(image)
        time.sleep(0.5)

#sense.set_pixels(pilogo3)
