import RPi.GPIO as GPIO
from time import sleep
import API_Mail

# I/O Pins
btnMail = 16
btnDoor = 20
btnParcel = 21
outpLED =  6

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
            print("Empfangen " + value)
            status = True
        else:
            print("entmneommen " + value)
            status = False
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
