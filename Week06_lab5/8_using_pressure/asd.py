from sense_hat import SenseHat


sense = SenseHat()


p=sense.get_pressure()

h= 44331*(pow((1-(p/1013.25)),(1/5.2558)))

print('Height: '+h)


