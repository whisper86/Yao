import json

with open("information.json", mode="r", encoding="utf-8") as f:
    information = json.dumps(f.read())
