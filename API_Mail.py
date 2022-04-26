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

# set actual time
def getActualTime():
    """set and format actual time
Input variables
None

Output variables
acutal time in format Hour:Minute:Second
"""
    actTime = (datetime.now().strftime("%H:%M:%S")) # format Date Time to correct format
    return actTime

# set actual date
def getActualDate():
    """set and format actual date
Input variables
None

Output variables
acutal date in format Day-Month-Year
"""
    actDate = (datetime.now().strftime("%d-%m-%Y"))
    return actDate

# prepare Data as json format to send
def jsonData(MailboxPart, Message,StatusJson):
    """Prepare JSON data to send

Input variabels:
Part of mailbox (string)
Message (string)
Status (int) -> 0/1

Output:
Json data
"""
    sendData = {"status" : Message,
                MailboxPart : StatusJson,
                "time" : getActualTime(),
                "date" : getActualDate(),
                }
    return sendData

# ----------------------------------------------------
# send routines to url
# ----------------------------------------------------

# send status of mailbox to url
def send_status_mail(Message_change,StatusMail):
    """Send status mail to URL

Input variabels:
Change message (incoming/outgoing)
Status of input (int) -> 0/1

Output:
None
"""
    try:
        data = jsonData("brieffach",Message_change,StatusMail)
    except:
        raise ValueError("Wrong format of data to transmit")
    try:
        response = requests.post(url_Mail, data = json.dumps(data), headers = headers)
    except:
        raise ValueError("Wrong response")
    
    
# send status of parcel box to url
def send_status_parcel(Message_change,StatusParcel):
    """end status Parcel to URL

Input variabels:
Change message (incoming/outgoing)
Status of input (int) -> 0/1

Output:
None
"""
    try:
        data = jsonData("packetfach",Message_change,StatusParcel)
    except:
        raise ValueError("Wrong format of data to transmit")
    try:
        response = requests.post(url_Parcel, data = json.dumps(data), headers = headers)
    except:
        raise ValueError("Wrong response")
    
def send_status_mail_Door(Message_change,StatusMailDoor):
    """end status mailboxdoor to URL

Input variabels:
Change message (open/close)
Status of input (int) -> 0/1

Output:
None
"""
    try:
        data = jsonData("brieffachtuer",Message_change,StatusMailDoor)
    except:
        raise ValueError("Wrong format of data to transmit")
    try:
        response = requests.post(url_Mail_Door, data = json.dumps(data), headers = headers)
    except:
        raise ValueError("Wrong response")
    
def send_status_parcel_Door(Message_change,StatusParcelDoor):
    """end status parcel door to URL

Input variabels:
Change message (open/close)
Status of input (int) -> 0/1

Output:
None
"""
    try:
        data = jsonData("packetfach",Message_change,StatusParcelDoor)
    except:
        raise ValueError("Wrong format of data to transmit")
    try:
        response = requests.post(url_Parcel_Door, data = json.dumps(data), headers = headers)
    except:
        raise ValueError("Wrong response")
