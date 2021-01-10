import RPi.GPIO as GPIO
import time

seg_pin = [18, 23, 24, 25]
hs_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(seg_pin, GPIO.OUT)
GPIO.setup(hs_pin, GPIO.IN)

seg_number = 9
i = 0

def write_7seg():
    global i
    while i < 4:
        GPIO.output(seg_pin[i], count & (0x01 << i))
        i = i + 1

# time.sleep(3)
# GPIO.output(seg_pin, GPIO.LOW)

try:
    print("処理キャンセル：Ctrl+C")
    seg_number = 1
    count = 1
    while True:
        if(GPIO.input(hs_pin) == GPIO.HIGH):
            print(str(count) + "回目の検知")
            count = count + 1
            write_7seg()
            time.sleep(20)
        else:
            print(GPIO.input(hs_pin))
            time.sleep(3)
except KeyboardInterrupt:
    print("終了処理中")
finally:
    GPIO.cleanup()
    print("GPIOクリナップクリンミセス")

GPIO.cleanup
