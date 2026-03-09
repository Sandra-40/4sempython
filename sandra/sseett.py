s={1,2,3,4,5,}
print(s)

s2={1,2,3,2,5,5,6,4,1}
print(s2)

print(type(s))

s3={'abc',1.09,52,True}
print(s3)

s3.add(12)
print(s3)

fs=frozenset([1,2,3,4,5])
print(fs)


s4=[]
print(s4)
for i in range(2,21,2):
    s4.append(i)
print(s4)