from time import sleep
import RPi.GPIO as GPIO
from dualsense_controller import DualSenseController

IN1 = 23
IN2 = 24
ENA = 16 

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

GPIO.output(ENA, GPIO.HIGH)


# list availabe devices and throw exception when tzhere is no device detected
device_infos = DualSenseController.enumerate_devices()
if len(device_infos) < 1:
    raise Exception('No DualSense Controller available.')

# flag, which keeps program alive
is_running = True

# create an instance, use fiŕst available device
controller = DualSenseController()


# switches the keep alive flag, which stops the below loop
def stop():
    global is_running
    is_running = False


# callback, when cross button is pressed, which enables rumble
def on_R2_btn_pressed():
    print('R2 button pressed')
    controller.left_rumble.set(255)
    controller.right_rumble.set(255)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)


# callback, when cross button is released, which disables rumble
def on_R2_btn_released():
    print('R2 button released')
    controller.left_rumble.set(0)
    controller.right_rumble.set(0)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

    # callback, when cross button is pressed, which enables rumble
def on_L2_btn_pressed():
    print('L2 button pressed')
    controller.left_rumble.set(255)
    controller.right_rumble.set(255)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)


# callback, when cross button is released, which disables rumble
def on_L2_btn_released():
    print('L2 button released')
    controller.left_rumble.set(0)
    controller.right_rumble.set(0)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)


# callback, when PlayStation button is pressed
# stop program
def on_ps_btn_pressed():
    print('PS button released -> stop')
    GPIO.cleanup()
    stop()


# callback, when unintended error occurs,
# i.e. physically disconnecting the controller during operation
# stop program
def on_error(error):
    print(f'Opps! an error occured: {error}')
    stop()


# register the button callbacks
controller.btn_ps.on_down(on_ps_btn_pressed)
controller.btn_r2.on_down(on_R2_btn_pressed)
controller.btn_r2.on_up(on_R2_btn_released)
controller.btn_l2.on_down(on_L2_btn_pressed)
controller.btn_l2.on_up(on_L2_btn_released)

# register the error callback
controller.on_error(on_error)

# enable/connect the device
controller.activate()

# start keep alive loop, controller inputs and callbacks are handled in a second thread
while is_running:
    sleep(0.001)

# disable/disconnect controller device
controller.deactivate()
