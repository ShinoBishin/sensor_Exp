import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
servo = GPIO.PWM(27, 50)

servo.start(7.25)
time.sleep(3)

for i in range(96):
    print("\ni=", i)

    x = (i/10)+2.5
    print("x = ", x)
    servo.ChangeDutyCycle(x)
    time.sleep(0.3)

    y = 12 - (i/10)
    print("y = ", y)
    servo.ChangeDutyCycle(y)
    time.sleep(0.3)

servo.stop()
GPIO.cleanup()
