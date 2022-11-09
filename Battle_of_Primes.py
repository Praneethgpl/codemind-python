def checkprime(number):
    count=0
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            count+=1
    return count
n1=int(input())
n2=int(input())
s=n1+n2
i=1
while True:
    if checkprime(s+i)==0:
        break
    i+=1
print(i)