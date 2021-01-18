import RPi.GPIO as GPIO
import time

seg_pin = [18, 23, 24, 25]
hs_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(seg_pin, GPIO.OUT)
GPIO.setup(hs_pin, GPIO.IN)

seg_number = 8
i = 0

# 7セグ表示プログラム(ドライバ用)
def write_7seg(seg_pin,seg_number):
    i = 0
    while i < 4:
        GPIO.output(seg_pin[i], seg_number & (0x01 << i))
        i = i + 1

# カウントアップ挙動の実験
# while i <= 9:
#     write_7seg(seg_pin, i)
#     time.sleep(1)
#     i = i + 1

# メイン処理(人感センサー制御)
try:
    check = 0
    num = 1
    prev_sensor = 0
    while True:
        current_sensor = GPIO.input(hs_pin)
        if (prev_sensor == 0) and (current_sensor == 1):
            check = check + 1
            print(str(check)+"人発見しました")
            write_7seg(seg_pin, num)
            time.sleep(0.1)
            num = num + 1
        else:
            print(GPIO.input(hs_pin))
            time.sleep(0.1)
        prev_sensor = current_sensor

except KeyboardInterrupt:
    pass
finally:
    GPIO.output(seg_pin, GPIO.LOW)
    GPIO.cleanup()
    print("GPIOクリナップクリンミセス")

# GPIO.cleanup
