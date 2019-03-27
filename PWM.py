import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

pwm = GPIO.PWM(7,50)

pwm.start(0) #Starts the PWM.

try:
    while True:
        for i in range(100): 
         pwm.ChangeDutyCycle(i)
         sleep(0.04)
        for i in range(100, 0, -1): #Changes PWN 100 to 0 by -1.
         pwm.ChangeDutyCycle(i)
         sleep(0.04)

except KeyboardInterrupt:  #For shutting the program using keyboard.
    pass

pwm.stop()
GPIO.cleanup()
