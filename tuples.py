import re
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

just_time_list=list()

for line in handle:
    if line.startswith('From'):
        first_split = line.split()
        regex = '([0-9]{2}:[0-9]{2}:[0-9]{2})'
        just_time = re.findall(regex,line)
        if len(just_time)>0:
            just_time_list.append(just_time[0])

just_time_list.sort()


final_dict = {}

for just_time in just_time_list:
    hr = just_time.split(":")
    final_dict[hr[0]]=final_dict.get(hr[0],0)+1



for k,v in final_dict.items():
    print(k,v)
        
