'''
Parse the json file demo1.json to retrieve the price of the book named testing.
Note - Index may change
'''

import json

with open("/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Python_API_Testing_Project1/demo1.json") as f:
    data = json.load(f)

print(type(data))

products = data["store"]["products"][1]["items"]
print(products)

for product in products:
    if product["id"] == "Testing":
        print(product["price"])



