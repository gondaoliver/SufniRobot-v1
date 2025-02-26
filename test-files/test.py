import time

import RPi.GPIO as GPIO

# Use Broadcom (BCM) pin numbering
GPIO.setmode(GPIO.BCM)

# Select a GPIO pin; for example, GPIO18
control_pin = 18

# Set up the pin as an output
GPIO.setup(control_pin, GPIO.OUT)

try:
    while True:
        # Activate the control circuit (e.g., turn on a relay)
        GPIO.output(control_pin, GPIO.HIGH)
        print("5V control circuit activated")

except KeyboardInterrupt:
    print("Exiting program...")

finally:
    # Clean up the GPIO settings
    GPIO.cleanup()
