import urllib.request,urllib.parse,urllib.error 
from bs4 import BeautifulSoup 
import ssl 
import requests

ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode  = ssl.CERT_NONE 

url = input("Enter the URL")
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('a')
list_data=[]
count = 0
for tag in tags :
    data=tag.get('href',None)
    if count == 17:
        list_data.append(data)
        nextpage = requests.get(tag['href'])
        
        html = urllib.request.urlopen(nextpage.url,context=ctx).read()
        soup = BeautifulSoup(html,'html.parser')
        tags = soup('a')
        count = 0
        for tag in tags :
            data=tag.get('href',None)
            print(tag)
            if count == 17:
                list_data.append(data)
                nextpage = requests.get(tag['href'])
                html = urllib.request.urlopen(nextpage.url,context=ctx).read()
                soup = BeautifulSoup(html,'html.parser')
                tags = soup('a')
                count = 0
                for tag in tags :
                    data=tag.get('href',None)
                    if count == 17:
                        list_data.append(data)
                        nextpage = requests.get(tag['href'])
                        html = urllib.request.urlopen(nextpage.url,context=ctx).read()
                        soup = BeautifulSoup(html,'html.parser')
                        tags = soup('a')
                        count = 0
                        for tag in tags :
                            data=tag.get('href',None)
                            if count == 17:
                                list_data.append(data)
                                nextpage = requests.get(tag['href'])
                                html = urllib.request.urlopen(nextpage.url,context=ctx).read()
                                soup = BeautifulSoup(html,'html.parser')
                                tags = soup('a')
                                count = 0
                                for tag in tags :
                                    data=tag.get('href',None)
                                    if count == 17:
                                        list_data.append(data)
                                        nextpage = requests.get(tag['href'])
                                        html = urllib.request.urlopen(nextpage.url,context=ctx).read()
                                        soup = BeautifulSoup(html,'html.parser')
                                        tags = soup('a')
                                        count = 0
                                        for tag in tags :
                                            data=tag.get('href',None)
                                            if count == 17:
                                                list_data.append(data)
                                                nextpage = requests.get(tag['href'])
                                                html = urllib.request.urlopen(nextpage.url,context=ctx).read()
                                                soup = BeautifulSoup(html,'html.parser')
                                                tags = soup('a')
                                                count = 0
                                                for tag in tags :
                                                    data=tag.get('href',None)
                                                    if count == 17:
                                                        list_data.append(data)
                                                    count+=1
                                            count+=1                                        
                                    count+=1
                            count +=1
                    count +=1
            count+=1                       
    count+=1

print(list_data)