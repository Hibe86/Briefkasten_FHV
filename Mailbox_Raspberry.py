import RPi.GPIO as GPIO
from time import sleep
import API_Mail


# I/O Pins
btnMail = 17
btnDoorMail = 27
btnParcel = 22
btnDoorParcel = 12

ledGreenRaspRun = 16
ledBlueRaspSendOK = 20
ledRedRaspSendNotOK = 21

# gerenal Variables

bncTime = 50 # time in ms
slpTime = 0.9 # time in ms
slpTimeLED = 500
msgDoorOpen = "Offen"
msgDoorClosed = "Geschlossen"
msgRecived = "Empfangen"
msgRemoved = "Entnommen"

# URL setting
url_Mail = "https://briefkasten.azurewebsites.net/briefkasten/brief/post"
url_Parcel = "https://briefkasten.azurewebsites.net/briefkasten/paket/post"
url_Mail_Door = "https://briefkasten.azurewebsites.net/briefkasten/brieftuere/post"
url_Parcel_Door = "https://briefkasten.azurewebsites.net/briefkasten/pakettuere/post"

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(btnMail, GPIO.IN)
GPIO.setup(btnDoorMail, GPIO.IN)
GPIO.setup(btnParcel, GPIO.IN)
GPIO.setup(btnDoorParcel, GPIO.IN)
GPIO.setup(ledGreenRaspRun, GPIO.OUT)
GPIO.setup(ledBlueRaspSendOK, GPIO.OUT)
GPIO.setup(ledRedRaspSendNotOK, GPIO.OUT)

def errorDetected():
    GPIO.output(ledRedRaspSendNotOK, GPIO.HIGH)
    sleep(slpTimeLED)
    GPIO.output(ledRedRaspSendNotOK, GPIO.LOW)
    return

def sendIsOkay():
    GPIO.output(ledBlueRaspSendOK, GPIO.HIGH)
    sleep(slpTimeLED)
    GPIO.output(ledBlueRaspSendOK, GPIO.LOW)
    return

# Callback Function
def callbackFuncMail(channel):
    try:
        if GPIO.input(channel):
            message_change = msgRecived
        else:
            message_change = msgRemoved
        #API_Mail.send_status_mail(message_change,GPIO.input(btnMail))
        API_Mail.send_status("brieffach",message_change,GPIO.input(btnMail),url_Mail)
    except:
        errorDetected()

def callbackFuncMailDoor(channel):
    try:
        if GPIO.input(channel):
            message_change = msgDoorOpen
        else:
            message_change = msgDoorClosed
        #API_Mail.send_status_mail_Door(message_change,GPIO.input(btnDoorMail))
        API_Mail.send_status("brieffachtuer",message_change,GPIO.input(btnDoorMail),url_Mail_Door)
    except:
        errorDetected()


def callbackFuncParcel(channel):
    try:
        if GPIO.input(channel):
            message_change = msgRecived
        else:
            message_change = msgRemoved
        #API_Mail.send_status_parcel(message_change,GPIO.input(btnParcel))
        API_Mail.send_status("packetfach",message_change,GPIO.input(btnParcel),url_Parcel)
    except:
         errorDetected()
         
def callbackFuncParcelDoor(channel):
    try:
        if GPIO.input(channel):
            message_change = msgDoorOpen
        else:
            message_change = msgDoorClosed
        #API_Mail.send_status_parcel_Door(message_change,GPIO.input(btnDoorParcel))
        API_Mail.send_status("packetfachtuere",message_change,GPIO.input(btnDoorParcel),url_Parcel_Door)
    except:
         errorDetected()
        
# Definition of action set by change of PIN status

# GPIO.add_event_detect(btnMail, GPIO.BOTH, callback = callbackFuncMail, bouncetime=bncTime)
GPIO.add_event_detect(btnDoorMail, GPIO.BOTH, callback = callbackFuncMailDoor, bouncetime=bncTime)
GPIO.add_event_detect(btnParcel, GPIO.BOTH, callback = callbackFuncParcel, bouncetime=bncTime)
GPIO.add_event_detect(btnDoorParcel, GPIO.BOTH, callback = callbackFuncParcelDoor, bouncetime=bncTime)

# Main programm
while True:
    try:
        GPIO.output(ledGreenRaspRun,GPIO.HIGH)
        sleep(slpTime)
    except:
        GPIO.output(ledGreenRaspRun,GPIO.LOW)
        GPIO.cleanup()
