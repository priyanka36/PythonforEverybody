import re
file1 = open("/home/priyanka/Desktop/assignment/regex_sum_1392172.txt","r")
numlist = list()
fnumlist =list()
for line in file1:
    line = line.rstrip()
    # print(line)
    # print("....................")
    stuff = re.findall('[0-9]+',line)
    numlist.append(stuff)
res = [ele for ele in numlist if ele != []]
flat_list = [float(item) for sublist in res for item in sublist]
print("Sum is : ",sum(flat_list) )

    