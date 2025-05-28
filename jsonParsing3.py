import json

with open("/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Python_API_Testing_Project1/demo1.json") as f:
    data = json.load(f)

print(type(data))

products = data["store"]["products"]

print(type(products))

print(products[1]["items"][0]["price"])