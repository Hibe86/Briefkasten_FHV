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
def main():
    import time
    import RPi.GPIO as GPIO           # import RPi.GPIO module  
    from time import sleep
    import time
    
    GPIO.a.add_event_detect(11,GPIO.RISING,print("trigger"))