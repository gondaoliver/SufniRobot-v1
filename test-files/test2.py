import time

import RPi.GPIO as GPIO

GPIO.cleanup()
time.sleep(3)

# Use Broadcom (BCM) pin numbering
GPIO.setmode(GPIO.BCM)

# Select a GPIO pin; for example, GPIO18
control_pin = 18

# Set up the pin asccc an output
GPIO.setup(control_pin, GPIO.OUT)

try:
        while True:
                GPIO.output(control_pin, GPIO.LOW)
                print("Led ki")
                time.sleep(1)
                
                GPIO.output(control_pin, GPIO.HIGH)
                print("Led be")
                time.sleep(1)


finally:
        GPIO.cleanup()
