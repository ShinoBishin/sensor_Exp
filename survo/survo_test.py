import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
servo = GPIO.PWM(27,50)

servo.start(12)
time.sleep(1)

servo.ChangeDutyCycle(2.5)
time.sleep(1)

servo.ChangeDutyCycle(12)
time.sleep(1)

servo.ChangeDutyCycle(2.5)
time.sleep(1)

servo.ChangeDutyCycle(7.25)
time.sleep(1)

servo.stop()
GPIO.cleanup()