import RPi.GPIO as GPIO
import time

led_pin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

GPIO.output(led_pin, True)
time.sleep(2.0)
GPIO.output(led_pin, False)

GPIO.cleanup()
