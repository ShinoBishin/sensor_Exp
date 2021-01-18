import RPi.GPIO as GPIO
import time

hs_pin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(hs_pin, GPIO.IN)

print("START\n")


# メイン処理(人感センサー制御)
try:
    check = 0
    prev_sensor = 0
    while True:
        current_sensor = GPIO.input(hs_pin)
        if (prev_sensor == 0) and (current_sensor == 1):
            check = check + 1
            print(str(check)+"人発見しました")
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
