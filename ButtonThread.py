import threading

def timeThread():
    import time
    time.sleep(20)

def buttonThread(Button):
    if Button==True:
        threading.Timer(10,timeThread).start()
        if Button==True:
            buttonCheck=True
        else:
            buttonCheck=False
    return(buttonCheck)