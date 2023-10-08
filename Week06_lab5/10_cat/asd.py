from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

h = (0,0,0) #no color
r = (246, 191, 210)
z = (0,46,0)
s=(222, 228, 102)



cat1_img = [h,h,h,h,h,h,h,h,
           r,h,h,h,h,h,h,h,
           h,r,h,h,r,h,r,h,
           h,r,z,z,r,s,s,h,
           h,z,z,z,s,h,s,z,
           h,z,z,z,z,s,s,h,
           h,z,h,z,h,z,h,h,
           h,h,h,h,h,h,h,h]
               
cat2_img = [h,h,h,h,h,h,h,h,
           r,h,h,h,h,h,h,h,
           h,r,h,h,r,h,r,h,
           h,r,z,z,r,s,s,h,
           h,z,z,z,s,h,s,z,
           h,z,z,z,z,s,s,h,
           h,h,z,h,z,h,h,h,
           h,h,h,h,h,h,h,h]

def move(f):
    if(f>1.0):
        sense.set_pixels(cat1_img)
        sense.clear()
        sense.set_pixels(cat2_img)
    else:
        sense.set_pixels(cat1_img)
    
    
    
    
    



while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)
    sense.set_pixels(cat1_img)
    f=pow((x**2+y**2+z**2),(1/2))
    move(f)
    sleep(2)
    print(f)

