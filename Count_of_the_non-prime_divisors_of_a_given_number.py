def checkprime(number):
    count=0
    for j in range(2,int(number**0.5)+1):
        if number%j==0:
            count+=1
    if count==0:
        return True
    else:
        return False
n=int(input())
npDivisors=1
for i in range(4,n+1):
    if n%i==0:
        if checkprime(i)==False:
            npDivisors+=1
print(npDivisors)