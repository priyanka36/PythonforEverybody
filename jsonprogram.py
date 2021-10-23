import urllib.request,urllib.parse,urllib.error
import json

serviceurl = ""

while True:
    address = input("Enter locations:")
    if len(address)<1:
        break
    
    url = serviceurl+urllib.parse.urlencode({'address':address})
    print('Retrieving',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved",len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None 

    if not js or 'status' not in js or js['status']!= 'OK':
        print('====Failure To Retrive=====')
        print(data)
        continue
    
    lat = js['results'][0]['geometry']["location"]["lat"]
    lng = js['results'][0]['geometry']["location"]["lng"]
    print("Latitude:"f{lat},"Longitude:"f{lng})


