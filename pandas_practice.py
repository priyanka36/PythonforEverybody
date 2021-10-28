import pandas as pd 

df = pd.DataFrame({'num_legs':[2,4,8,0],
'num_wings':[2,0,0,0],'num_specimen':[10,2,1,8]},index=['falcon', 'dog', 'spider', 'fish'])


print(df)

# We use random state to ensure the reproducability of the materials

# Extract 3 random elements from the Series df['num_legs']:
print(df['num_legs'].sample(n=3,random_state=1))

print(df.sample(frac=0.5))


dictnoary = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]

df = pd.DataFrame(dictnoary)

print(type(df.iloc[0]))

print(df.iloc[0])
print(df.iloc[:3])
print(df.iloc[True,False,True])


data = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(data=d, index=['a','b','c'])
print(ser)