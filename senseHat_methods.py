# Ben woodfield
# Sense Hat examples

# The basic set-up to scroll a message
from sense_hat import SenseHat
sense = SenseHat()
sense.show_message("Ben Loves Sian")

# This changes the scrolling speed, text colour, and bg colour
from sense_hat import SenseHat
sense = SenseHat()
sense.show_message("Astro Pi is awesome!!", scroll_speed=0.05, text_colour=[255,255,0], back_colour=[0,0,255])


# This makes it loop
sense = SenseHat()
while True:
    sense.show_message("Astro Pi is awesome!!", scroll_speed=0.05, text_colour=[255,255,0], back_colour=[0,0,255])
