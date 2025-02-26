from time import sleep
import RPi.GPIO as GPIO
from dualsense_controller import DualSenseController

IN1 = 23
IN2 = 24
ENA = 16
SERVO_Steering = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(SERVO_Steering, GPIO.OUT)

GPIO.output(ENA, GPIO.HIGH)

p = GPIO.PWM(SERVO_Steering, 50)  # 50Hz frequency
p.start(0)  # Alap position 

device_infos = DualSenseController.enumerate_devices()
if len(device_infos) < 1:
    raise Exception('No DualSense Controller available.')

is_running = True
controller = DualSenseController()

# Gombok eseményeinek definiálása
def stop():
    global is_running
    is_running = False
    GPIO.cleanup()


def on_R2_btn_pressed():
    print('R2 button pressed')
    controller.left_rumble.set(255)
    controller.right_rumble.set(255)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def on_R2_btn_released():
    print('R2 button released')
    controller.left_rumble.set(0)
    controller.right_rumble.set(0)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

def on_L2_btn_pressed():
    print('L2 button pressed')
    controller.left_rumble.set(255)
    controller.right_rumble.set(255)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

def on_L2_btn_released():
    print('L2 button released')
    controller.left_rumble.set(0)
    controller.right_rumble.set(0)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

def on_left_stick_moved(joystick):
    x = joystick.x  # Extract the x-axis value
    duty_cycle = 0 + (x * 2.5)  # Convert -1 to 1 range into 5 to 10 duty cycle
    duty_cycle = max(5, min(10, duty_cycle))  # Clamp within servo range
    p.ChangeDutyCycle(duty_cycle)
    print(f'Servo position: {duty_cycle}%')

"""def on_left_stick_released(joystick):
    p.ChangeDutyCycle(0)  # Alap position
    print('Servo position: 0%')
"""

def on_ps_btn_pressed():
    print('PS button pressed -> stop')
    stop()

def on_error(error):
    print(f'Error: {error}')
    stop()


# Gombok és azok eseményeinek regisztrálása
controller.btn_ps.on_down(on_ps_btn_pressed)
controller.btn_r2.on_down(on_R2_btn_pressed)
controller.btn_r2.on_up(on_R2_btn_released)
controller.btn_l2.on_down(on_L2_btn_pressed)
controller.btn_l2.on_up(on_L2_btn_released)
controller.left_stick.on_change(on_left_stick_moved)
# controller.left_stick.on_release(on_left_stick_released)

controller.on_error(on_error)

controller.activate()

while is_running:
    sleep(0.001)
    
controller.deactivate()