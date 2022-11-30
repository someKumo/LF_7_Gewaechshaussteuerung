import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
i = 1
while i<11 :

	# read data using pin 14
	instance = dht11.DHT11(pin = 4)
	result = instance.read()

	while not result.is_valid():
		result = instance.read()


	print ("Temperature: %-3.1f C" % result.temperature)
	print ("Humidity: %-3.1f %%" % result.humidity)
	time.sleep(2)
	i = i + 1
