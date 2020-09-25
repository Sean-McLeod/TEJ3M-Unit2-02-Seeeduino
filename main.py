import time
import board
from digitalio import DigitalInOut, Direction
 
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
lightTime = 1
while True:
    led.value = True
    time.sleep(lightTime)
    led.value = False
    time.sleep(1)
    
    lightTime = lightTime + 1