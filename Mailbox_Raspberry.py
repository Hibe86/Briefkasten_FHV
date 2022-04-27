import RPi.GPIO as GPIO
from time import sleep
import API_Mail

# I/O Pins
btnMail = 17
btnDoorMail = 27
btnParcel = 22
btnDoorParcel = 12

ledProgRun = 5
ledSend = 6
ledSendError = 13
ledGeneralError = 26

# set URL for API

url_Mail = "https://briefkasten.azurewebsites.net/briefkasten/brief/post"
url_Parcel = "https://briefkasten.azurewebsites.net/briefkasten/paket/post"
url_Mail_Door = "https://briefkasten.azurewebsites.net/briefkasten/brieftuere/post"
url_Parcel_Door = "https://briefkasten.azurewebsites.net/briefkasten/pakettuere/post"

# gerenal Variables

bncTime = 50 # time in ms
slpTime = 0.9 # time in seconds
flashTime = 0.5 # time in seconds

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO.setup(btnMail, GPIO.IN)
GPIO.setup(btnDoorMail, GPIO.IN)
GPIO.setup(btnParcel, GPIO.IN)
GPIO.setup(btnDoorParcel, GPIO.IN)
GPIO.setup(ledProgRun, GPIO.OUT)
GPIO.setup(ledSend, GPIO.OUT)
GPIO.setup(ledSendError, GPIO.OUT)
GPIO.setup(ledGeneralError, GPIO.OUT)

# send LED toggle
def flashLed(Channel):
    GPIO.output(Channel, GPIO.HIGH)
    sleep(flashTime)
    GPIO.output(Channel, GPIO.LOW)

# Callback Function
def callbackFuncMail(channel):
    try:
        if GPIO.input(channel):
            message = "Empfangen"# + value
        else:
            message = "Entnommen"# + value
        # API_Mail.send_status_mail(message_change,GPIO.input(btnMail),GPIO.input(btnDoorMail))
        API_Mail.send_status(message,"brieffach",GPIO.input(btnMail),url_Mail)
        flashLed(ledSend)
    except:
        flashLed(ledSendError)

def callbackFuncMailDoor(channel):
    try:
        if GPIO.input(channel):
            message_change = "Offen"# + value
        else:
            message_change = "Geschlossen"# + value
        # API_Mail.send_status_mail_Door(message_change,GPIO.input(btnDoorMail))
        API_Mail.send_status(message,"briefkastentuere",GPIO.input(btnDoorMail),url_Mail_Door)
        flashLed(ledSend)
    except:
        flashLed(ledSendError)

def callbackFuncParcel(channel):
    try:
        if GPIO.input(channel):
            message_change = "Empfangen" #+ value
        else:
            message_change = "Entnommen" #+ value
        #API_Mail.send_status_parcel(message_change,GPIO.input(btnParcel),GPIO.input(btnDoorParcel))
        API_Mail.send_status(message,"packetfach",GPIO.input(btnParcel),url_Parcel)
        flashLed(ledSend)
    except:
        flashLed(ledSendError)
         
def callbackFuncParcelDoor(channel):
    try:
        if GPIO.input(channel):
            message_change = "Empfangen" #+ value
        else:
            message_change = "Entnommen" #+ value
        # API_Mail.send_status_parcel_Door(message_change,GPIO.input(btnDoorParcel))
        API_Mail.send_status(message,"packetfach",GPIO.input(btnDoorParcel),url_Parcel_Door)
        flashLed(ledSend)
    except:
        flashLed(ledSendError)

# Test program for API
# def testFunc(ChannelStatus,MailBoxPart):
#     try:
#         print("Testfunktion gestartet")
#         if ChannelStatus:
#             message="Offen"
#         else:
#             message="Geschlossen"
#         print("Testfunktion vorbereiten senden")
#         API_Mail.send_status(message,MailBoxPart,ChannelStatus,url_Mail_Door)
#         print("Testfunktion gesendet")
#     except:
#         print("Testfunktion fehlerhaft")
        
# Definition of action set by change of PIN status

GPIO.add_event_detect(btnMail, GPIO.BOTH, callback = callbackFuncMail, bouncetime=bncTime)
GPIO.add_event_detect(btnDoorMail, GPIO.BOTH, callback = callbackFuncMailDoor, bouncetime=bncTime)
GPIO.add_event_detect(btnParcel, GPIO.BOTH, callback = callbackFuncParcel, bouncetime=bncTime)
GPIO.add_event_detect(btnDoorParcel, GPIO.BOTH, callback = callbackFuncParcelDoor, bouncetime=bncTime)


# Main programm
while True:
    GPIO.output(ledGeneralError, GPIO.LOW)
    try:
#         testFunc(1,"briefkastentuere")
#         sleep(slpTime)
#         testFunc(0,"briefkastentuere")
        GPIO.output(ledProgRun, GPIO.HIGH)
        sleep(slpTime)
    except:
        GPIO.output(ledProgRun, GPIO.LOW)
        GPIO.output(ledGeneralError, GPIO.HIGH)
        sleep(slpTime)
        GPIO.cleanup()
