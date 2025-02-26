import RPi.GPIO as GPIO
import time

in1 = 24
in2 = 23

GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)
