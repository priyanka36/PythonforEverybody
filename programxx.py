import xml.etree.ElementTree as ET
import urllib.request,urllib.parse,urllib.error

fhand = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1392176.xml")

tree = ET.parse(fhand)
lst = tree.findall('comments/comment')
print('User count:',len(lst))
lst2=[]
for item in lst:
    count_value = item.find('count').text
    lst2.append(float(count_value))

print(lst2)
print("Sum is :",sum(lst2))