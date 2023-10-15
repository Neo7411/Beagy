import time
import random
from sense_hat import SenseHat

# Create an instance of the SenseHat class
sense = SenseHat()

# Define the blue color
blue = (0, 0, 255)
black = (0, 0, 0)

# Initialize the LED matrix with all LEDs turned off
display = [black] * 64

# Function to create rain effect
def rain_effect():
    while True:
        # Randomly turn on a LED in the first row with blue color
        index = random.randint(0, 7)
        display[index] = blue
        
        # Update the LED matrix display
        sense.set_pixels(display)

        # Wait for 500ms
        time.sleep(0.5)

        # Shift all rows down
        for i in range(55, -1, -1):
            display[i+8] = display[i]

        # Turn off the LEDs in the first row
        for i in range(8):
            display[i] = black

# Create rain effect
rain_effect()
