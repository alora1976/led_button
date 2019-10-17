from gpiozero import Button
from time import sleep
from gpiozero import LED
from signal import pause




button=Button(17)
blue=LED(14)
red=LED(23)
green=LED(24)


        

while True:
    
   
    blue.on()
    sleep(.3)
    blue.off()
    red.on()
    sleep(.3)
    red.off()
    green.on()
    sleep(.3)
    green.off()
   
    if button.is_pressed:
        print("Button was Pressed")
        pause()
        
    else:
        print("Press Button to Stop Light")
    
    
    
    
    
    

    
    


    
    