name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = {}
list_lines = list()

for line in handle:
    if line.startswith("From:"):
        a = line.split()
        
        counts[a[1]] = counts.get(a[1],0)+1



count=0

for k,v in counts.items():
    if count == 0:
        maximum = v
        max_key = k
    else:
        if maximum<v:
            maximum = v
            max_key = k
    count+=1

    
print(max_key,maximum)
    

