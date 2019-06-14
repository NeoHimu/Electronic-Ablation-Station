#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
import Adafruit_DHT

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.IN)

prev_flag = False
while True:
    if GPIO.input(14) is 1 and prev_flag==False:
        print('The pin is high')
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 15)
        with open("current_count.txt", "r+") as f:
            count = int(f.read())
            f.seek(0)
            f.write(str(count+1))
            f.truncate()
            print(count, datetime.datetime.now())
            # record data in the data.txt file
            with open("data.txt", "a") as data_file:
                data_file.write(str(count) +" "+ str(datetime.datetime.now())+" "+str(temperature)+"c "+str(humidity)+"%\n")
            prev_flag = True
    elif GPIO.input(14) is 0:
        prev_flag = False
        print('The pin is low')
        
    time.sleep(0.25)



        