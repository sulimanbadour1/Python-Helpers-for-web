import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input("Enter - ")
url = input("Enter URL: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("span")
sum = 0
count = 0
for tag in tags:
    count += 1
    sum += int(tag.contents[0])
print("Count", count)
print("Sum", sum)
