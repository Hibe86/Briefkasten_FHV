import RPi.GPIO as GPIO
from time import sleep
import API_Mail
import requests
import json
from datetime import datetime


url = "   "
header = {"Content-Type" : "application/json"}


# I/O Pins
btnMail = 17
btnDoor = 27
btnParcel = 22
outpLED =  5

# gerenal Variables

bncTime = 5000 # time in ms

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(btnMail, GPIO.IN)
GPIO.setup(btnDoor, GPIO.IN)
GPIO.setup(btnParcel, GPIO.IN)
GPIO.setup(outpLED, GPIO.OUT)

# Callback Function
def callbackFunc(channel):
    try:
        if channel == btnMail:
            value = "Brieffach"
        elif channel == btnDoor:
            value = "Briefkastentür"
        elif channel == btnParcel:
            value = "Paketfach"
        else:
            raise Exception

        if GPIO.input(channel):
            message_change = "Empfangen " + value
            status = True
        else:
            message_change = "entnommen " + value
            status = False
            
        data = {"message_change" : message_change,
                "brieffach" : GPIO.input(btnMail),
                "briefkastentuere" : GPIO.input(btnDoor),
                "packetfach" : GPIO.input(btnParcel),
                "zeitstempel" : datetime.now()
                }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        
    except:
        API_Mail.send_error(Exception.Errorcode)
        raise ValueError ("Callback not complete")
        
    # send data
    try:
        API_mail.send_status(value, status)
    except:
        API_Mail.send_error(Exception.Errorcode)
    
# Definition of Pins
GPIO.add_event_detect(btnMail, GPIO.BOTH, callback = callbackFunc, bouncetime=bncTime)
GPIO.add_event_detect(btnDoor, GPIO.BOTH, callback = callbackFunc, bouncetime=bncTime)
GPIO.add_event_detect(btnParcel, GPIO.BOTH, callback = callbackFunc, bouncetime=bncTime)

# Main programm
while True:
    try:
        sleep(0.1)
    except:
        GPIO.cleanup()