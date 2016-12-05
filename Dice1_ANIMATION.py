# Ben Woodfield - DICE ANIMATION
# So this one is one oof my own
# This is an animation, you can change the grids to diaplay any images using coloured LED's as pixels
# Then update the list if you add more images. If you create RGB variables, assign them to a single letter
# so you can add them to the grid nicely...so far this only has blue and white (b and w)
#
# This was a project I started to get Dice simulation using the SenseHat,
# So I drew out the numbered images using the grids, and have yet do add the random capability
#
# What I did manage though was to create an animation where the Hat scrolls through a series of
# 6 images (a list of images) and has a small time delay inbetween each one. You could make a little cartoon
# The API requires it's own commands, and it's just a case of figuring out how to interact with random

from sense_hat import SenseHat
#import random
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
        time.sleep(0.5)



# If you just want to test a particular image from the series
# comment out the while loop
# and uncomment this line below...changing the image name(Letter)

#sense.set_pixels(imageF)


