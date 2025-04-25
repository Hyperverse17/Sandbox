
import random
import time
import pyautogui
import keyboard

goahead = True
counter = 1
securityLimit = 10
screenWidth, screenHeight = pyautogui.size()
print("")

try:
    print("Moving...")
    while goahead == True:
        # Obteniendo el centro
        h = screenWidth // 2
        k = screenHeight // 2
        
        # Obteniendo un punto aleatorio
        x = random.randint(0,screenWidth)
        y = random.randint(0,screenHeight)
        
        pyautogui.moveTo(x,y,duration=0.5)
        time.sleep(0.5)
        counter += 1
        if (counter > securityLimit) or (keyboard.is_pressed("enter")):
            print("Process stopped by the user")
            break


except:
    print("Something went wrong")

finally:
    print("Finished Program")
    time.sleep(3)






