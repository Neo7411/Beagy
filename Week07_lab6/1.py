from sense_hat import SenseHat
import time

# 1.1 Import necessary libraries
sense = SenseHat()

# 1.2 Create an object from the SenseHat class
delay_val = 1.0  # 1.3 Define a variable which controls the blink rate delay

# 1.4 Define on/off patterns
w = (255,255,255)
n = (0,0,0)

on = [w] * 64
off = [n] * 64

# 1.5 Create event handlers to control the delay value for different joystick events
def delay_up(event):
    global delay_val
    if event.action == 'pressed':
        delay_val = 0.1

def delay_down(event):
    global delay_val
    if event.action == 'pressed':
        delay_val = 0.2

def delay_left(event):
    global delay_val
    if event.action == 'pressed':
        delay_val = 0.3

def delay_right(event):
    global delay_val
    if event.action == 'pressed':
        delay_val = 0.4

def delay_middle(event):
    global delay_val
    if event.action == 'pressed':
        delay_val = 0.5
    elif event.action == 'released':
        delay_val = 1.0

# 1.6 Define joystick’s trigger events
sense.stick.direction_up = delay_up
sense.stick.direction_down = delay_down
sense.stick.direction_left = delay_left
sense.stick.direction_right = delay_right
sense.stick.direction_middle = delay_middle

# 1.7 Main loop
while True:
    sense.set_pixels(on)
    time.sleep(delay_val)
    sense.set_pixels(off)
    time.sleep(delay_val)
