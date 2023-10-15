import time
import random
from sense_hat import SenseHat


sense = SenseHat()


blue = (0, 0, 255)
black = (0, 0, 0)


display = [black] * 64



while True:
        
    index = random.randint(0, 7)
    display[index] = blue
        
     
    sense.set_pixels(display)

  
    time.sleep(0.5)

    
    for i in range(55, -1, -1):
        display[i+8] = display[i]

    for i in range(8):
        display[i] = black


