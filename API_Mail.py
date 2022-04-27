# general imports
from datetime import datetime
import requests
import json

# global variables/settings
url_Mail = "https://briefkasten.azurewebsites.net/briefkasten/brief/post"
url_Parcel = "https://briefkasten.azurewebsites.net/briefkasten/paket/post"
url_Mail_Door = "https://briefkasten.azurewebsites.net/briefkasten/brieftuere/post"
url_Parcel_Door = "https://briefkasten.azurewebsites.net/briefkasten/pakettuere/post"
headers = {"Content-Type" : "application/json"}

def getActualTime():
    actTime = (datetime.now().strftime("%H:%M:%S")) # format Date Time to correct format
    return actTime

def getActualDate():
    actDate = (datetime.now().strftime("%d-%m-%Y"))
    return actDate

# send status of mailbox to url
def send_status_mail(Message_change,StatusMail):
    try:
        data = {"status" : Message_change,
                "brieffach" : StatusMail,
                "time" : getActualTime(),
                "date" : getActualDate(),
                }
        print("Send status Mail")
    except:
        raise ValueError("Wrong format of data to transmit")
    try:
        print("Send status Mail correct")
        response = requests.post(url_Mail, data = json.dumps(data), headers = headers)
    except:
        raise ValueError("Wrong response")
    
    
# send status of parcel box to url
def send_status_parcel(Message_change,StatusParcel):
    try:
        data = {"status" : Message_change,
                "packetfach" : StatusParcel,
                "time" : getActualTime(),
                "date" : getActualDate(),
                }
        print("Send status parcel")
    except:
        raise ValueError("Wrong format of data to transmit")
    try:
        response = requests.post(url_Parcel, data = json.dumps(data), headers = headers)
        print("Send status Parcel correct")
    except:
        raise ValueError("Wrong response")
    
def send_status_mail_Door(Message_change,StatusMailDoor):
    try:
        data = {"status" : Message_change,
                "briefkastentuere" : StatusMailDoor,
                "time" : getActualTime(),
                "date" : getActualDate(),
                }
        print("Send status Mail")
    except:
        raise ValueError("Wrong format of data to transmit")
    try:
        print("Send status Mail correct")
        response = requests.post(url_Mail_Door, data = json.dumps(data), headers = headers)
    except:
        raise ValueError("Wrong response")
    
def send_status_parcel_Door(Message_change,StatusParcelDoor):
    try:
        data = {"status" : Message_change,
                "pakettuer" : StatusParcelDoor,
                "time" : getActualTime(),
                "date" : getActualDate(),
                }
        print("Send status Mail")
    except:
        raise ValueError("Wrong format of data to transmit")
    try:
        print("Send status Mail correct")
        response = requests.post(url_Parcel_Door, data = json.dumps(data), headers = headers)
    except:
        raise ValueError("Wrong response")
    
def send_status(Message,Part,Status,UrlAdress):
    try:
        data = {"status" : Message,
                Part : Status,
                "time" : (datetime.now().strftime("%H:%M:%S")),
                "date" : (datetime.now().strftime("%d-%m-%Y")),
                }
        print("data collected")
    except:
        raise ValueError("Wrong format of data to transmit")
    try:
        print("Try to send status Mail")
        response = requests.post(UrlAdress, data=json.dumps(data), headers=headers)
        print("Send okay")
    except:
        print("Sending failed")
        raise ValueError("Send not sucessful")
    
