import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl 

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE 

url = input("Enter the url")
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

tags= soup("span")
list_data =[]
for tag in tags:
    data = tag.contents[0]
    list_data.append(float(data))
print("Sum is : ", sum(list_data)) 

