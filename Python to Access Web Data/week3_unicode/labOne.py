import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input("Enter URL: ")


count = input("Enter count: ")
position = input("Enter position: ")


for i in range(int(count)):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    url = tags[int(position) - 1].get("href", None)
    print("Retrieving: ", url)
    i += 1
