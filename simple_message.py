from sense_hat import SenseHat

# Basic RGB Values

# White   [255, 255, 255]
# Black   [  0,   0,   0]
# Red     [255,   0,   0]
# Green   [  0, 255,   0] 
# Gray    [128, 128, 128]
# Yellow  [255, 255,   0]
# Navy    [  0,   0, 128]
# Purple  [128,   0, 128]
# Teal    [  0, 128, 128]
# Cyan    [  0, 255, 255]


# Basic Message
ben = SenseHat()
ben.show_message('Bens Message Is THIS!')

# This adds some extra values like scrolling speed, background color and text color
#ben.show_message('Bens Message Is THIS!', scroll_speed=0.05, text_colour=[255,255,0], back_colour=[0,0,255])
