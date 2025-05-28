import json

with open("/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Python_API_Testing_Project1/demo1.json") as f1:
    content1 = json.load(f1)

with open("/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Python_API_Testing_Project1/demo2.json") as f2:
    content2 = json.load(f2)

assert content1 == content2

