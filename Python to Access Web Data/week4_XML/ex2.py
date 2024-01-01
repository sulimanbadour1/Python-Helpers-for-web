import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False


# 3. Extracting Data from XML
url = input("Enter location: ")
print("Retrieving", url)

uh = urllib.request.urlopen(url, context=ctx)
print(uh)
data = uh.read()
print("Retrieved", len(data), "characters")

tree = ET.fromstring(data)
counts = tree.findall(".//count")
print("Count:", len(counts))
sum = 0
for count in counts:
    sum += int(count.text)
print("Sum:", sum)
print("Done")
