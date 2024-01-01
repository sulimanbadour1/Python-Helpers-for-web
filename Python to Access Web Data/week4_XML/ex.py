import xml.etree.ElementTree as ET

# XML EXERCISES

# 1. Extracting Data from XML
# data = """
# <person>
#     <name>Chuck</name>
#     <phone type="intl">
#         +1 734 303 4456
#     </phone>
#     <email hide="yes">
#     chucj@mail.com
#     </email>
# </person>"""


# tree = ET.fromstring(data)
# print("Name:", tree.find("name").text)
# print("Phone:", tree.find("phone").text.strip())
# print("Attr:", tree.find("phone").get("type"))
# print("email:", tree.find("email").text.strip())
# print("Attr:", tree.find("email").get("hide"))


# 2. Extracting Data from XML
data = """
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
"""

stuff = ET.fromstring(data)
lst = stuff.findall("users/user")

print("User count:", len(lst))
for item in lst:
    print("Name:", item.find("name").text)
    print("Id:", item.find("id").text)
    print("Attribute:", item.get("x"))
