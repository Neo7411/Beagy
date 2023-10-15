from sense_hat import SenseHat
import time

# 3.1 Import necessary libraries
sense = SenseHat()

# 3.2 Create an object from the SenseHat class
# 3.3 Create a variable (p) which keeps track of the rightmost point of the light beam
p = [2, 3]
light_len = 3
space_size = 8
speed = 1/7  # 3.3 Speed of the moving light

# 3.4 Define the initial position of the light beam on the LED matrix
r = (255, 0, 0)
n = (0, 0, 0)

# Initial light position
space = [n] * space_size * space_size
for i in range(light_len):
    space[p[1] * space_size + p[0] - i] = r

sense.set_pixels(space)

# 3.5 Create 2 functions which shift the light beam to the left side and to the right side
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

# 3.6 Main function which is moving the light beam from right to left and left to right continuously
def main():
    while True:
        while p[0] < space_size - 1:
            shift_right()
            time.sleep(speed)
        
        while p[0] > light_len - 1:
            shift_left()
            time.sleep(speed)

# Run the main function
main()
