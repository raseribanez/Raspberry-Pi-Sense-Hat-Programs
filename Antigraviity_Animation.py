# Ben Woodfield - 06.12.2016
# NOT FINISHED I am still working on this on the Trinket site

# This is a cartoon or animation based on the little joke
# when you type import antigravity into a Python shell

# The cartoon shows a little robot, rolling into the screen, 
# then typing 'import antigravity' then he goes floating off!
# Theres 16 frames, or images, and 2 breaks / messages in the animation loop

# you could wrap the entire thing into a class, or make a function
# to handle the main animation!

from sense_hat import SenseHat
import time

sense = SenseHat()

# RGB Values / Variables
B = [0,255,255]
G = [0,255,0]
P = [255,255,255]
W = [128,128,128]
O = [0,0,0]


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
sense.show_message('import antigravity...', scroll_speed=0.02, text_colour=[255,255,0], back_colour=[0,0,255])

# Start the second animation loop
while True:
    for image in picListB:
        sense.set_pixels(image)
        time.sleep(0.5)
    break
  
# Second break / message  
sense.show_message('The power of PYTHON....by Ben Woodfield', scroll_speed=0.02, text_colour=[255,255,0], back_colour=[0,0,255])

##======================================================##

''' 
STILL TO DO
*  Show a final Python Logo
*  Show a final Pi logo
'''

# This can be used to clear the screen of LED's if needed
#sense.clear()

##======================================================##

'''
    Every time you create a new frame or image
    Use this line for testing them on the screen / sense hat
'''
#sense.set_pixels(screen4)
