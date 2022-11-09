def checkprime(number):
    count=0
    for j in range(1,int(number**0.5)+1):
        if number%j==0:
            count+=1
    return count
n1=int(input())
if n1==1:
    n1+=1
n2=int(input())
for i in range(n1,n2+1):
    if checkprime(i)==1:
        print(i)