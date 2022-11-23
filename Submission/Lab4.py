#Melody Street 41078250
from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def trinket_logo(G = green, Y = yellow, B = blue, O = nothing):
  
    logo = [
    O, O, O, O, O, O, O, O,
    O, Y, Y, Y, B, G, O, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    O, Y, Y, Y, B, G, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
    
def raspi_logo(G = green, R = red, O = nothing):
    
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus(W = white, O = nothing):
    
    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals(W = white, O = nothing):
    
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def heart(P = pink, O = nothing):
    
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def elephant(o=(0,0,0), c1=(255,255,255), c2=(220,220,220)):
    logo = [
    o, o, c1, c1, o, o, o, o,
    o, c1, c1, c1, c1, c1, c1, o,
    c1, o, c1, c1, c1, c1, c1, c1,
    c1, c1, c1, c1, c1, c1, c1, c1,
    c1, c2, c2, c1, c1, c1, c1, c1,
    c1, o, c1, c1, c1, c1, c1, c1,
    c1, o, c1, c1, o, c1, c1, o,
    c1, o, c2, c1, o, c2, c1, o,
    ]
    return logo

images = [exit, trinket_logo, plus, equals, raspi_logo, heart, elephant]


def getUserChoice():

        

         while True:
            print( "1. Logo \n"
            "2. Plus sign \n"
            "3. Equals sign \n"
            "4. Raspberry \n"
            "5. Heart \n"
            "6. Elephant \n"
            "0. Exit")

            choice = int(input("what do you want to display? type '0' to exit \n"))
  
            try: 
                if(0 <= choice <= 6):
                    
                    if(choice == 1):
                        trinket_logo()
                        s.set_pixels(images[choice % len(images)]())
                    
                    elif(choice == 2):
                        plus()
                        s.set_pixels(images[choice % len(images)]())
                    
                    elif (choice == 3):
                        equals()
                        s.set_pixels(images[choice % len(images)]())
                    elif (choice== 4):
                        raspi_logo()
                        s.set_pixels(images[choice % len(images)]())
                    elif(choice==5):
                        heart()
                        s.set_pixels(images[choice % len(images)]())
                    elif (choice==6):
                        elephant()
                        s.set_pixels(images[choice % len(images)]())
                    elif (choice == 0):
                        break
            except:
                #i don't know why but this isn't working.

                if (choice < 0 or choice > 6):
                    print("unacceptable input")

         return choice
            
getUserChoice()


while True: 
        
        time.sleep(.75)
