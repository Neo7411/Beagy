from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

def falling(p0):
    z=round(127-0.12*p0)
    if z==1:
        print('Settle fine')
    elif z==2:
        print('Weather fine')
    elif z==3:
        print('fine becoming less settled')
    elif z==4:
        print('Fairly Fine, Showery Later')
    elif z==5:
        print('Showery, Becoming More Unsettled')
    elif z==6:
        print('Unsettled, Rain Later')   
    elif z==7:
        print('Rain at Times, Worse Later')
    elif z==8:
        print('Rain at Times, Becoming Very Unsettled')
    elif z==9:
        print('Very Unsettled, Rain')
    else:
        print('Error')
    
def steady(p0):
    z=round(144-0.13*p0)
    if z==10:
        print('Settle fine')
    elif z==11:
        print('Weather fine')
    elif z==12:
        print('Fine, Possibly Showers')
    elif z==13:
        print('Fairly Fine, Showers Likely')
    elif z==14:
        print('Showery, Bright Intervals')
    elif z==15:
        print('Changeable, Some Rain')   
    elif z==16:
        print('Unsettled, Rain at Times')
    elif z==17:
        print('Rain at Frequent Intervals')
    elif z==18:
        print('Very Unsettled, Rain')
    else:
        print('Error')
        
        
def rising(p0):
    z=round(185-0.16*p0)
    if z==20:
        print('Settle fine')
    elif z==21:
        print('Weather fine')
    elif z==22:
        print('Becoming Fine')
    elif z==23:
        print('Fairly Fine, Improving')
    elif z==24:
        print('Fairly Fine, Possibly Showers Early')
    elif z==25:
        print(' Showery Early, Improving')   
    elif z==26:
        print('Changeable, Mending')
    elif z==27:
        print('Rather Unsettled, Clearing Later')
    elif z==28:
        print('Unsettled, Probably Improving')
    elif z==29:
        print(' Unsettled, Short Fine Intervals')
    elif z==30:
        print('Very Unsettled, Finer at Times')   
    elif z==31:
        print('Stormy, Possibly Improving')
    elif z==32:
        print('Stormy, Much Rain')
    else:
        print('Error')
    
    
    



while True:
    p = sense.get_pressure()
    t = sense.get_temperature()
    h = 125
    p0 = p * pow((1 - (0.0065 * h / (t + 0.0065 * h + 273.15))), -5.257)
    sleep(5)
    p2=sense.get_pressure()
    dp=(p2-p)
    
    if(dp==0.0 and p>=960 and p<=1033):
        steady(p0)
    elif(dp<0.0  and p>=985 and p<=1050):
        falling(p0)
    elif(dp>0.0 and p>=947 and p<=1030):
        rising(p0)
    else:
        print('Error')
