import RPi.GPIO as GPIO
from time import sleep
# import API_Mail
from datetime import datetime
import requests
import json

url_Mail = "https://briefkasten.azurewebsites.net/briefkasten/brief/post"
url_Parcel = "https://briefkasten.azurewebsites.net/briefkasten/paket/post"
headers = {"Content-Type" : "application/json"}


# I/O Pins
btnMail = 17
btnDoorMail = 27
btnParcel = 22
btnDoorParcel = 12

# gerenal Variables

bncTime = 50 # time in ms
slpTime = 0.9 # time in ms

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(btnMail, GPIO.IN)
GPIO.setup(btnDoorMail, GPIO.IN)
GPIO.setup(btnParcel, GPIO.IN)
GPIO.setup(btnDoorParcel, GPIO.IN)

# Callback Function
def callbackFuncMail(channel):
    try:
        if channel == btnMail:
            value = "Brieffach"
        elif channel == btnDoorMail:
            value = "Briefkastentuer"
        else:
            raise Exception

        if GPIO.input(channel):
            message_change = "empfangen " + value
            status = True
        else:
            message_change = "entnommen " + value
            status = False
        
        time = (datetime.now().strftime("%d-%m-%Y--%H:%M:%S"))
        data = {"message_change" : message_change,
                "brieffach" : GPIO.input(btnMail),
                "briefkastentuere" : GPIO.input(btnDoorMail),
                "zeitstempel" : time,
                }
     
        response = requests.post(url_Mail, data = json.dumps(data), headers = headers)
    
        #print(response.status_code)
        print(response.content)

    except:
        errorHandler(response.status_code)

def callbackFuncParcel(channel):
    try:
        if channel == btnParcel:
            value = "Paketfach"
        elif channel == btnDoorParcel:
            value = "Pakettuer"
        else:
            raise Exception

        if GPIO.input(channel):
            message_change = "empfangen " + value
            status = True
        else:
            message_change = "entnommen " + value
            status = False
        
        time = (datetime.now().strftime("%d-%m-%Y--%H:%M:%S"))
        data = {"message_change" : message_change,
                "packetfach" : GPIO.input(btnParcel),
                "pakettuer" : GPIO.input(btnDoorParcel),
                "zeitstempel" : time,
                }
     
        response = requests.post(url_Parcel, data = json.dumps(data), headers = headers)
    
        #print(response.status_code)
        print(response.content)

    except:
         print("HELLO" + str(data))
         errorHandler(response.status_code)
         
         
def errorHandler(Errorcode):
    try:
        with open("errors.txt", "a") as f:
            f.write(Errorcode)
    except:
        print("No file created")
        
# Definition of action set by change of PIN status

GPIO.add_event_detect(btnMail, GPIO.BOTH, callback = callbackFuncMail, bouncetime=bncTime)
GPIO.add_event_detect(btnDoorMail, GPIO.BOTH, callback = callbackFuncMail, bouncetime=bncTime)
GPIO.add_event_detect(btnParcel, GPIO.BOTH, callback = callbackFuncParcel, bouncetime=bncTime)
GPIO.add_event_detect(btnDoorParcel, GPIO.BOTH, callback = callbackFuncParcel, bouncetime=bncTime)

# Main programm
while True:
    try:
        sleep(slpTime)
    except:
        GPIO.cleanup()
