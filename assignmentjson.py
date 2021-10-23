import urllib.request,urllib.parse,urllib.error 
import json 

service_url = "http://py4e-data.dr-chuck.net/comments_1392177.json"

uh = urllib.request.urlopen(service_url)

data = uh.read().decode()

info = json.loads(data)


Sum = 0
for key, value in info.items():
    if key == "comments":
        sum = 0
        for i,items in enumerate(value):
            sum+=(items['count'])
        print(sum)
