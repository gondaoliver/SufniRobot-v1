import RPi.GPIO as GPIO
import time
import keyboard

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)  
p.start(2.5)

try:
    while True:
        if keyboard.is_pressed('w'):
            print("90 fok előre")
            p.ChangeDutyCycle(5)
        elif keyboard.is_pressed('s'):
            print("180 fok hátra")
            p.ChangeDutyCycle(10)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program vége")    
    p.stop()
    GPIO.cleanup()
