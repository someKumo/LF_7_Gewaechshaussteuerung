#!/usr/bin/python
# -*- coding: utf-8 -*-
import board
import RPi.GPIO as GPIO
import dht11
import time

from adafruit_ht16k33.segments import Seg7x4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
i2c = board.I2C()
segment = Seg7x4(i2c, address=0x70)
#segment der I2C Adresse 0x70 und die Displaydefinition zuweisen
segment.fill(0)
# Initialisierung des Displays.
# Muss einmal ausgefÃ¼hrt werden bevor das Display benutzt wird.
print ("STRG+C Druecken zum beenden.")
#print Befehl für Ausgabe zum beenden des Scriptes
#Schleife welche dauerhaft die Zeit updated und sie auf dem Display anzeigt.
try:
    while(True):
        #segment.fill(0)
        
        instance = dht11.DHT11(pin = 4)
        result = instance.read()

        while not result.is_valid():
                result = instance.read()
        
        temp = int(round(result.temperature,0))
        humi = int(round(result.humidity,0))
        
        # Doppelpunkt zwischen Nummern
        segment.colon = True
        
        # Temperatur
        segment[0] = str(int(temp / 10)) # Zehnerzahlen
        segment[1] = str(temp % 10) # Einerzahlen
        # Luftfeuchtigkeit
        segment[2] = str(int(humi / 10)) # Zehnerzahlen
        segment[3] = str(humi % 10) # Einerzahlen
            
        segment.show() # Wird benötigt um die Display LEDs zu updaten.
        time.sleep(1) # Warte eine Sekunde
except KeyboardInterrupt:
    segment.fill(0)
