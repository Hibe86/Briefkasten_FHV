def send_status_Mail(StatusMail,StatusMailDoor):
    """Send status of Mailbox to server
Var in:
Status mail recived or removed (BOOL)
Status mailboxdoor open or closed (Bool)
Var out:
Response from Server (string)
"""
    import requests
    import json
    
    process_ID = "Mail"
    api_key = "wing_test"
    url = "http://domainname.org/api/Mailbox/" + process_ID   # todo: change the url -- "http://domainname.org/"
    
    # POST-Request
    data = { "Brieffach": StatusMail,
             "Briefkastentür": StatusMailDoor
             }
    headers = { 'Content-Type' : 'application/json', 'api_key' : api_key }
    response = requests.post(url, data = json.dumps(data), headers = headers)
    
    print(response.status_code)
    print(response.content)
    return response.content

def send_status_Parcel(StatusParcel):
    """Send status of parcel storage to Server
Var in:
Status parcel recived
Var out:
Response from Server (string)
"""
    import requests
    import json
    
    process_ID = "Parcel"
    api_key = "wing_test"
    url = "http://domainname.org/api/Mailbox/" + process_ID   # todo: change the url -- "http://domainname.org/"
    
    # POST-Request
    data = { "Paketfach": StatusParcel
             }
    headers = { 'Content-Type' : 'application/json', 'api_key' : api_key }
    response = requests.post(url, data = json.dumps(data), headers = headers)
    
    print(response.status_code)
    print(response.content)
    return response.content