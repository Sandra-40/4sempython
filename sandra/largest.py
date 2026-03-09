def largest(a,b,c):
    if a>=b and a<=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
z=int(input("Enter another number: "))
result=largest(x,y,z)
print("The largest number is ",result)