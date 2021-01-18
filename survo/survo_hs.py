import RPi.GPIO as GPIO
import time

hs_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(hs_pin, GPIO.IN)
GPIO.setup(27,GPIO.OUT)
servo = GPIO.PWM(27,50)

print("START\n")

def servo_v():
    servo.start(7.25)
    time.sleep(1)

    servo.ChangeDutyCycle(2.5)
    time.sleep(1)

    servo.ChangeDutyCycle(7.25)
    time.sleep(1)

    servo.ChangeDutyCycle(12)
    time.sleep(1)

    servo.ChangeDutyCycle(7.25)
    time.sleep(1)

    servo.stop()


# メイン処理(人感センサー制御)
try:
    check = 0
    prev_sensor = 0
    while True:
        current_sensor = GPIO.input(hs_pin)
        if (prev_sensor == 0) and (current_sensor == 1):
            check = check + 1
            print(str(check)+"人発見しました")
            servo_v()
            time.sleep(0.1)
        else:
            print(GPIO.input(hs_pin))
            time.sleep(1)
        prev_sensor = current_sensor

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    print("GPIOクリナップクリンミセス")

# GPIO.cleanup
