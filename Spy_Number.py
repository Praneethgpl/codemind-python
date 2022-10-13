number=int(input())
sum=0
product=1
while number!=0:
    sum+=number%10
    product*=number%10
    number=number//10
if sum==product:
    print("Spy Number")
else:
    print("Not Spy Number")