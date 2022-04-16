def send_status(Sensor,Status):
    import requests
    import json
    
    sensor_id = Sensor 
    api_key = "wing_test"
    url = "http://domainname.org/api/sensors/" + Sensor   # todo: change the url -- "http://domainname.org/api/sensors/"
    
    # Post request
    data={Sensor : Status}
    headers = { 'Content-Type' : 'application/json', 'api_key' : api_key }
    response = requests.post(url, data = json.dumps(data), headers = headers)
    
    return response.content

def send_error(Sensor, Errorcode):
    import requests
    import json
    
    sensor_id = Sensor 
    api_key = "wing_test"
    url = "http://domainname.org/api/sensors/" + Sensor   # todo: change the url -- "http://domainname.org/api/sensors/"
    
    # Post request
    data={Sensor : Errorcode}
    headers = { 'Content-Type' : 'application/json', 'api_key' : api_key }
    response = requests.post(url, data = json.dumps(data), headers = headers)
    
    return response.content