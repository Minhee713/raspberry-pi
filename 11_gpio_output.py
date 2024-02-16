import RPi.GPIO as GPIO

led_pin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

GPIO.output(led_pin, True)

try: 
    while True:
        pass

except KeyboardInterrupt:
    pass

GPIO.cleanup()
