from machine import Pin
import time

IN1 = Pin((5), Pin.OUT)
IN2 = Pin((18), Pin.OUT)
IN3 = Pin((19), Pin.OUT)
IN4 = Pin((22), Pin.OUT)

while True:
	#1st second:
	IN1.value(1)
	IN2.value(0)
	IN3.value(0)
	IN4.value(0)
	time.sleep_ms(5)
	#time delay of 5 milliseconds
  
	#2nd second:
	IN1.value(0)
	IN2.value(1)
	IN3.value(0)
	IN4.value(0)
	
	time.sleep_ms(5)
	
	#3rd second:
	IN1.value(0)
	IN2.value(0)
	IN3.value(1)
	IN4.value(0)
	
	time.sleep_ms(5)
	
	#4th second:
	IN1.value(0)
	IN2.value(0)
	IN3.value(0)
	IN4.value(1)
	
	time.sleep_ms(5)
  #Write your code here to run the stepper motor without using any loop
