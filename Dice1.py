# Ben Woodfield - DICE ANIMATION
# This was a project I started to get Dice simulation using the SenseHat,
# So I drew out the images using the grids, and have yet do add the random

# What I did manage though was to create an animation where the Hat scrolls
# Through 6 images (a list of images) and has a small time delay inbetween each one

from sense_hat import SenseHat
import random
import time

sense = SenseHat()

b = [0,255,255]
w = [255,255,255]

# Number 1
imageA = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,b,b,w,w,w,
w,w,w,b,b,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

# Number 2
imageB = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,b,b,w,w,b,b,w,
w,b,b,w,w,b,b,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

# Number 3
imageC = [
w,w,w,w,w,w,w,w,
w,w,w,b,b,w,w,w,
w,w,w,b,b,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,b,b,w,w,b,b,w,
w,b,b,w,w,b,b,w,
w,w,w,w,w,w,w,w
]

# Number 4
imageD = [
w,w,w,w,w,w,w,w,
w,b,b,w,w,b,b,w,
w,b,b,w,w,b,b,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,b,b,w,w,b,b,w,
w,b,b,w,w,b,b,w,
w,w,w,w,w,w,w,w
]

# Number 5
imageE = [
b,b,w,w,w,w,b,b,
b,b,w,w,w,w,b,b,
w,w,w,w,w,w,w,w,
w,w,w,b,b,w,w,w,
w,w,w,b,b,w,w,w,
w,w,w,w,w,w,w,w,
b,b,w,w,w,w,b,b,
b,b,w,w,w,w,b,b
]

# Number 6
imageF = [
w,b,b,w,w,b,b,w,
w,b,b,w,w,b,b,w,
w,w,w,w,w,w,w,w,
w,b,b,w,w,b,b,w,
w,b,b,w,w,b,b,w,
w,w,w,w,w,w,w,w,
w,b,b,w,w,b,b,w,
w,b,b,w,w,b,b,w
]

diceList = [imageA, imageB, imageC, imageD, imageE, imageF]

while True:
    for image in diceList:
        sense.set_pixels(image)
        sleep(0.5)



# If you just want to test a particular image from the series
# comment out the while loop
# and uncomment this line below...changing the image name(Letter)

#sense.set_pixels(imageF)


