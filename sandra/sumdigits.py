num=int(input("Enter a number:"))
if 1000<=num<=9999:
    digit1=num//1000
    digit2=(num//100)%10
    digit3=(num//10)%10
    digit4=num%10
    total=digit1+digit2+digit3+digit4
    print("Sum of digits:",total)
else:
    print("Please enter a valid number")