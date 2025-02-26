import RPi.GPIO as GPIO
import time

# Define GPIO pins
IN1 = 23
IN2 = 24
ENA = 16  # Enable pin

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

# Enable the motor driver
GPIO.output(ENA, GPIO.HIGH)

def move_forward():
    """Move forward at full speed."""
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def move_backward():
    """Move backward at full speed."""
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

def stop_motor():
    """Stop the motor."""
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

# Example usage
try:
    move_forward()
    time.sleep(2)  # Move forward for 2 seconds
    move_backward()
    time.sleep(2)  # Move backward for 2 seconds
    stop_motor()

except KeyboardInterrupt:
    stop_motor()
    GPIO.cleanup()
