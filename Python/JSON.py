# JSON -> JavaScript Object Notation

import json

string = """
{
    "people": 
    [
        {
            "Name": "Sudais",
            "Gender": "Male",
            "Phone": "0333-3137735",
            "Emails": "sudiasahmed710@gmail.com",
            "Nationality": "Pakistan", 
            "Religion": "Islam"
        },
        {
            "Name": "Shifa",
            "Gender": "Female",
            "Phone": "0336-8478422",
            "Emails": "shifaahmed2205@gmail.com",
            "Nationality": "Pakistan", 
            "Religion": "Islam" 
        }
    ]
}
"""

#############################################     JSON STRINGS      ############################################## 

# json.loads -> Converts json format into a python objects
# json.dumps -> Converts python objects into json format


data = json.loads(string)
print(json.dumps(data, indent = 4))

for person in data["people"]:
    del person["Emails"]
    
new_string = json.dumps(data, indent = 4)
print("\n--------------------------------------------------------------------------------------\n\n", new_string)

#############################################     JSON FILES      ##############################################

with open("sample.json") as file:
    json_data = json.load(file)
    
    emails = ["sudaisahmed710@gmail.com", "shifaahmed2205@gmail.com"]
    i = 0
    
    for person in json_data["people"]:
        person["Email"] = emails[i]
        i += 1
        
with open("sample.json", "w") as file:
    json.dump(json_data, file, indent = 4)   
