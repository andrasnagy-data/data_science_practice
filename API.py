import requests
# saving the data in response
response = requests.get("http://api.open-notify.org/astros.json")
# checking the request
print(response.status_code)
print(response.json())

import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys = True, indent = 4)
    print(text)

# requesting data, specifying parameters in URL
response_specifying_parameters = requests.get("http://api.open-notify.org/iss-pass.json?lat=55&lon=12")
print(response_specifying_parameters.status_code)

# extracting the pass times from JSON object
pass_times = response_specifying_parameters.json()["response"]
jprint(pass_times)

# using loop to extract the risetimevalues
risetimes = []
for i in pass_times:
    time = i["risetime"]
    risetimes.append(time)
# data is in timestamp / epoch format
print(risetimes)

# importing datetime library
from datetime import datetime

# loop to transform format
times = []
for j in risetimes:
    time = datetime.fromtimestamp(j)
    times.append(time)
    # datetime format
    print(time)

# practice poke api request
response_poke = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
print(response_poke.status_code)
