#!/Python3/python
import urllib.request
import cgi


# If you are using Python 3+, import urllib instead of urllib2

import json 
print"Content-Type: text/html"
print

data1=cgi.FormContent()
print data

data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["Environment", "mGroup", "mFamily", "Material", "localizedAttack", "Conc", "days", "Temperature (deg C)", "rate1"],
                    "Values": [ [ "value", "value", "value", "value", "value", "value", "0", "value", "0" ], [ "value", "value", "value", "value", "value", "value", "0", "value", "0" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/053fd63ff313491a94553e4597480612/services/8adf385ca8f74d399a95f35b096571de/execute?api-version=2.0&details=true'
api_key = 'tUGXC2NFb5s5ZykrvnA9RgRup3UbwxEymEFXU7I6LCIyulNbLJYJUBhNSSMQQio4MIFUbhGiIAYvkCVmIpmvXA==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers) 

try:
    response = urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result) 
except urllib.request.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))                 