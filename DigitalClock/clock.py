
import time
import os
from settings import *

print()
while loopCounter < secondsLimit:
    localtime = time.localtime()
    os.system("cls")
    print(time.strftime("%H:%M:%S", localtime))
    print(time.strftime("%I:%M:%S %p", localtime))
    time.sleep(1)
    loopCounter += 1
print()
    