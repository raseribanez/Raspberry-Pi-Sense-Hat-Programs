# Show temperature and other values in scrolling screen
# Temp has a red background if within a certain range

from sense_hat import SenseHat
sense = SenseHat()

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    if t > 18.3 and t < 26.7:
        bg = [0, 100, 0]  # green
    else:
        bg = [100, 0, 0]  # red

    msg = "Temperature = {0}, Pressure = {1}, Humidity = {2}".format(t, p, h)

    sense.show_message(msg, scroll_speed=0, back_colour=bg)
