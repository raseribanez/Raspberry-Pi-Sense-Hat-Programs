'''
  NOTE the scroll_sopeed seems ok in this browser emulator, 
  at least it is on my system, BUT I ran it on the Raspberry Pi
  and it was waaaaay too fast to read the scrolling message
  
  It is 0.5 here and that is slow on my browser, so I changed
  it to 0.2 and it sped up nicely...but if you run that speed 
  on the Pi it is too fast.
  
  I think it may just be my internet connection speed and PC
  so in different systems it may run better
  
  To change it, go to LINES 236 and 246 and adjust the scroll_speed
'''

# Ben Woodfield - 06.12.2016
# NOT FINISHED I am still working on this on the Trinket site

# This is a cartoon or animation based on the little joke
# when you type import antigravity into a Python shell

# The cartoon shows a little robot, rolling into the screen, 
# then typing 'import antigravity' then he goes floating off!
# Theres 16 frames, or images, and 2 breaks / messages in the animation loop

# you could wrap the entire thing into a class, or make a function
# to handle the main animation!

# Import the modules
from sense_hat import SenseHat
import time

sense = SenseHat()

# RGB Values / Variables
# Main animation colors
B = [0,255,255]           # aqua (light blue)
G = [0,255,0]             # lime
P = [255,255,255]         # white
W = [128,128,128]         # gray
O = [0,0,0]               # none (black)

# The Pi Logos new colors - some were above so just used them
R = [255,0,255]           # red
X = [0,0,255]             # blue
L = [178,34,34]           # firebrick (dark red)

# The Python Logos new colors
F = [255,255,0]           # yellow]


# The first animation images
screen = [
B, B, B, B, B, B, B, B,  
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B, 
B, B, B, B, B, B, B, B, 
B, B, B, B, B, B, B, B,
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G, 
] 

screen1 = [
B, B, B, B, B, B, B, B,  
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, P, P, 
B, B, B, B, B, B, P, P, 
B, B, B, B, B, B, B, P,
G, G, G, G, G, G, G, P, 
G, G, G, G, G, G, G, W, 
G, G, G, G, G, G, W, W, 
] 

screen2 = [
B, B, B, B, B, B, B, B,  
B, B, B, B, B, B, B, B,
B, B, B, B, B, P, P, B, 
B, B, B, B, B, P, P, B, 
B, B, B, B, B, B, P, B,
G, G, G, G, G, G, P, G, 
G, G, G, G, G, G, W, G, 
G, G, G, G, G, W, W, W 
] 

screen3 = [
B, B, B, B, B, B, B, B,  
B, B, B, B, B, B, B, B,
B, B, B, B, P, P, B, B, 
B, B, B, B, P, P, B, B, 
B, B, B, B, B, P, B, B,
G, G, G, G, G, P, G, G, 
G, G, G, G, G, W, G, G, 
G, G, G, G, W, W, W, G 
] 

screen4 = [
B, B, B, B, B, B, B, B,  
B, B, B, B, B, B, B, B,
B, B, B, P, P, P, B, B, 
B, B, B, P, P, P, B, B, 
B, B, B, B, P, B, B, B,
G, G, G, G, P, G, G, G, 
G, G, G, G, W, G, G, G, 
G, G, G, W, W, W, G, G 
] 

screen5 = [
B, B, B, B, B, B, B, B,  
B, B, B, B, B, B, B, B,
B, B, B, P, P, P, B, B, 
B, B, B, P, P, P, B, B, 
B, B, B, B, P, B, B, B,
G, G, G, G, P, G, G, G, 
G, G, G, W, W, W, G, G, 
G, G, G, W, W, W, G, G 
] 

screen6 = [
B, B, B, B, B, B, B, B,  
B, B, B, B, B, O, O, B,
B, B, B, P, P, O, O, B, 
B, B, B, P, P, P, B, B, 
B, B, B, B, P, B, B, B,
G, G, G, G, P, G, G, G, 
G, G, G, W, W, W, G, G, 
G, G, G, W, W, W, G, G 
] 

##======================================================##

# The second animation images
screen7 = [
B, B, B, B, B, B, B, B,  
B, B, B, B, B, B, B, B,
B, B, B, P, P, P, B, B, 
B, B, B, P, P, P, B, B, 
B, B, B, B, P, B, B, B,
G, G, G, G, P, G, G, G, 
G, G, G, W, W, W, G, G, 
G, G, G, W, W, W, G, G 
] 

screen8 = [
B, B, B, B, B, B, B, B,  
B, B, B, P, P, P, B, B,
B, B, B, P, P, P, B, B, 
B, B, B, B, P, B, B, B, 
B, B, B, B, P, B, B, B,
G, G, G, G, W, G, G, G, 
G, G, G, W, W, W, G, G, 
G, G, G, G, G, G, G, G 
] 

screen9 = [
B, B, B, P, P, P, B, B,  
B, B, B, P, P, P, B, B,
B, B, B, B, P, B, B, B, 
B, B, B, B, P, B, B, B, 
B, B, B, B, W, B, B, B,
G, G, G, W, W, W, G, G, 
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G 
] 

screen10 = [
B, B, B, P, P, P, B, B,  
B, B, B, B, P, B, B, B,
B, B, B, B, P, B, B, B, 
B, B, B, B, W, B, B, B, 
B, B, B, W, W, W, B, B,
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G 
] 

screen11 = [
B, B, B, B, P, B, B, B,  
B, B, B, B, P, B, B, B,
B, B, B, B, W, B, B, B, 
B, B, B, W, W, W, B, B, 
B, B, B, B, B, B, B, B,
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G 
] 

screen12 = [
B, B, B, B, P, B, B, B,  
B, B, B, B, W, B, B, B,
B, B, B, W, W, W, B, B, 
B, B, B, B, B, B, B, B, 
B, B, B, B, B, B, B, B,
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G 
] 

screen13 = [
B, B, B, B, W, B, B, B,  
B, B, B, W, W, W, B, B,
B, B, B, B, B, B, B, B, 
B, B, B, B, B, B, B, B, 
B, B, B, B, B, B, B, B,
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G 
]

screen14 = [
B, B, B, W, W, W, B, B,  
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B, 
B, B, B, B, B, B, B, B, 
B, B, B, B, B, B, B, B,
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G 
]

screen15 = [
B, B, B, B, B, B, B, B,  
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B, 
B, B, B, B, B, B, B, B, 
B, B, B, B, B, B, B, B,
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G, 
G, G, G, G, G, G, G, G 
]

##======================================================##

# Raspberry Pi Logo
pi_logo = [
O, G, G, O, O, G, G, O, 
O, O, G, G, G, G, O, O,
O, O, R, R, R, R, O, O, 
O, R, R, R, R, R, R, O,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
O, R, R, R, R, R, R, O,
O, O, R, R, R, R, O, O,
]

# Raspberry Pi Logo 2
pi_logo2 = [
O, G, G, O, O, G, G, O, 
O, O, G, G, G, G, O, O,
O, O, R, R, R, R, O, O, 
O, R, X, R, R, X, R, O,
R, R, R, R, R, R, R, R,
R, L, R, R, R, R, L, R,
O, R, L, L, L, L, R, O,
O, O, R, R, R, R, O, O,
]


##======================================================##


# Arrange the images into 2 lists for the animation sequences
picList  = [screen,screen1,screen2,screen3,screen4,screen5,screen6]
picListB = [screen7,screen8,screen9,screen10,screen11,screen12,screen13,screen14,screen15] 

# Start the first animation loop
while True:
    for image in picList:
        sense.set_pixels(image)
        time.sleep(0.5)
    break
  
# First break / message  
sense.show_message('import antigravity...', scroll_speed=0.05, text_colour=[255,255,0], back_colour=[0,0,255])

# Start the second animation loop
while True:
    for image in picListB:
        sense.set_pixels(image)
        time.sleep(0.5)
    break
  
# Second break / message  
sense.show_message('The Power of Python....by Ben Woodfield', scroll_speed=0.05, text_colour=[255,255,0], back_colour=[0,0,255])
# End display images
sense.set_pixels(pi_logo)
time.sleep(2)
sense.set_pixels(pi_logo2)
#time.sleep(3)

##======================================================##

''' 
STILL TO DO
*  Show a final Python Logo
*  Show a final Pi logo ### DONE
'''

# This can be used to clear the screen of LED's if needed when testing
#sense.clear()

##======================================================##

'''
    Every time you create a new frame or image
    Use this line for testing them on the screen / sense hat
    You can test an image by ONLY running the import sensehat line, the sense = SenseHat(line
    the color variables, the image you draw (grid)
    Then this one line below will allow you to display your grid image for testing
    this is how I create animations by drawing and testing images/frames one by one
'''
#sense.set_pixels(screen4)
