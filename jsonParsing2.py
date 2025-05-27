import json

with open('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Python_API_Testing_Project1/demo.json') as f:
    data = json.load(f)

print(data["phone_numbers"][0])

print(data["address"]["zipcode"])
