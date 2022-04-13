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
    
    def button(Status):
        if not Status:
            status=True
            return status
        else:
            if Status:
                status=False
                return status
    
    while True:
        if btnMail.is_active:
            if not statusMail:
                statusMail=True
                print("Mail empfangen")
        elif not btnMail.is_active:
            if statusMail:
                statusMail=False
                print("Mail entnommen")
        
        if btnDoorMail.is_active:
            if not statusDoorMail:
                statusDoorMail=True
                print("Mail empfangen")
        elif not btnDoorMail.is_active:
            if statusDoorMail:
                statusDoorMail=False
                print("Mail entnommen")
        
        if btnParecl.is_active:
            if not statusParcel:
                statusParcel=True
                print("Paket empfangen")
        elif not btnParecl.is_active:
            if statusParcel:
                statusParcel=False
                print("Paket entnommen")
        
        if statusMail  or statusDoorMail:
            statLed.on()
        if not (statusMail or statusDoorMail):
            statLed.off()
        
        if statusParcel:
            statLed.blink()
        if not statusParcel:
            statLed.off()