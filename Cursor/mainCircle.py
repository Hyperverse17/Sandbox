


import math
import time
import pyautogui
import keyboard

goahead       = True
counter       = 0
maxLoops      = 10
radius        = 10

# Obteniendo información de la pantalla:
screenWidth, screenHeight = pyautogui.size()

# Coordenadas del centro:
h = screenWidth // 2
k = screenHeight // 2

try:
    print("Moving...")
    print("")
    while goahead == True:
        for theta in range (0,361,30):
            radians = math.radians(theta)
            cosTheta = round(math.cos(radians),2)
            sinTheta = round(math.sin(radians),2)

            x = h + (radius*cosTheta)
            y = k + (radius*sinTheta)

            pyautogui.moveTo(x,y,duration=0)
        
        counter += 1
        if counter > maxLoops:
            print("leaving...")
            print("")
            break

except:
    print("Something went wrong")

finally:
    print("Finished Program")
    time.sleep(3)









