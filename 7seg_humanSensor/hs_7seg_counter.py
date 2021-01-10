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
    num = 1
    count = 1
    while True:
        if(GPIO.input(hs_pin) == GPIO.HIGH):
            print(str(count) + "人発見しました")
            count = count + 1
            write_7seg(seg_pin, num)
            time.sleep(20)
            num = num + 1
        else:
            print(GPIO.input(hs_pin))
            time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.output(seg_pin, GPIO.LOW)
    GPIO.cleanup()
    print("GPIOクリナップクリンミセス")

# GPIO.cleanup
