from gpiozero import LED, Button
from time import sleep

#BUTTON
#.wait_for_press()
#.wait_for_release()
#.when_pressed()
#.when_released()


led = LED(17)
button = Button(2)

while True:
    button.when_pressed = led.toggle     #switch state of LED
    sleep(0.5)    
