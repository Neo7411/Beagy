from sense_hat import SenseHat
import time


sense = SenseHat()


p = [2, 3]
light_len = 3
space_size = 8
speed = 1/7 


r = (255, 0, 0)
n = (0, 0, 0)

space = [n] * space_size * space_size
for i in range(light_len):
    space[p[1] * space_size + p[0] - i] = r

sense.set_pixels(space)


def shift_right():
    global p
    p[0] = (p[0] + 1) % space_size
    for i in range(space_size):
        space[p[1] * space_size + i] = n
    for i in range(light_len):
        index = p[1] * space_size + p[0] - i
        if index >= p[1] * space_size:
            space[index] = r
    sense.set_pixels(space)

def shift_left():
    global p
    p[0] = (p[0] - 1) % space_size
    for i in range(space_size):
        space[p[1] * space_size + i] = n
    for i in range(light_len):
        index = p[1] * space_size + p[0] - i
        if index >= p[1] * space_size:
            space[index] = r
    sense.set_pixels(space)


def main():
    while True:
        while p[0] < space_size - 1:
            shift_right()
            time.sleep(speed)
        
        while p[0] > light_len - 1:
            shift_left()
            time.sleep(speed)


main()
