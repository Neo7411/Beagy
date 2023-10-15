from sense_hat import SenseHat
import time

sense = SenseHat()

state = 0

w = (255,255,255)
r = (255,0,0)
g = (0,255,0)
y = (255,255,0)
n = (0,0,0)

red = [
 n, n, n, r, r, n, n, n,
 n, n, n, r, r, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]

red_yellow = [
 n, n, n, r, r, n, n, n,
 n, n, n, r, r, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]

yellow = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]

green = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, g, g, n, n, n,
 n, n, n, g, g, n, n, n
 ]


def set_state():
    global state
    # state variable has been defined outside
    if state < 3:
        state += 1
    elif state == 3:
        state = 0
    else:
        pass
def button_event(event):
    global state
    if event.action == 'released':
        if state != 4: 
            state = 4
        else:   
            state = 3

def reset_event(event):
    global state
    if event.action == 'released':
        sense.clear()
        time.sleep(2)
        state = 0



def state_control(state):
    if state == 0:
        sense.set_pixels(red)
        time.sleep(3)
        sense.clear()
    elif state == 1:
        sense.set_pixels(red_yellow)
        time.sleep(1)
        sense.clear()
    elif state == 2:
        sense.set_pixels(green)
        time.sleep(2)
        sense.clear()
    elif state == 3:
        sense.set_pixels(yellow)
        time.sleep(1)
        sense.clear()
    else:
        sense.set_pixels(yellow)
        time.sleep(0.5)
        sense.clear()
        time.sleep(0.5)


def main():
    global state
    sense.stick.direction_middle = button_event
    sense.stick.direction_up = reset_event
    while True:
        state_control(state)
        set_state()
main()