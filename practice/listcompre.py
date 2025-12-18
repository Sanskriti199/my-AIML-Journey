
sq=[i*i for i in range(6)]
print(sq)

m=[i*i for i in range(6)if i%2!=0]
print(m)

nums=[-1,-2,-4,4,5,6]
n=[0 if val<0 else val for val in nums]
print(n)

words=["hello","python","me"]

print(words[0].upper())

words=[val.upper() for val in words]
print(words)