from machine import Pin
import time

IN1 = Pin((5), Pin.OUT)
IN2 = Pin((18), Pin.OUT)
IN3 = Pin((19), Pin.OUT)
IN4 = Pin((22), Pin.OUT)


mainlist = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]]

while True:
    for i in mainlist:
        IN1.value(i[0])
        IN2.value(i[1])
        IN3.value(i[2])
        IN4.value(i[3])
        time.sleep(0.005)
