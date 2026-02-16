from machine import Pin
import time

IN1 = Pin((5), Pin.OUT)
IN2 = Pin((18), Pin.OUT)
IN3 = Pin((19), Pin.OUT)
IN4 = Pin((22), Pin.OUT)


clockwise = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
anticlockwise = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]

while True:
    for x in range(500):
        #must occur 500 times
        for cw in clockwise:
            IN1.value(cw[0])
            IN2.value(cw[1])
            IN3.value(cw[2])
            IN4.value(cw[3])
            time.sleep_ms(5)
            
    for y in range(500):
        for acw in anticlockwise:
            IN1.value(acw[0])
            IN2.value(acw[1])
            IN3.value(acw[2])
            IN4.value(acw[3])
            time.sleep_ms(5)

