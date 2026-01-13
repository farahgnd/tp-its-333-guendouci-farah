import json

f = open('data.json', 'r', encoding='utf-8')
data = json.load(f)
f.close()

print(data)
print(data["features"])
print(data["features"][0]["geometry"])

for i in data["features"]:
    print(i["geometry"]["coordinates"][0])
data["features"][0]["geometry"]["coordinates"] = [2.0, 48.0]

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)
data["features"][0]["properties"]["name"] = "New Place"

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)