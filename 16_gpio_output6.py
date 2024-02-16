import RPi.GPIO as GPIO
import time

led_pin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        for t_high in range(0, 11):
            GPIO.output(led_pin, True)
            time.sleep(t_high*0.001)
            GPIO.output(led_pin, False)
            time.sleep((10-t_high)*0.001)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
