import serial
import time
S = serial.Serial('com5', 9600, timeout=2)
while True:
    data = S.readline().decode().rstrip()
    print(data)
    if data == "alert":
        print("入侵警報！！！")
    elif data == "normal":
        print("警報解除")
time.sleep(1)