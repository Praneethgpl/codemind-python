number=int(input())
square=number*number
sum=0
while(square!=0):
    sum=sum+square%10
    square=square//10
if int(sum)==number:
    print("Neon Number")
else:
    print("Not Neon Number")