from tkgpio import TkCircuit
import API_Mailbox as API

configuration = {
    "width": 600,
    "hight": 600,
    "leds": [
        {"x":50, "y":50,"name": "Mailbox status", "pin":21}
        ],
    "buttons": [
        {"x":50, "y":150,"name": "Mail in/out", "pin":11},
        {"x":150, "y":150,"name": "Parcel in/out", "pin":12},
        {"x":250, "y":150,"name": "Door Mail open/close", "pin":13},
        ],
    }

circuit = TkCircuit(configuration)
@circuit.run
def main():
    from gpiozero import LED, Button
    from time import sleep
    
    btnMail= Button(11)
    btnDoorMail=Button(13)
    btnParecl= Button(12)
    statLed=LED(21)
    
    statusMail=False
    statusDoorMail=False
    statusParcel=False

    while True:
        if btnMail.is_active:
            if not statusMail:
                statusMail=True
                API.send_status_Mail(statusMail,statusDoorMail)
                print("Mail empfangen")
        elif not btnMail.is_active:
            if statusMail:
                statusMail=False
                API.send_status_Mail(statusMail,statusDoorMail)
                print("Mail entnommen")
        
        if btnDoorMail.is_active:
            if not statusDoorMail:
                statusDoorMail=True
                API.send_status_Mail(statusMail,statusDoorMail)
                print("Mail empfangen")
        elif not btnDoorMail.is_active:
            if statusDoorMail:
                statusDoorMail=False
                API.send_status_Mail(statusMail,statusDoorMail)
                print("Mail entnommen")
        
        if btnParecl.is_active:
            if not statusParcel:
                statusParcel=True
                API.send_status_Parcel(statusParcel)
                print("Paket empfangen")
        elif not btnParecl.is_active:
            if statusParcel:
                statusParcel=False
                API.send_status_Parcel(statusParcel)
                print("Paket entnommen")
        
        if statusMail  or statusDoorMail:
            statLed.on()
        if not (statusMail or statusDoorMail):
            statLed.off()
        
        if statusParcel:
            statLed.blink()
        if not statusParcel:
            statLed.off()