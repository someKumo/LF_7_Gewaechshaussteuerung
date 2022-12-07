#!/usr/bin/python
# -*- coding: utf-8 -*-

#DHT11

import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
i = 1


#LCD-2x16

import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Definiere LCD Zeilen und Spaltenanzahl.
lcd_columns = 16
lcd_rows    = 2

# Initialisierung I2C Bus
i2c = busio.I2C(board.SCL, board.SDA)

# Festlegen des LCDs in die Variable LCD
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x21)

try:
    lcd.backlight = True
    while i<21:
        instance = dht11.DHT11(pin = 4)
        result = instance.read()

        while not result.is_valid():
                result = instance.read()
        lcd.message = "Temperature: " % str(int(round(result.temperature,0))) % "\n" % "Humidity: " % str(int(round(result.humidity,0)))        
        time.sleep(15)
        i = i + 1

    lcd.clear()
    lcd.backlight = False
    
    
except KeyboardInterrupt:
    # LCD ausschalten.
    lcd.clear()
    lcd.backlight = False
