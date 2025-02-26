import RPi.GPIO as GPIO
import time

# Define GPIO pins
IN1 = 23
IN2 = 24
ENA = 16  # PWM pin
speed = 80

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

def move_forward(speed=100):
    """Move forward at given speed."""
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

# Example usage
try:
    move_forward(80)  # Move forward at 80% speed
    time.sleep(2)  # Run for 2 seconds
 

except KeyboardInterrupt:
    print("Stopping")
    stop_motor()
    GPIO.cleanup()
