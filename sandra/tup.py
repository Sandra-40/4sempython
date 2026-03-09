t1=()
print(t1)

t2 = (10,20,30)
print(t2)

t3=1,2,3
print(t3)

t4='a','b',"bla",0.81
print(t4)

t5=tuple()
print(t5)

t=tuple("tennis")
print(t)

t6=(1, (3,4), 5)
print(t6)

print(t2[0])
print(t4[2])
print(t4[-2])
print(t2[-3])

t7=(1,2,3,4,5,6,7)
print(t7[1:4])
print(t7[1::2])

t8=t2+t3
print(t8)

print(t3 * 3)

print(5 in t7)
print(9 in t7)

for i in t7:
    print(i)