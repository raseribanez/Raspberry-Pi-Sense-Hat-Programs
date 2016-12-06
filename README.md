# Raspberry-Pi-Sense-Hat-Programs
A collection of scripts for the Sense Hat (ALL work on the Sense Hat Emulator, both on the Pi and on Trinket-IO website)

USE:
=====
These scripts will ALL work on any sense hat -  
but if you are using the Raspberry Pi's emulator you will have to change a script's import line like this:
    
    # For online emulators and Hardware version (the real sense hat) the import line is
    from sense_hat import SenseHat
    
    # For the Raspberry Pi's built in Sense Hat emulator (Raspbian Jessie Pixel)
    from sense_emu import SenseHat
    
    # From there you can interact very easily - to write a scrolling message:
    from sense_hat import SenseHat()
    sense = SenseHat()
    sense.show_message('The power of PYTHON....by Ben Woodfield')
    
    # To add colour to text and background, and control the scrolling speed:
    from sense_hat import SenseHat()
    sense = SenseHat()
    sense.show_message('The power of PYTHON....by Ben Woodfield', scroll_speed=0.02, text_colour=[255,255,0], back_colour=[0,0,255])
    
    # You can set your own veriables too - for RGB:
    from sense_hat import SenseHat()
    sense = SenseHat()
    
    blue = [0,255,255]
    green = [0,255,0]
    sense = SenseHat()
    
    #                                                              <Scrolling Speed>    <Text Colour>    <Background Colour>
    sense.show_message('The power of PYTHON....by Ben Woodfield', scroll_speed=0.02, text_colour='blue', back_colour='green')
    
    
To draw a picture with the LED's you have access to all of the RGB values. And you can draw a grid using variable letters. So if I wanted to draw the raspberry Pi logo for example...

    from sense_hat import SenseHat
    
    sense = SenseHat()
    
    # Create the variables to use in the grid - so every G means a green LED
    G = [0,255,0]    # Green for the leaves
    R = [255,0,255]  # Red for the main body
    O = [0,0,0]      # Black shows a NO led for the background
    
    # The sense Hat is an 8 X 8 matrix or grid so you can draw pixelated images within those dimensions
    
    pi_logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]

    # Then draw the picture to the SenseHat using the set_pixels() command
    sense.set_pixels(pi_logo)


 

I have a Raspberry Pi, but Don't have a Sense Hat I just use the Emulator

When I updated my OS for the Pi to Raspbian Jessie Pixel it had a new Sense Hat Emulator, an API like virtual version that you can interact with.

So I know that you are limited like this because you can't make full use of the sensors and amazing things it is capable of, but you CAN still interact with the LED matrix and write games, and fun little programs for it.

I loved this, because you can see your code interact physically with hardware, even if it is only onscreen. So Trinket IO is one of the sites that has an Emulator online for the Sense Hat - it was the best one I tried. It means that you get a virtual image of the Sense Hat and the LED matrix, plus little sliders for the atmospheric sensors...but alongside is a code editor, and you can write code that plays with the SenseHat directly.

MOST of the codes here are a collection of things I found while trying to learn more about codeing the Sense Hat, so a lot aren't my actual work although I hae rewritten them for my own use.

HOWEVER...once I sussed out how simple it is to play with the SenseHat I started to play with my own ideas...I have made a simple animation script, where you set RGB variables to a single letter, then draw a grid with them in an array fashion, like this:

    imageA = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, b, b, w, w, w,
    w, w, w, b, b, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w
    ]

w = [white RGB values]
b = [blue RGB values]

By making a series of them, you create a list, or a sequence and then tell the sense hat to display a list of images - as an animation...I then just put a small time delay inbetween them. The above image is just a blue dot - representing number 1 of a dice. I drew all the numbers and made a dice simulator, in the process learned how to do the animation, so the file Dice1_ANIMATION.py is a template for animation on the sensehat, You could just rewrite the grids to display your own image, and update the rgb list to make new colours.

I may do som elittle cartoons with this but at the moment I am playing with the random for the dice simulator, it isn't as easy as:
    
    choiceList = [1, 2, 3, 4, 5, 6, 7, 8]
    print random.choice(choiceList)
    
because you have to follow the API requirements for interacting with other modules.

UPDATE
=========
Just a little update, I figured out how to do the random side of things... and went with (random.choice) seeing as my dice numbers were stored in a list. I knoew it was random.choice...but just had to suss out how the API would accept it

The dice simulator is Dice2_SIMULATION.py

Its a bit rough around the edges, it literally just shows a random picture using the grid method I showed...I want to add the clear screen to it and have interaction with the user (do you want to roll again?) and also have a little animation before the number shows, to simulate the rolling action!

ALL of the codes here will work on the Real version and the Digital or Virtual version, either online at Trinket.io or on the Raspberry Pi itself using Raspbian Jessie Pixel

Theres some cool stuff here, from little games, to interacting with the Minecraft Pi game! I am not taking credit for any of the work that's not mine, I am just putting what I have found in one place for others to find easily!

NOTE:
=======
There are one ortwo scripts here that require additional modules to be imported to Python

If you use the Online Emulator (trinket.io) then you will find that some won't run because they don't have access to the required modules.

If you run them on the Pi however they will run fine, providing you have them installed. Most I am sure are just Standard Python modules like random and itertools so you will be fine using the Pi
