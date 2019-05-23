# import requests libraries
import requests

#import json libraries
import json

controller='sandboxapic.cisco.com'
#given that controller='devnetapi.cisco.com/sandbox/apic_em'


# put the ip address of your apic-em controller 
url = "https://" + controller + "/api/v1/ticket"

#type the username and password to access the Controller
payload = {"username":"devnetuser","password":"Cisco123!"}

header = {"content-type": "application/json"}

response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

#conversion
r_json=response.json()
