# Set 2 pixels to the screen

# the blue pixel is at coordinates (0, 2)
# the red pixel is at coordinates (7, 4)

from sense_hat import SenseHat

sense = SenseHat()

sense.set_pixel(0, 2, [0, 0, 255])
sense.set_pixel(7, 4, [255, 0, 0])
