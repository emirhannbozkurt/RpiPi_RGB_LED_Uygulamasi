#rgb.py
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) #Kirmizi
GPIO.setup(5, GPIO.OUT) #Mavi
GPIO.setup(6, GPIO.OUT) #Yesil



while True:
    
    #Kirmizi
    GPIO.output(4, False)
    GPIO.output(5, True)
    GPIO.output(6, True)
    time.sleep(1)
    #Yesil
    GPIO.output(4, True)
    GPIO.output(5, True)
    GPIO.output(6, False)
    time.sleep(1)
    #Mavi
    GPIO.output(4, True)
    GPIO.output(5, False)
    GPIO.output(6, True)
    time.sleep(1)
    #Beyaz
    GPIO.output(4, False)
    GPIO.output(5, False)
    GPIO.output(6, False)
    time.sleep(1)
    #Sonuk
    GPIO.output(4, True)
    GPIO.output(5, True)
    GPIO.output(6, True)
    time.sleep(1)
    
    

    
