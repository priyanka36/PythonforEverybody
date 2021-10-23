
print(len('banana')*7)
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(pos)

greet = "Hello Bob"
zap = greet.lower()
print(zap)

zap = greet.upper()
print(zap)

nstr = greet.replace('Bob','Jane')
print(nstr)

nstr = greet.replace('o','x')
print(nstr)

greet = "   Hello Bob    "
print(greet.lstrip())

print(greet.rstrip())


stpos = data.find('@')
print(stpos)

stuff = "Hello\nWorld"

print(len(stuff))