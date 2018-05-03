from gpiozero import LED
from time import sleep

#LED
#.on()
#.off()
#.toggle()

sunshine = LED(17)

while True:
    print("LED on")
    sunshine.on()
    sleep(1)
    print("LED off")
    sunshine.off()
    sleep(1.5)



