from tkgpio import TkCircuit

configuration = {
    "width": 600,
    "hight": 600,
    "leds": [
        {"x":50, "y":50,"name": "Mailbox status", "pin":21}
        ],
    "buttons": [
        {"x":50, "y":150,"name": "Mail in/out", "pin":11},
        {"x":150, "y":150,"name": "Parcel in/out", "pin":12},
        {"x":250, "y":150,"name": "Door open/close", "pin":13}
        ],
    }

circuit = TkCircuit(configuration)
@circuit.run

#Global variables
statusMail=False        
statusParcel=False
statusDoorOpen=False

def mail(Channel):
    global statusMail
    if inputChannel

def main():
    from gpiozero import LED, Button
    from time import sleep
    
        
    ledStaus = LED(21)
    buttonMail=Button(11, hold_time=5)
    buttonParcel=Button(12, hold_time=5)
    reedContDoor=Button(13)
    
    if buttonMail.when_activated:
        if not statusMail:
            statusMail=True
            print("Post")
    else:
        if statusMail:
            statusMail=False
            print("Entfernt")
    
    
 
    while True:
        sleep(0.1)