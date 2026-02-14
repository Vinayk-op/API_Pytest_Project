import requests
import json


# Quick Reference: String vs. File
# Function 	        Target	        Action	                                     Result
# json.loads()	    String	    Deserialize (JSON string → Python object)	    Python dict or list
# json.load()	    File	    Deserialize (File → Python object)	            Python dict or list
# json.dumps()	    String	    Serialize (Python object → JSON string)	        JSON-formatted str
# json.dump()	    File	    Serialize (Python object → File)	            Data written to disk

url = "https://fakerestapi.azurewebsites.net"

head = {
    "accept": "text/plain",
    "Content-Type": "application/json"
}

json_file = open("./payload.json")
request_body = json.load(json_file)

response = requests.post(url+"/api/v1/Activities", headers=head, data=json.dumps(request_body))

print(response.text)
print("##############")
print(response.json())
