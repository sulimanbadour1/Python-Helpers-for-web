import urllib.request, urllib.parse, urllib.error
import json


url = "https://py4e-data.dr-chuck.net/comments_1953024.json"
print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), "characters")
info = json.loads(data)
print("Count:", len(info["comments"]))
sum = 0
for item in info["comments"]:
    sum += int(item["count"])
print("Sum:", sum)
