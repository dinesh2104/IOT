#import requests
import time
import RPi.GPIO as GPIO
import random

#url='https://dinesh.selfmade.technology/'

GPIO.setmode(GPIO.BCM)
channal=[12,13,19]

for c in channal:
	GPIO.setup(c,GPIO.OUT)

r=GPIO.PWM(channal[0],1000)
g=GPIO.PWM(channal[1],1000)
b=GPIO.PWM(channal[2],1000)

r.start(100)
g.start(100)
b.start(100)

try:
	while True:
		# response=requests.get(url+'rgbcolor')
		# data=response.json()

		i=random.randint(0,255)
		j=random.randint(0,255)
		z=random.randint(0,255)
		print([i,j,z])
		r.ChangeDutyCycle(100-(i*100/255))
		g.ChangeDutyCycle(100-(j*100/255))
		b.ChangeDutyCycle(100-(z*100/255))				
		time.sleep(1)


except KeyboardInterrupt as e:
	GPIO.cleanup()
	print('\n------------Exiting--------------')

except Exception as e:
	GPIO.cleanup()
	print('\n------------Exiting--------------')
	