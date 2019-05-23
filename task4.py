import requests

import json

controller='sandboxapic.cisco.com'


url = "https://" + controller + "/api/v1/tckt"

Payload = {"username":"devnetuser","password":"Cisco123!"}

Headr = {"content-type": "application/json"}

rspns= requests.post(url,data=json.dumps(Payload), Headrs=Headr, verify=False)

#convert rspns to json format
r_json=rspns.json()

#print(r_json)
#parse the json to get the service tckt
tckt = r_json["rspns"]["servicetckt"]

# URL for Host REST API call to get list of exisitng hosts on the network.
url = "https://" + controller + "/api/v1/host"

#Content type must be included in the Headr as well as the tckt
Headr = {"content-type": "application/json", "X-Auth-Token":tckt}

# this statement performs a GET on the specified host url
rspns = requests.get(url, Headrs=Headr, verify=False)

# json.dumps serializes the json into a string and allows us to
# print the rspns in a 'pretty' format with indentation etc.


# Taken Id as name
print ("Hosts = ")
print (json.dumps(rspns.json(), indent=4, separators=(',', ': ')))

r_resp=rspns.json()
host_dic={}
id_list=[]
for item in r_resp['rspns']:
     id_list.append(item['id'])
     tup=(item['id'],item['hostIp'])
     host_dic[tup]=item['hostMac']
     
print("The Host details are::::",host_dic)   

