import RPi.GPIO as GPIO
from time import sleep
import API_Mail

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
        if GPIO.input(channel):
            message_change = "Empfangen"# + value
            status = True
        else:
            message_change = "Entnommen"# + value
            status = False
        API_Mail.send_status_mail(message_change,GPIO.input(btnMail),GPIO.input(btnDoorMail))
    except:
        print("HELLO")

def callbackFuncMailDoor(channel):
    try:
        if GPIO.input(channel):
            message_change = "Empfangen"# + value
            status = True
        else:
            message_change = "Entnommen"# + value
            status = False
        API_Mail.send_status_mail_Door(message_change,GPIO.input(btnDoorMail))
    except:
        print("HELLO")


def callbackFuncParcel(channel):
    try:
        if GPIO.input(channel):
            message_change = "Empfangen" #+ value
            status = True
        else:
            message_change = "Entnommen" #+ value
            status = False
        API_Mail.send_status_parcel(message_change,GPIO.input(btnParcel),GPIO.input(btnDoorParcel))
    except:
         print("HELLO")
         
def callbackFuncParcelDoor(channel):
    try:
        if GPIO.input(channel):
            message_change = "Empfangen" #+ value
            status = True
        else:
            message_change = "Entnommen" #+ value
            status = False
        API_Mail.send_status_parcel_Door(message_change,GPIO.input(btnDoorParcel))
    except:
         print("HELLO")
        
# Definition of action set by change of PIN status

GPIO.add_event_detect(btnMail, GPIO.BOTH, callback = callbackFuncMail, bouncetime=bncTime)
GPIO.add_event_detect(btnDoorMail, GPIO.BOTH, callback = callbackFuncMailDoor, bouncetime=bncTime)
GPIO.add_event_detect(btnParcel, GPIO.BOTH, callback = callbackFuncParcel, bouncetime=bncTime)
GPIO.add_event_detect(btnDoorParcel, GPIO.BOTH, callback = callbackFuncParcelDoor, bouncetime=bncTime)

# Main programm
while True:
    try:
        sleep(slpTime)
    except:
        GPIO.cleanup()

