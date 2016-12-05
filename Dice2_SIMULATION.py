# Ben Woodfield - DICE SIMULATION

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


# Make a list out of all the dice numbers
diceList = [imageA, imageB, imageC, imageD, imageE, imageF]

# Display a random number
sense.set_pixels(random.choice(diceList))
