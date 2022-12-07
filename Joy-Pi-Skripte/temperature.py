import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
z = 1
i = 1
while i<21 :

        # read data using pin 14
        instance = dht11.DHT11(pin = 4)
        result = instance.read()

        while not result.is_valid():
                result = instance.read()
        print ("")
        print ("Versuch: " + str(z))
        temp = round(result.temperature)
        humi = round(result.humidity)
        print ("Temperature: %-3.0fC" % result.temperature)
        print ("Humidity: %-3.0f%%" % result.humidity)
        time.sleep(15)
        i = i + 1
        z = z + 1
