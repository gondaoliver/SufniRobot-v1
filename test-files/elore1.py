import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the motor control
motor_pin_1 = 24  # IN1
motor_pin_2 = 23  # IN2
en = 16

# Set up the GPIO pins as outputs
GPIO.setup(motor_pin_1, GPIO.OUT)
GPIO.setup(motor_pin_2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)

# Function to run motor forward
def motor_forward():
    GPIO.output(en, GPIO.HIGH)
    GPIO.output(motor_pin_1, GPIO.HIGH)  # Turn motor on forward
    GPIO.output(motor_pin_2, GPIO.LOW)   # Motor rotates in the forward direction

# Function to stop motor
def motor_stop():
    GPIO.output(en, GPIO.LOW)
    GPIO.output(motor_pin_1, GPIO.LOW)   # Stop motor
    GPIO.output(motor_pin_2, GPIO.LOW)   # Stop motor

try:
    # Run motor forward for 5 seconds
    print("Motor is running forward.")
    motor_forward()
    time.sleep(5)  # Run for 5 seconds

    # Stop motor
    print("Motor stopped.")
    motor_stop()

finally:
    # Clean up GPIO settings to ensure a clean exit
    GPIO.cleanup()

