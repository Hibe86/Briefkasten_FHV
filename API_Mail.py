def send_status(Message,Part,Status,UrlAdress,headers = {"Content-Type" : "application/json"}):
    """API sends JSON-Data to webservice
obligatory variables:
Message (string): message that shows what happend (recived, picked, door status)
part(string): which part of the mailbox is affected (brieffach, briefkastentuere, packetfachtuere)
status(BOOL): Which actual status has the input
urlAdredd (string): to which url the data is going to be sent

non mandatory variables:
headers (string): standard config is {"Content-Type" : "application/json"}

output and return:
Value Errors and Transmit Errors
"""
    from datetime import datetime
    import requests
    import json

    try:
        data = {"status" : Message,
                Part : Status,
                "time" : (datetime.now().strftime("%H:%M:%S")),
                "date" : (datetime.now().strftime("%d-%m-%Y")),
                }
    except:
        raise ValueError("Wrong format of data to transmit")
    try:
        response = requests.post(UrlAdress, data=json.dumps(data), headers=headers)
    except:
        raise ValueError("Send not sucessful")
