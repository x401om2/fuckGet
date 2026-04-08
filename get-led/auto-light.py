import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
light_sensor = 6
GPIO.setup(light_sensor, GPIO.IN)
while True:
    GPIO.output(led, not GPIO.input(light_sensor))