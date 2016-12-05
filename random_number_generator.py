# RGB Random number generator for sensehat - shows a letter aswell

from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

r = randint(0,255)
sense.show_letter("O", text_colour=[r, 0, 0])
sleep(1)

r = randint(0,255)
sense.show_letter("M", text_colour=[0, 0, r])
sleep(1)

r = randint(0,255)
sense.show_letter("G", text_colour=[0, r, 0])
sleep(1)

sense.show_letter("!", text_colour=[0, 0, 0], back_colour=[255, 255, 255])
sleep(1)
sense.clear()
Click File -- Save As,
