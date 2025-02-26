import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

p = GPIO.PWM(14, 100)  # PWM frequency is 50Hz
p.start(5)  # Initialization

try:
    while True:
        print("90 fok előre")
        p.ChangeDutyCycle(25.5)


except KeyboardInterrupt:
    print("Program vége")    
    p.stop()
    GPIO.cleanup()
