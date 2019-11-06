import requests 
url = "http://127.0.0.1:5000/cars"

import json 
 #other code 
 #save this to a file 
filename = 'cars.json' 
if filename:     
     # Writing JSON data     
  with open(filename, 'w') as f:         
    json.dump(data, f, indent=4)

#response = requests.get(url) 
#data = response.json() 
 
#for car in data["cars"]:     
    #print (car)
#output to console 
#print (data)