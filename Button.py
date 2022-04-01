from gpiozero import LED, Button
import ButtonThread

buttonMail = Button(17)
buttonParcel= Button(22)
reedDoor= Button(27)
led = LED(18)


while True:
    if buttonMail.when_activated==True:
        ButtonThread.buttonThread(buttonMail)
        if buttonMail.when_activated==True:
            buttonMailactive=True
        else:
            buttonMailactive=False
    if buttonMail.when_deactivated==True:
        ButtonThread.buttonThread(buttonMail)
        if buttonMail.when_deactivated==True:
            buttonMailactive=False
        else:
            buttonMailactive=True

    if buttonMailactive==True:
        led.on
    