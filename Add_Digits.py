def calculatesum(temp):
    sum=0
    while(temp!=0):
          sum+=temp%10
          temp=temp//10
    return sum
number=int(input())
sum=calculatesum(number)
while (sum//10!=0):
    number=sum
    sum=calculatesum(number)
print(sum)