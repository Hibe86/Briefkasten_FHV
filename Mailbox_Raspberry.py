import RPi.GPIO as GPIO
from time import sleep
import API_Mail

# I/O Pins
# Input pins
btnMail = 17
btnDoorMail = 27
btnParcel = 22
btnDoorParcel = 12
# output pins
ledProgRun = 25
ledSend = 23
ledSendError = 24
ledGeneralError = 8

# ---------------------
# Variables
# set URL for API

url_Mail = "https://briefkasten.azurewebsites.net/briefkasten/brief/post"
url_Parcel = "https://briefkasten.azurewebsites.net/briefkasten/paket/post"
url_Mail_Door = "https://briefkasten.azurewebsites.net/briefkasten/brieftuere/post"
url_Parcel_Door = "https://briefkasten.azurewebsites.net/briefkasten/pakettuere/post"

# Global Variables
# timer variablkes
bncTime = 500 # time in ms
slpTime = 0.9 # time in seconds
flashTime = 0.5 # time in seconds

# Effected part
prtMail = "brieffach"
prtMailDoor = "briefkastentuere"
prtParcel = "packetfach"
prtParcelDoor = "packetfachtuere"

# Standard messages
msgMailArrived = "Recived"
msgMailPicked = "Picked up"
msgDoorOpen = "Door open"
msgDoorClosed = "Door closed"

# ---------------------
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(btnMail, GPIO.IN)
GPIO.setup(btnDoorMail, GPIO.IN)
GPIO.setup(btnParcel, GPIO.IN)
GPIO.setup(btnDoorParcel, GPIO.IN)
GPIO.setup(ledProgRun, GPIO.OUT)
GPIO.setup(ledSend, GPIO.OUT)
GPIO.setup(ledSendError, GPIO.OUT)
GPIO.setup(ledGeneralError, GPIO.OUT)

# Subroutines
# send LED toggle
def flashLed(Channel):
    """Used to flash an LED that is connected to an output
Used output set by Main program
Input Variable: Channel (I/O pin)
"""
    try:
        GPIO.output(Channel, GPIO.HIGH)
        sleep(flashTime)
        GPIO.output(Channel, GPIO.LOW)
    except:
        raise Exception("Connection to Output not possible")
    
# Callback Function
def callbackFuncMail(channel):
    """Callback function for Mail delivery:
Sets the message that is delivered from the API to the Webservice
Input Variable:
Channel (I/O setting via Main program)

used Variables:
message (arrived/picked) set by global declaration)
prtMail: effected Mailbox part
GPIO pin
URL of Webservice
"""
    try:
        if GPIO.input(channel):
            message = msgMailArrived
        else:
            message = msgMailPicked
        API_Mail.send_status(message,prtMail,GPIO.input(btnMail),url_Mail)
        flashLed(ledSend)
    except:
        flashLed(ledSendError)

def callbackFuncMailDoor(channel):
    """Callback function for Mailbox door:
Sets the message that is delivered from the API to the Webservice
Input Variable:
Channel (I/O setting via Main program)

used Variables:
message (open/closed) set by global declaration)
prtMailDoor: effected Mailbox part
GPIO pin
URL of Webservice
"""
    try:
        if GPIO.input(channel):
            message = msgDoorOpen
        else:
            message = msgDoorClosed
        API_Mail.send_status(message,prtMailDoor,GPIO.input(btnDoorMail),url_Mail_Door)
        flashLed(ledSend)
    except:
        flashLed(ledSendError)

def callbackFuncParcel(channel):
    """Callback function for Parcel delivery system:
Sets the message that is delivered from the API to the Webservice
Input Variable:
Channel (I/O setting via Main program)

used Variables:
message (arrived/picked) set by global declaration)
prtParcel: effected Mailbox part
GPIO pin
URL of Webservice
"""
    try:
        if GPIO.input(channel):
            message = msgMailArrived
        else:
            message = msgMailPicked
        API_Mail.send_status(message,prtParcel,GPIO.input(btnParcel),url_Parcel)
        flashLed(ledSend)
    except:
        flashLed(ledSendError)
         
def callbackFuncParcelDoor(channel):
    """Callback function for Parcel delivery door:
Sets the message that is delivered from the API to the Webservice
Input Variable:
Channel (I/O setting via Main program)

used Variables:
message (open/closed) set by global declaration)
prtParcelDoor: effected Mailbox part
GPIO pin
URL of Webservice
"""
    try:
        if GPIO.input(channel):
            message = msgDoorOpen
        else:
            message = msgDoorClosed
        API_Mail.send_status(message,prtParcelDoor,GPIO.input(btnDoorParcel),url_Parcel_Door)
        flashLed(ledSend)
    except:
        flashLed(ledSendError)
        
# Definition of action set by change of PIN status

GPIO.add_event_detect(btnMail, GPIO.BOTH, callback = callbackFuncMail, bouncetime=bncTime)
GPIO.add_event_detect(btnDoorMail, GPIO.BOTH, callback = callbackFuncMailDoor, bouncetime=bncTime)
GPIO.add_event_detect(btnParcel, GPIO.BOTH, callback = callbackFuncParcel, bouncetime=bncTime)
GPIO.add_event_detect(btnDoorParcel, GPIO.BOTH, callback = callbackFuncParcelDoor, bouncetime=bncTime)

# ----------------------------------
# Main programm
# ----------------------------------
# set LED to status
GPIO.output(ledGeneralError, GPIO.LOW)
GPIO.output(ledProgRun, GPIO.HIGH)
# Initial status send to API
try:
    if GPIO.input(btnMail):
        message=msgMailArrived
    else:
        message=msgMailPicked
    API_Mail.send_status(message,prtMail,GPIO.input(btnMail),url_Mail)
    if GPIO.input(btnDoorMail):
        message=msgDoorClosed
    else:
        message=msgDoorOpen
    API_Mail.send_status(message,prtMailDoor,GPIO.input(btnDoorMail),url_Mail_Door)
    if GPIO.input(btnParcel):
        message=msgMailArrived
    else:
        message=msgMailPicked
    API_Mail.send_status(message,prtParcel,GPIO.input(btnParcel),url_Parcel)
    if GPIO.input(btnDoorParcel):
        message=msgDoorClosed
    else:
        message=msgDoorOpen
    API_Mail.send_status(message,prtParcelDoor,GPIO.input(btnDoorParcel),url_Parcel_Door)
    flashLed(ledSend)
except:
    GPIO.output(ledProgRun, GPIO.LOW)
    GPIO.output(ledGeneralError, GPIO.HIGH)
    GPIO.cleanup()

while True:
    try:
        sleep(slpTime)
    except:
        GPIO.output(ledProgRun, GPIO.LOW)
        GPIO.output(ledGeneralError, GPIO.HIGH)
        sleep(slpTime)
        GPIO.cleanup()
